from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        ([34, 34]),              # correct on the first attempt
        ([34, 10, 34]),          # too low, then correct
        ([34, 10, 60, 34]),      # too low, too high, then correct
        ([34, 35, 33, 34]),      # boundaries on both sides, then correct
        ([34, 10, 20, 30]),      # too low three times: lose
        ([34, 60, 50, 40]),      # too high three times: lose
        ([34, 33, 35, 36]),      # boundaries: lose
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
        guesses_left = 2 - attempt
        if guesses_left == 2:
            expected_output += "Try again! (You have 2 guesses left)\n"
        elif guesses_left == 1:
            expected_output += "Try again! (You have 1 guess left)\n"
        else:
            expected_output += "You lose!\n"
    run_script(__file__, inputs, expected_output)
