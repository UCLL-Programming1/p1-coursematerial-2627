from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "card_1,card_2,expected",
    [
        ("5", "5", 0),
        ("Jack", "Jack", 0),
        ("10", "9", 1),
        ("9", "10", 2),
        ("Jack", "10", 1),
        ("10", "Jack", 2),
        ("Queen", "King", 2),
        ("King", "Queen", 1),
        ("King", "2", 1),
        ("2", "3", 2),
    ]
)
def test_function(pytestconfig, card_1, card_2, expected):
    result = call_function(__file__, "highest_card", [card_1, card_2])
    assert result == expected, f"highest_card({card_1}, {card_2}) - Expected: {expected}, Returned: {result}"

@pytest.mark.parametrize(
    "card_1,card_2,message",
    [
        ("5", "5", "Both players are holding the same value card!"),
        ("Jack", "10", "Player 1 has the highest card!"),
        ("Queen", "King", "Player 2 has the highest card!"),
    ]
)
def test_function_script(pytestconfig, card_1, card_2, message):
    expected_output = "Let's see who has the highest card!\n"
    expected_output += f"Player 1, enter your card: > {card_1}\n"
    expected_output += f"Player 2, enter your card: > {card_2}\n"
    expected_output += message + "\n"
    run_script(__file__, [card_1, card_2], expected_output)
