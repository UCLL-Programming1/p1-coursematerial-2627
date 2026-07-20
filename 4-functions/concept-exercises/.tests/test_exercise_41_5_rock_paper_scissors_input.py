from p1_util.tests.test_util import call_function, run_script

import pytest

PROMPT = "Player 1, enter your choice (rock/paper/scissors) or (Q)uit: > "
CASES = [
    ("Rock", "rock"),
    ("PAPER", "paper"),
    ("Scissors", "scissors"),
    ("Q", "q"),
]

@pytest.mark.parametrize("typed,choice", CASES)
def test_function(pytestconfig, typed, choice):
    result = call_function(__file__, "ask_input", [1], inputs=[typed],
                                      expected_output=PROMPT + typed + "\n")
    assert result == choice, f"ask_input() was expected to return {choice}, returned {result} instead."

@pytest.mark.parametrize("typed,choice", CASES)
def test_function_script(pytestconfig, typed, choice):
    expected_output = PROMPT + typed + "\n" + f"Player 1 chose: {choice}\n"
    run_script(__file__, [typed], expected_output)
