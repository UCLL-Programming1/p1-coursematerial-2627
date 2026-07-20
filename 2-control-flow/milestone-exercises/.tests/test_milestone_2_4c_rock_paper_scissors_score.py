from p1_util.tests.test_util import run_script

import pytest

P1_PROMPT = "Player 1, enter your choice (rock/paper/scissors) or (Q)uit: > "
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
        (["q"]),
        (["Q"]),
        (["rock", "scissors", "q"]),
        (["rock", "paper", "q"]),
        (["rock", "rock", "q"]),
        (["rock", "scissors", "paper", "rock", "scissors", "rock", "Q"]),
        (["Rock", "SCISSORS", "q"]),
    ]
)
def test_function(pytestconfig, inputs):
    score_1 = 0
    score_2 = 0

    expected_output = "Welcome to Rock Paper Scissors!\n"

    index = 0
    stop = False
    while not stop:
        expected_output += P1_PROMPT + inputs[index] + "\n"
        choice_1 = inputs[index].lower()
        index += 1
        if choice_1 == "q":
            stop = True
        else:
            expected_output += P2_PROMPT + inputs[index] + "\n"
            choice_2 = inputs[index].lower()
            index += 1

            result = round_result(choice_1, choice_2)
            if result == "tie":
                expected_output += "It's a tie!\n"
            elif result == "p1":
                expected_output += "Player 1 wins this round!\n"
                score_1 += 1
            else:
                expected_output += "Player 2 wins this round!\n"
                score_2 += 1

            expected_output += f"Score - Player 1: {score_1}, Player 2: {score_2}\n"

    expected_output += "Thanks for playing!\n"
    run_script(__file__, inputs, expected_output)
