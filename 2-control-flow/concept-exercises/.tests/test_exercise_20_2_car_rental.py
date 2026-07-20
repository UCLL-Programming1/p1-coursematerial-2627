from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([25, "yes"],True),
        ([21, "yes"],True),
        ([20, "yes"],False),
        ([21, "no"],False),
        ([18, "no"],False),
        ([30, "no"],False),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = (
        "Let's find out if you can rent a car!\n"
        f"How old are you? > {inputs[0]}\n"
        f"Do you have a driver's license? (yes/no): > {inputs[1]}\n"
    )
    if expected:
        expected_output += "You can rent a car!\n"
    else:
        expected_output += "Sorry, you cannot rent a car.\n"
    run_script(__file__, inputs, expected_output)
