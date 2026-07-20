from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        ([1]),
        ([10]),
        ([5]),
        ([0, 4]),
        ([11, 4]),
        ([0, 11, 7]),
    ]
)
def test_function(pytestconfig, inputs):
    expected_output = ""
    for number in inputs:
        expected_output += f"Enter a number between 1 and 10: > {number}\n"
        if number < 1 or number > 10:
            expected_output += "That number is out of range!\n"
    expected_output += f"You entered: {inputs[-1]}\n"
    run_script(__file__, inputs, expected_output)
