from p1_util.tests.test_util import run_script, call_function

import pytest

@pytest.mark.parametrize(
    "number,guesses",
    [
        (5, [5]),
        (5, [3, 7, 5]),
        (10, [1, 20, 10]),
        (7, [8, 6, 7]),
    ]
)
def test_function_script(pytestconfig, number, guesses):
    expected_output = compute_expected_output(number, guesses)
    run_script(__file__, [number] + guesses, expected_output)


@pytest.mark.parametrize(
    "number,guesses",
    [
        (5, [5]),
        (5, [3, 7, 5]),
        (10, [1, 20, 10]),
        (7, [8, 6, 7]),
    ]
)
def test_function(pytestconfig, number, guesses):
    expected_output = compute_expected_output(number, guesses)
    result = call_function(__file__, "main", [], inputs=[number]+guesses, expected_output=expected_output)
    assert result is None, f"The function main() is not supposed to return any value, your function returned {result}"

def compute_expected_output(number, guesses):
    expected_output = f"Game master, enter a number: > {number}\n"
    index = 0
    guess = guesses[index]
    expected_output += f"Player, guess the number: > {guess}\n"
    while guess != number:
        if guess > number:
            expected_output += "Your guess is too high!\n"
        else:
            expected_output += "Your guess is too low!\n"
        expected_output += "Try again!\n"
        index += 1
        guess = guesses[index]
        expected_output += f"Player, guess the number: > {guess}\n"
    expected_output += "You guessed correctly!\n"
    return expected_output
