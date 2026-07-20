from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([5,5,5],5.0),
        ([5,3,2],3.3333333333333335),
        ([125,46,15],62.0),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"What is your first number? > {inputs[0]}\nWhat is your second number? > {inputs[1]}\nWhat is your third number? > {inputs[2]}\nThe total average is {expected}.\n"
    run_script(__file__, inputs, expected_output)
