from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([13, 2], 0),
        ([3, 3], 2),
        ([2, 5], 1),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"Let's see who has the highest card!\nPlayer 1, enter your card: > {inputs[0]}\nPlayer 2, enter your card: > {inputs[1]}\n"
    if expected == 0:
        expected_output += "Player 1 has the highest card!\n"
    elif expected == 2:
        expected_output += "Both players are holding the same value card!\n"
    else:
        expected_output += "Player 2 has the highest card!\n"
    run_script(__file__, inputs, expected_output)

