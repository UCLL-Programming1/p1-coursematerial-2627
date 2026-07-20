from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        (["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]),
        (["cat", "c", "a", "t", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]),
        (["dog", "xy", "d", "d", "a", "b", "c", "e", "f", "h", "i", "j", "k", "l", "m"]),
        (["dog", "", "a", "a", "b", "c", "e", "f", "h", "i", "j", "k", "l", "m"]),
    ]
)
def test_function(pytestconfig, inputs):
    word = inputs[0]
    guesses = inputs[1:]

    expected_output = "Welcome to guessing some letters!\n"
    expected_output += f"Gamemaster, which word should be guessed: > {word}\n"
    expected_output += "\n"
    expected_output += "Ready to play!\n"

    guessed_letters = ""
    nb_lives = 11
    index = 0

    while nb_lives > 0:
        expected_output += "\n"
        expected_output += f"Already guessed: {guessed_letters}\n"
        expected_output += f"{nb_lives} lives left\n"
        expected_output += "\n"
        expected_output += f"Guess a letter: > {guesses[index]}\n"

        guess = guesses[index]
        index += 1

        if len(guess) != 1:
            expected_output += "Your guess needs to be exactly one character!\n"
        elif guess in guessed_letters:
            expected_output += f"You already guessed {guess}!\n"
        else:
            guessed_letters += guess
            if guess in word:
                expected_output += "Good guess!\n"
            else:
                expected_output += "Miss!\n"
                nb_lives -= 1

    run_script(__file__, inputs, expected_output)
