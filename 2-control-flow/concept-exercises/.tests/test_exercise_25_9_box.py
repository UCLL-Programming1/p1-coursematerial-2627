from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "string",
    [
        "Hello",
        "Python",
        "Hi",
        "Python is fun!",
        "X",
    ]
)
def test_function(pytestconfig, string):
    line = "+" + "-" * (len(string) + 2) + "+"
    expected_output = (
        f"Enter the string you want to put in a box: > {string}\n"
        f"{line}\n"
        f"| {string} |\n"
        f"{line}\n"
    )
    run_script(__file__, [string], expected_output)
