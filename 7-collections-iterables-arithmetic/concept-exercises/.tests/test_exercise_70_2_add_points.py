
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (
            ["5", "3", "1", "4"],
            "(6, 7)"
        ),
        (
            ["0", "0", "2", "2"],
            "(2, 2)"
        ),
        (
            ["-1", "4", "3", "-2"],
            "(2, 2)"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = (
        f"Provide the first coordinate of the first point: > {inputs[0]}\n"
        f"Provide the second coordinate of the first point: > {inputs[1]}\n"
        f"Provide the first coordinate of the second point: > {inputs[2]}\n"
        f"Provide the second coordinate of the second point: > {inputs[3]}\n"
        f"The resulting point is {expected}\n"
    )

    run_script(__file__, inputs, expected_output)