from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([17],False),
        ([18],True),
        ([7],False),
        ([79],True),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"Let's determine whether you can vote!\nWhat is your age? > {inputs[0]}\n"
    if expected:
        expected_output += "Congratulations, you get to vote!\n"
    else:
        expected_output += "Unfortunately, you don't get to vote yet...\n"
    run_script(__file__, inputs, expected_output)
