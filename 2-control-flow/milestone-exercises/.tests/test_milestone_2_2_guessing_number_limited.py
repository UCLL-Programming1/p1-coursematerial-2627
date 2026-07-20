from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        ([42, 2, 42]),
        ([42, 2, 30, 42]),
        ([42, 2, 60, 42]),
        ([42, 2, 30, 60]),
        ([42, 1, 30]),
        ([42, 3, 30, 60, 42]),
        ([42, 3, 30, 60, 50]),
    ]
)
def test_function(pytestconfig, inputs):
    number = inputs[0]
    nb_attempts = inputs[1]
    guesses = inputs[2:]

    expected_output = f"Game master, enter a number: > {number}\n"
    expected_output += f"Game master, how many guesses does the player have: > {nb_attempts}\n"
    expected_output += f"Player, guess the number: > {guesses[0]}\n"

    index = 0
    guess = guesses[index]
    while guess != number and nb_attempts > 0:
        if guess > number:
            expected_output += "Your guess is too high!\n"
        else:
            expected_output += "Your guess is too low!\n"
        nb_attempts -= 1

        if nb_attempts != 0:
            expected_output += "Try again!\n"
            index += 1
            guess = guesses[index]
            expected_output += f"Player, guess the number: > {guess}\n"

    if guess == number:
        expected_output += "You guessed correctly!\n"
    else:
        expected_output += "You guess incorrectly, game over!\n"

    run_script(__file__, inputs, expected_output)
