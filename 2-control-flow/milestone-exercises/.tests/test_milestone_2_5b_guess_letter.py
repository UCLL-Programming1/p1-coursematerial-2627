from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        (["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]),
        (["a", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]),
        (["a", "bc", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]),
        (["", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]),
    ]
)
def test_function(pytestconfig, inputs):
    guessed_letters = ""
    nb_lives = 11
    expected_output = "Welcome to guessing some letters!\n"

    index = 0
    while nb_lives > 0:
        expected_output += "\n"
        expected_output += f"Already guessed: {guessed_letters}\n"
        expected_output += f"{nb_lives} lives left\n"
        expected_output += "\n"
        expected_output += f"Guess a letter: > {inputs[index]}\n"

        guess = inputs[index]
        index += 1

        if len(guess) != 1:
            expected_output += "Your guess needs to be exactly one character!\n"
        elif guess in guessed_letters:
            expected_output += f"You already guessed {guess}!\n"
        else:
            guessed_letters += guess
            nb_lives -= 1

    run_script(__file__, inputs, expected_output)
