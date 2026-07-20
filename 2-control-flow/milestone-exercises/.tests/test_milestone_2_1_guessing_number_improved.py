from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        ([42, 42]),
        ([42, 30, 42]),
        ([42, 60, 42]),
        ([42, 30, 60, 42]),
        ([42, 60, 30, 42]),
        ([1, 100, 50, 25, 1]),
    ]
)
def test_function(pytestconfig, inputs):
    number = inputs[0]
    guesses = inputs[1:]
    expected_output = f"Game master, enter a number: > {number}\n"
    for guess in guesses:
        expected_output += f"Player, guess the number: > {guess}\n"
        if guess == number:
            break
        if guess > number:
            expected_output += "Your guess is too high!\n"
        else:
            expected_output += "Your guess is too low!\n"
        expected_output += "Try again!\n"
    expected_output += "You guessed correctly!\n"
    run_script(__file__, inputs, expected_output)
