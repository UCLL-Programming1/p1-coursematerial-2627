
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (
            ["5", "1", "23", "78", "12", "7", "Q"],
            "[1, 5, 7, 12, 23, 78]"
        ),
        (
            ["3", "2", "1", "Q"],
            "[1, 2, 3]"
        ),
        (
            ["10", "5", "10", "2", "Q"],
            "[2, 5, 10, 10]"
        ),
        (
            ["1", "2", "3", "4", "Q"],
            "[1, 2, 3, 4]"
        ),
        (
            ["2", "4", "1", "3", "Q"],
            "[1, 2, 3, 4]"
        ),
        (
            ["42", "Q"],
            "[42]"
        ),
        (
            ["Q"],
            "[]"
        ),
        (
            ["3", "-7", "0", "-2", "Q"],
            "[-7, -2, 0, 3]"
        ),
        (
            ["9", "1", "Q"],
            "[1, 9]"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = ""

    # Add repeated prompts
    for i in range(len(inputs)):
        expected_output += f"Give me a number to put in the list, or (Q) quit adding: > {inputs[i]}\n"

    expected_output += f"After sorting, the list is: {expected}\n"

    run_script(__file__, inputs, expected_output)
