from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["King", "2"], 0),
        (["3", "3"], 2),
        (["Jack", "Queen"], 1),
        (["Jack", "10"], 0),
        (["10", "King"], 1),
        (["9", "10"], 1),
        (["10", "9"], 0),
        (["Queen", "Queen"], 2),
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

