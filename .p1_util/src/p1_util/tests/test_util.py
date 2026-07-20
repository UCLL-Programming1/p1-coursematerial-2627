import ast
import io
import os
import difflib
import traceback
from contextlib import contextmanager
from pathlib import Path

import pytest

class _OutOfInputs(BaseException):
    """Internal signal; BaseException so student `except Exception` can't swallow it."""


## CAPTURING OUTPUT OF FUNCTIONS THAT USE print() AND input() ##

class CapturedOutput:
    def __init__(self):
        self._buffer = io.StringIO()

    def capture(self):
        """Return everything printed so far (including echoed input() prompts)."""
        return self._buffer.getvalue()

@contextmanager
def capture_outputs(inputs=None):
    """Capture stdout and feed scripted answers to input() inside the block.

    Usage:
        with capture_outputs(["Mary"]) as output:
            some_function()
        assert output.capture() == "What is your name? Mary\\nHello Mary!\\n"

    input() prompts AND the provided answers (followed by a newline) are echoed
    into the captured output, just like in a real terminal. Note: stdout is
    patched inside the block, so print(output.capture()) only shows something
    once the block has exited.
    """
    remaining_inputs = [str(i) for i in (inputs or [])]
    output = CapturedOutput()

    def fake_input(prompt=""):
        output._buffer.write(str(prompt))  # the prompt is shown, just like in the terminal
        if not remaining_inputs:
            print("⟨no input left⟩")
            raise _OutOfInputs
        answer = remaining_inputs.pop(0)
        output._buffer.write(answer + "\n")  # what the user typed is shown too, followed by the enter
        return answer

    with pytest.MonkeyPatch.context() as monkeypatch:
        monkeypatch.setattr("builtins.input", fake_input)
        monkeypatch.setattr("sys.stdout", output._buffer)
        yield output

# --- locating the script under test -----------------------------------------
#
# A test file is named 'test_' + the name of the script it runs, and sits
# either next to that script (while authoring, in src/) or in a hidden
# '.tests' folder beside it (in the student repo):
#
#   src/.../01-guest-list/        |  <chapter>/concept-exercises/
#     solution.py                 |    exercise_50_1_guest_list.py
#     test_solution.py            |    .tests/test_exercise_50_1_guest_list.py
#
# Every helper below takes the test's own __file__ and works the rest out, so
# the build never has to rewrite a test's contents.

TEST_PREFIX = "test_"
HIDDEN_TESTS_DIR = ".tests"

def fail_test(message):
    pytest.fail(message, pytrace=False,
)


def get_script_dir(test_file):
    """The folder the script under test lives in."""
    directory = Path(test_file).parent
    if directory.name == HIDDEN_TESTS_DIR:
        return directory.parent
    return directory


def _script_path(test_file):
    name = Path(test_file).name
    if not name.startswith(TEST_PREFIX):
        fail_test(
            f"\n❌ Test file '{name}' should be named "
            f"'{TEST_PREFIX}<script name>.py'.\n")
    return get_script_dir(test_file) / name[len(TEST_PREFIX):]


def run_script(test_file, inputs, expected_output):
    """Run the student's script and compare its output with the expected one."""
    script = _script_path(test_file)
    run_student_script(script.parent, script.name, inputs, expected_output)


def call_function(test_file, function_name, args, inputs=None,
                  expected_output=None):
    """Call one function from the student's script and return its result."""
    script = _script_path(test_file)
    return call_student_function(script.parent, script.name, function_name,
                                 args, inputs, expected_output)


def restore_files(test_file, *names):
    """Snapshot the named files next to the script and revert them on exit."""
    return _restore_files(get_script_dir(test_file), names)


# The _restore_files context manager snapshots the named files in the script
# directory on entry and reverts them on exit (restoring the original contents,
# or deleting files that did not exist), so tests that read and write files
# leave the directory exactly as they found it.
@contextmanager
def _restore_files(directory, names):
    saved = {}
    for name in names:
        path = Path(directory) / name
        saved[name] = path.read_bytes() if path.exists() else None
    try:
        yield
    finally:
        for name, content in saved.items():
            path = Path(directory) / name
            if content is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(content)

def _student_traceback(error):
    """Format an exception without the frames that come from this helper file."""
    tb = traceback.TracebackException.from_exception(error)
    tb.stack = traceback.StackSummary.from_list(
        [frame for frame in tb.stack if frame.filename != __file__]
    )
    return "".join(tb.format())

def run_student_script(script_dir, script_name, inputs, expected_output):
    script_path = Path(script_dir) / script_name
    if not script_path.exists():
        fail_test(f"\n❌ Could not find the file '{script_name}'.\n")

    source = script_path.read_text()
    try:
        code = compile(source, str(script_path), "exec")
    except SyntaxError:
        fail_test(
            f"\n❌ Script crashed with error\n"
            f"{traceback.format_exc(limit=0)}\n"
        )

    # Run the script in-process with input() and stdout patched, so that the
    # captured output shows the provided inputs echoed after each prompt,
    # exactly as a real terminal session would look. The working directory is
    # set to the script's folder (like before, when it ran as a subprocess),
    # so scripts that read/write files keep working.
    error_text = None
    out_of_inputs = False
    previous_cwd = os.getcwd()
    os.chdir(script_dir)
    try:
        with capture_outputs(inputs) as output:
            try:
                exec(code, {"__name__": "__main__"})
            except _OutOfInputs:
                out_of_inputs = True
            except SystemExit:
                pass  # a script may end itself with sys.exit(); that is not a crash
            except Exception as error:
                error_text = _student_traceback(error)
    finally:
        os.chdir(previous_cwd)

    actual_output = output.capture()
    expected_output = str(expected_output)

    if out_of_inputs:
        print("=== Program Output ===")
        print(actual_output)
        fail_test(
            f"\n❌ Too many input() calls: a correct program would only ask for the exact amount of inputs provided by this test, but your program asked for more.\n"
        )

    # If there was an error, show it clearly
    if error_text is not None:
        print("=== Program Output ===")
        print(actual_output)
        fail_test(
            f"\n❌ Script crashed with error\n"
            f"{error_text}\n"
        )

    # Compare outputs
    if actual_output != expected_output:
        diff = "\n".join(
            difflib.unified_diff(
                expected_output.splitlines(),
                actual_output.splitlines(),
                fromfile="expected",
                tofile="actual",
                lineterm=""
            )
        )
        print(f"=== Program Output ===\n{actual_output}\n")
        fail_test(
            # f"=== Expected Program Output ===\n{expected_output}\n"
            f"\n❌ Output mismatch!\n"
            f"{diff}\n"
            f"\ninputs: {inputs}\n"
        )

## TESTING INDIVIDUAL FUNCTIONS ##

def _load_definitions(script_path):
    # Parse the file and keep only definitions (imports, functions, classes),
    # dropping top-level statements so importing does not run the script's
    # input()/print() driver code.
    source = Path(script_path).read_text()
    tree = ast.parse(source, filename=str(script_path))
    tree.body = [
        node for node in tree.body
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    ]
    ast.fix_missing_locations(tree)
    namespace = {}
    exec(compile(tree, str(script_path), "exec"), namespace)
    return namespace

# --- Testing individual functions with side effects (print / input) --------
# These functions
#  - call a specific function in a student script. (stripping the script of all top-level statements)
#  - return the value of the function (so that it can be inspected)
#  - pass any potential input that is needed to the function (if the function uses input())
#  - check whether the output (prompts + print) of the function corresponds to the expected output. (Raises an assertion error if it doesn't)
def call_student_function(script_dir, script_name, function_name, args, inputs=None, expected_output=None):
    if not script_name.endswith(".py"):
        script_name += ".py"
    script_path = Path(script_dir) / script_name

    if not script_path.exists():
        fail_test(f"\n❌ Could not find the file '{script_name}'.\n")

    try:
        namespace = _load_definitions(script_path)
    except Exception as error:
        fail_test(
            f"\n❌ Your code could not be loaded because of an error:\n{_student_traceback(error)}\n"
        )

    if function_name not in namespace or not callable(namespace[function_name]):
        fail_test(
            f"\n❌ No function named '{function_name}' was found.\n"
            f"Make sure you define a function called '{function_name}'.\n"
        )

    function = namespace[function_name]
    call_args = list(args)
    out_of_inputs = False

    with capture_outputs(inputs) as output:
        try:
            actual_return = function(*call_args)
        except _OutOfInputs:
            out_of_inputs = True
        except Exception as error:
            arguments = ", ".join(repr(a) for a in args)
            fail_test(
                f"\n❌ Calling {function_name}({arguments}) raised an error:\n{_student_traceback(error)}\n"
            )

    actual_output = output.capture()
    if out_of_inputs:
        print("=== Program Output ===")
        print(actual_output)
        fail_test(
            f"\n❌ Too many input() calls: a correct function would only ask for the exact amount of inputs provided by this test, but your function asked for more.\n"
        )

    if expected_output is not None and actual_output != expected_output:
        diff = "\n".join(
            difflib.unified_diff(
                expected_output.splitlines(),
                actual_output.splitlines(),
                fromfile="expected",
                tofile="actual",
                lineterm=""
            )
        )
        fail_test(
            f"\n❌ Output mismatch when calling {function_name}!\n{diff}\n"
        )

    return actual_return
