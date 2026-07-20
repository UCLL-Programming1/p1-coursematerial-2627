from p1_util.tests.test_util import call_function

import pytest

@pytest.mark.parametrize(
    "word,guessed_letters,expected",
    [
        ("hangman", "ag", "*a*g*a*"),
        ("hangman", "", "*******"),
        ("hangman", "hangm", "hangman"),
        ("apple", "p", "*pp**"),
        ("banana", "an", "*anana"),
        ("hi", "hi", "hi"),
        ("hi", "", "**"),
    ]
)
def test_function(pytestconfig, word, guessed_letters, expected):
    result = call_function(__file__, "hide_word", [word, guessed_letters])
    assert result == expected, f'hide_word("{word}", "{guessed_letters}") is expected to return "{expected}"", returned "{result}" instead.'
