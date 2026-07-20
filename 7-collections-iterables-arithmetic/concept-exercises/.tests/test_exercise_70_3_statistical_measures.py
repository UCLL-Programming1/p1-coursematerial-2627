
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (
            ["25", "30", "31", "30", "28"],
            "(144, 28.8, 25, 31)"
        ),
        (
            ["1", "2", "3", "4", "5"],
            "(15, 3.0, 1, 5)"
        ),
        (
            ["10", "10", "10", "10", "10"],
            "(50, 10.0, 10, 10)"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = ""

    # Prompts (5 times)
    for i in range(5):
        expected_output += f"Provide a number for the tuple: > {inputs[i]}\n"

    expected_output += f"The statistical measures are: {expected}\n"

    run_script(__file__, inputs, expected_output)
