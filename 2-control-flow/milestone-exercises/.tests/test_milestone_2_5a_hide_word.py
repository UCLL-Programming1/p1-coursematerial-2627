from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        (["banana", "an"]),
        (["python", "ph"]),
        (["hello", "el"]),
        (["mississippi", "is"]),
        (["secret", ""]),
        (["secret", "secret"]),
    ]
)
def test_function(pytestconfig, inputs):
    word = inputs[0]
    shown_letters = inputs[1]

    hidden_word = ""
    index = 0
    while index < len(word):
        if word[index] in shown_letters:
            hidden_word += word[index]
        else:
            hidden_word += "*"
        index += 1

    expected_output = f"Enter a word to hide: > {word}\n"
    expected_output += f"Enter the letters of the word that need to be shown: > {shown_letters}\n"
    expected_output += f"The hidden word is: {hidden_word}\n"

    run_script(__file__, inputs, expected_output)
