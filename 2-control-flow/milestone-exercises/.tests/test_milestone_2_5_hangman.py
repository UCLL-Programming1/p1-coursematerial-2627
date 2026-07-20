from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        (["hi", "h", "i"]),
        (["go", "x", "g", "o"]),
        (["hi", "ab", "h", "h", "i"]),
        (["moon", "m", "o", "n"]),
        (["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]),
        (["cat", "a", "x", "c", "t"]),
        # an empty guess is not exactly one character either
        (["hi", "", "h", "i"]),
        # guessing the same wrong letter twice only costs one life
        (["hi", "z", "z", "h", "i"]),
        # winning with only one life left
        (["hi", "a", "b", "c", "d", "e", "f", "g", "j", "k", "l", "h", "i"]),
        # losing while part of the word is already revealed
        (["hello", "h", "e", "a", "b", "c", "d", "f", "g", "i", "j", "k", "m", "n"]),
    ]
)
def test_function(pytestconfig, inputs):
    word = inputs[0]
    guesses = inputs[1:]

    expected_output = "Welcome to hangman!\n"
    expected_output += f"Gamemaster, which word should be guessed: > {word}\n"
    expected_output += "\n"
    expected_output += "Ready to play!\n"

    guessed_letters = ""
    hidden_word = "*" * len(word)
    nb_lives = 11
    game_over = False
    index = 0

    while not game_over:
        expected_output += "\n"
        expected_output += f"Already guessed: {guessed_letters}\n"
        expected_output += f"Word to guess: {hidden_word}\n"
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

            hidden_word = ""
            position = 0
            while position < len(word):
                if word[position] in guessed_letters:
                    hidden_word += word[position]
                else:
                    hidden_word += "*"
                position += 1

            if hidden_word == word:
                expected_output += "You win!\n"
                game_over = True
            elif nb_lives == 0:
                expected_output += "You lose!\n"
                expected_output += f"The correct word was: {word}\n"
                game_over = True

    run_script(__file__, inputs, expected_output)
