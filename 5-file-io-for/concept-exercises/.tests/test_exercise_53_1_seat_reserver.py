
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected_lines",
    [
        (
            ["5", "3"],
            [
                "You have reserved seat 5",
                "You have reserved seat 6",
                "You have reserved seat 7",
            ]
        ),
        (
            ["1", "2"],
            [
                "You have reserved seat 1",
                "You have reserved seat 2",
            ]
        ),
        (
            ["10", "1"],
            [
                "You have reserved seat 10",
            ]
        ),
    ]
)
def test_function(pytestconfig, inputs, expected_lines):
    expected_output = (
        f"Enter a starting seat number: > {inputs[0]}\n"
        f"Enter the amount of persons: > {inputs[1]}\n"
    )

    for line in expected_lines:
        expected_output += f"{line}\n"

    run_script(__file__, inputs, expected_output)
