
from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "inputs,character,expected_count",
    [
        (
            [
                "I like python",
                "perhaps it will rain tomorrow",
                "have you watched the new popeye film?",
                "Q",
                "p"
            ],
            "p",
            5
        ),
        (
            [
                "hello world",
                "testing code",
                "Q",
                "o"
            ],
            "o",
            3
        ),
        (
            [
                "aaa",
                "bbb",
                "ccc",
                "Q",
                "a"
            ],
            "a",
            3
        ),
        # the character does not occur at all
        (
            ["hello world", "Q", "z"],
            "z",
            0
        ),
        # no sentences at all
        (
            ["Q", "a"],
            "a",
            0
        ),
        # counting is case-sensitive: only lowercase "p" counts
        (
            ["Python and pandas", "PIP", "Q", "p"],
            "p",
            1
        ),
        # the character occurs at the first and last position of a sentence
        (
            ["xox", "x", "Q", "x"],
            "x",
            3
        ),
    ]
)
def test_function(pytestconfig, inputs, character, expected_count):
    expected_output = ""

    # Prompts for sentence input
    for i in range(len(inputs) - 1):  # minus the character input
        expected_output += f"Enter a sentence or (Q) quit: > {inputs[i]}\n"

    # Character input prompt
    expected_output += f"Enter a character to count: > {inputs[-1]}\n"

    # Final output
    expected_output += f"The character {character} has {expected_count} occurrences.\n"

    run_script(__file__, inputs, expected_output)


@pytest.mark.parametrize(
    "sentence_list,character,expected",
    [
        (["I like python", "perhaps it will rain tomorrow", "have you watched the new popeye film?"], "p", 5),
        (["aaa", "bbb"], "b", 3),
        (["abc"], "z", 0),
        ([], "a", 0),
        (["", ""], "a", 0),
        (["Aa"], "a", 1),
    ]
)
def test_function_count_characters(pytestconfig, sentence_list, character, expected):
    result = call_function(__file__, "count_characters", [list(sentence_list), character])
    assert result == expected, (
        f"count_characters({sentence_list!r}, {character!r}) should return {expected}, but returned {result!r}"
    )
