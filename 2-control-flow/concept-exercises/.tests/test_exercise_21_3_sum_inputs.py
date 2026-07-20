from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        ([0]),
        ([5, 0]),
        ([5, 3, 0]),
        ([10, -4, 2, 0]),
    ]
)
def test_function(pytestconfig, inputs):
    expected_output = ""
    total = 0
    for number in inputs:
        expected_output += f"Enter a number (0 to stop): > {number}\n"
        if number != 0:
            total = total + number
    expected_output += f"Total: {total}\n"
    run_script(__file__, inputs, expected_output)
