"""Check that the Programming 1 installation was done correctly.

Run this from the VS Code terminal, inside the course material folder:

    python3 checkinstall.py

The script prints a checklist. Every item that is not checked off comes with
a short explanation of what to do about it.

This file must keep working on a broken installation, so it uses nothing but
the Python standard library, and no syntax that is newer than Python 3.0
(a Python 2 interpreter should be able to read it far enough to complain).
"""

import sys

if sys.version_info[0] < 3:
    sys.stdout.write(
        "\nThis is Python {0}, but the course needs Python 3.\n"
        "Try running the command again with 'python3' instead of 'python'.\n"
        "If that does not work either, install Python 3 first.\n".format(
            sys.version.split()[0]))
    raise SystemExit(1)

import shutil

from pathlib import Path


MINIMUM_PYTHON = (3, 10)

# Where this script lives: the top of the course material folder.
ROOT = Path(__file__).resolve().parent

# Things the download should contain. If one of these is missing, the zip was
# not unpacked completely or the wrong folder was opened.
EXPECTED_ENTRIES = ["requirements.txt", ".p1_util", ".vscode", "0-intro"]

# Extension id -> name as it appears in the VS Code marketplace.
REQUIRED_EXTENSIONS = [
    ("ms-python.python", "Python"),
    ("ms-toolsai.jupyter", "Jupyter"),
]

# Module to import -> what to call it in a message.
REQUIRED_PACKAGES = [
    ("pytest", "pytest"),
    ("ipywidgets", "ipywidgets"),
    ("IPython", "ipython"),
    ("jupyter_core", "jupyter"),
]

INSTALL_COMMAND = "python -m pip install -r requirements.txt"

INSTALL_HINT = ("Open a terminal in the course material folder and run:\n"
                + INSTALL_COMMAND)


# --- output helpers ---------------------------------------------------------

def supports(text):
    """Whether the terminal can print this text without blowing up."""
    encoding = getattr(sys.stdout, "encoding", None) or "ascii"
    try:
        text.encode(encoding)
    except (UnicodeError, LookupError):
        return False
    return True


CHECKED = "✓" if supports("✓") else "v"
UNCHECKED = "✗" if supports("✗") else "x"
ARROW = "→" if supports("→") else "->"

WIDTH = 62


def rule(character="-"):
    print(character * WIDTH)


# Whether the check that was reported last printed an explanation. Used to
# keep a blank line between an explanation and the next item.
had_notes = [False]


def report(passed, label, notes=()):
    """Print one line of the checklist, plus any explanation underneath."""
    print(" [{0}] {1}".format(CHECKED if passed else UNCHECKED, label))
    first = "     {0} ".format(ARROW)
    for note in notes:
        for index, line in enumerate(note.splitlines()):
            print((first if index == 0 else " " * len(first)) + line)
    had_notes[0] = bool(notes)
    return passed


# --- the individual checks --------------------------------------------------

def check_python_version():
    version = ".".join(str(number) for number in sys.version_info[:3])
    wanted = ".".join(str(number) for number in MINIMUM_PYTHON)

    if sys.version_info[:2] >= MINIMUM_PYTHON:
        return report(True, "Python {0} is installed".format(version))

    return report(False, "Python {0} is installed".format(version), [
        "The course needs Python {0} or newer. Install a more recent\n"
        "version from https://www.python.org/downloads/ and then close\n"
        "and reopen VS Code.".format(wanted)])


def is_importable(module):
    try:
        import importlib.util
        return importlib.util.find_spec(module) is not None
    except Exception:
        return False


def check_packages():
    label = "The Python packages from requirements.txt are installed"
    missing = [name for module, name in REQUIRED_PACKAGES
               if not is_importable(module)]

    if not missing:
        return report(True, label)

    notes = ["Not installed: {0}.\n{1}".format(", ".join(missing), INSTALL_HINT)]

    # Classic cause: pip installed the packages for a different Python than
    # the one running this script.
    if shutil.which("pytest") is not None and "pytest" in missing:
        notes.append("There is a 'pytest' command on your computer, but this\n"
                     "Python cannot see it. That usually means pip installed\n"
                     "into a different Python. The 'python -m pip' command\n"
                     "above avoids that.")

    return report(False, label, notes)


def check_p1_util():
    label = "p1_util is installed"

    try:
        import importlib.util
        spec = importlib.util.find_spec("p1_util")
    except Exception:
        spec = None

    if spec is None or not spec.origin:
        return report(False, label, [
            "p1_util is not installed.\n" + INSTALL_HINT])

    location = Path(spec.origin).resolve()
    if ROOT in location.parents:
        return report(True, label)

    return report(False, label, [
        "p1_util was found in\n{0}\n"
        "instead of inside your course material folder. That is probably a\n"
        "leftover from an older download. Reinstall it from the course\n"
        "material folder with:\n"
        "python -m pip uninstall p1-util\n{1}".format(location.parent, INSTALL_COMMAND)])


CHECKS = [
    check_python_version,
    check_packages,
    check_p1_util,
]


def main():
    print("")
    rule("=")
    print(" Programming 1 - checking your installation")
    rule("=")
    print("")

    results = []
    for check in CHECKS:
        try:
            results.append(check())
        except Exception as error:
            results.append(report(False, check.__name__, [
                "This check itself went wrong ({0}). Show this to your\n"
                "teacher.".format(error)]))
        if had_notes[0]:
            print("")

    unchecked = results.count(False)

    if not had_notes[0]:
        print("")
    rule()
    if unchecked == 0:
        print(" Everything checks off. You are ready to start. Nice work!")
    elif unchecked == 1:
        print(" 1 item is not checked off yet. Read the {0} line above and\n"
              " run this script again afterwards.".format(ARROW))
    else:
        print(" {0} items are not checked off yet. Read the {1} lines above\n"
              " and run this script again afterwards.".format(unchecked, ARROW))
        print(" Work through them from top to bottom: the first one is often\n"
              " the cause of the ones below it.")
    rule()
    print("")

    return 0 if unchecked == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
