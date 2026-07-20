
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (["hello", "world", "Q"],"['hello', 'world']"),
        (["Q"], "[]"),
        (["A", "Q"], "['A']"),
        (["Queen", "King", "Knight", "Pawn", "Fish", "Television", "Toast", "Q"], "['Queen', 'King', 'Knight', 'Pawn', 'Fish', 'Television', 'Toast']"),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = ""
    for i in range(0,len(inputs)):
        expected_output += f"Give me a word to put in the list, or (Q) quit adding: > {inputs[i]}\n"

    expected_output += f"Your list of words is: {expected}\n"
    run_script(__file__, inputs, expected_output)
