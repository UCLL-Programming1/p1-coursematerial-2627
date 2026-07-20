from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        ([34, 34]),  # guessed correctly
        ([34, 35]),  # too high, boundary
        ([34, 33]),  # too low, boundary
        ([34, 60]),  # too high
        ([34, 10]),  # too low
        ([0, 0]),    # guessed correctly
    ]
)
def test_function(pytestconfig, inputs):
    number, guess = inputs
    expected_output = f"Game master, enter a number: > {number}\n"
    expected_output += f"Player, guess the number: > {guess}\n"
    if guess == number:
        expected_output += "You guessed correctly!\n"
    else:
        if guess > number:
            expected_output += "Your guess is too high!\n"
        else:
            expected_output += "Your guess is too low!\n"
        expected_output += "Try again!\n"
    run_script(__file__, inputs, expected_output)
