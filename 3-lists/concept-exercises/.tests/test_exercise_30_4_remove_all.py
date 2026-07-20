
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (
            ["a", "b", "2", "fish", "c", "a", "word", "4", "Q", "a"],
            "['b', '2', 'fish', 'c', 'word', '4']"
        ),
        (
            ["1", "2", "3", "2", "4", "Q", "2"],
            "['1', '3', '4']"
        ),
        (
            ["apple", "banana", "cherry", "Q", "pear"],
            "['apple', 'banana', 'cherry']"
        ),
        (
            ["x", "x", "x", "Q", "x"],
            "[]"
        ),
        (
            ["Q", "x"],
            "[]"
        ),
        (
            ["a", "b", "b", "c", "b", "Q", "b"],
            "['a', 'c']"
        ),
        (
            ["a", "b", "c", "a", "Q", "a"],
            "['b', 'c']"
        ),
        (
            ["c", "a", "b", "c", "Q", "c"],
            "['a', 'b']"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected):
    # Build repeated prompt dynamically based on number of inputs before "Q"
    expected_output = ""
    for i in range(len(inputs) - 1):  # all inputs except last removal input
        expected_output += f"Give me an entry to put in the list, or (Q) quit adding: > {inputs[i]}\n"

    expected_output += f"Which entry do you want to remove? > {inputs[-1]}\n"
    expected_output += f"Your final list is: {expected}\n"

    run_script(__file__, inputs, expected_output)
