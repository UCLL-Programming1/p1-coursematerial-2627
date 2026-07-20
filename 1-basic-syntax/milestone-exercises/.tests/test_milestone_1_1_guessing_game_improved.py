from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["lion", "giraffe"], False),
        (["lion", "lion"], True),
        (["zebra", "zebra"], True),
        (["zebra", "lion"], False)
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"Player 1, enter an animal that player 2 needs to guess: > {inputs[0]}\nPlayer 2, what animal is player 1 thinking of? > {inputs[1]}\n"
    if expected:
        expected_output += "You guessed correctly!\n"
    else:
        expected_output += "Nope, try again!\n"
    run_script(__file__, inputs, expected_output)

