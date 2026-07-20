from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        ([34, 34]),          # correct on the first attempt
        ([34, 10, 34]),      # too low, then correct
        ([34, 35, 34]),      # too high (boundary), then correct
        ([34, 10, 20]),      # too low twice: lose
        ([34, 60, 10]),      # too high, too low: lose
        ([34, 33, 35]),      # boundaries on both sides: lose
    ]
)
def test_function(pytestconfig, inputs):
    number = inputs[0]
    guesses = inputs[1:]
    expected_output = f"Game master, enter a number: > {number}\n"
    for attempt, guess in enumerate(guesses):
        expected_output += f"Player, guess the number: > {guess}\n"
        if guess == number:
            expected_output += "You guessed correctly!\n"
            break
        if guess > number:
            expected_output += "Your guess is too high!\n"
        else:
            expected_output += "Your guess is too low!\n"
        if attempt == 0:
            expected_output += "Try again! (You have 1 guess left)\n"
        else:
            expected_output += "You lose!\n"
    run_script(__file__, inputs, expected_output)
