from p1_util.tests.test_util import run_script

import pytest

P1_PROMPT = "Player 1, enter your choice (rock/paper/scissors): > "
P2_PROMPT = "Player 2, enter your choice (rock/paper/scissors): > "


def round_result(choice_1, choice_2):
    if choice_1 == choice_2:
        return "tie"
    if (choice_1 == "rock" and choice_2 == "scissors") or \
       (choice_1 == "scissors" and choice_2 == "paper") or \
       (choice_1 == "paper" and choice_2 == "rock"):
        return "p1"
    return "p2"


@pytest.mark.parametrize(
    "inputs",
    [
        (["rock", "rock"]),
        (["paper", "paper"]),
        (["scissors", "scissors"]),
        (["rock", "scissors"]),
        (["scissors", "paper"]),
        (["paper", "rock"]),
        (["rock", "paper"]),
        (["paper", "scissors"]),
        (["scissors", "rock"]),
        (["Rock", "SCISSORS"]),
    ]
)
def test_function(pytestconfig, inputs):
    choice_1 = inputs[0].lower()
    choice_2 = inputs[1].lower()

    expected_output = "Welcome to Rock Paper Scissors!\n"
    expected_output += P1_PROMPT + inputs[0] + "\n"
    expected_output += P2_PROMPT + inputs[1] + "\n"

    result = round_result(choice_1, choice_2)
    if result == "tie":
        expected_output += "It's a tie!\n"
    elif result == "p1":
        expected_output += "Player 1 wins this round!\n"
    else:
        expected_output += "Player 2 wins this round!\n"

    expected_output += "Thanks for playing!\n"
    run_script(__file__, inputs, expected_output)
