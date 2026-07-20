
from p1_util.tests.test_util import run_script, get_script_dir, restore_files

import pytest


@pytest.mark.parametrize(
    "filename,file_content,expected_output_content",
    [
        (
            "input.txt",
            "a\n\n\nb\nc\n\nd\n",
            "a\nb\nc\nd\n"
        ),
        (
            "input.txt",
            "hello\n\nworld\n\n\npython\n",
            "hello\nworld\npython\n"
        ),
        # empty lines at the very start and the very end of the file
        (
            "input.txt",
            "\n\nfirst\nlast\n\n\n",
            "first\nlast\n"
        ),
        # lines that only contain spaces are NOT empty and have to be kept
        (
            "input.txt",
            "a\n   \n\nb\n \n",
            "a\n   \nb\n \n"
        ),
        # a file without any non-empty lines
        (
            "input.txt",
            "\n\n\n",
            ""
        ),
        # the program should use the filename the user typed
        (
            "notes.txt",
            "buy milk\n\ncall mom\n",
            "buy milk\ncall mom\n"
        ),
    ]
)
def test_function(pytestconfig, filename, file_content, expected_output_content):
    script_dir = get_script_dir(__file__)

    with restore_files(__file__, "input.txt", filename, "output.txt"):
        # Create input file
        with open(script_dir / filename, "w") as f:
            f.write(file_content)

        inputs = [filename]

        expected_output = (
            f"Provide a filename for the file which should have it's empty lines removed: > {inputs[0]}\n"
        )

        run_script(__file__, inputs, expected_output)

        # Check output file
        with open(script_dir / "output.txt") as f:
            content = f.read()

        assert content == expected_output_content, (
            f"For a file containing {file_content!r}, output.txt should contain "
            f"{expected_output_content!r}, but it contains {content!r}"
        )
