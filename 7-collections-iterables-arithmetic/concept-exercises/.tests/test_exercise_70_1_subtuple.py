
from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (
            ["1", "2", "3", "4", "5", "2", "3", "4"],
            "(2, 3, 4) is a subtuple of (1, 2, 3, 4, 5)\n"
        ),
        (
            ["1", "2", "3", "4", "5", "1", "3", "4"],
            "(1, 3, 4) is not a subtuple of (1, 2, 3, 4, 5)\n"
        ),
        # at the very start
        (
            ["1", "2", "3", "4", "5", "1", "2", "3"],
            "(1, 2, 3) is a subtuple of (1, 2, 3, 4, 5)\n"
        ),
        # at the very end
        (
            ["1", "2", "3", "4", "5", "3", "4", "5"],
            "(3, 4, 5) is a subtuple of (1, 2, 3, 4, 5)\n"
        ),
        # the first part matches, but then the match has to start over
        (
            ["1", "2", "1", "2", "3", "1", "2", "3"],
            "(1, 2, 3) is a subtuple of (1, 2, 1, 2, 3)\n"
        ),
        # the right numbers in the wrong order
        (
            ["1", "2", "3", "4", "5", "3", "2", "1"],
            "(3, 2, 1) is not a subtuple of (1, 2, 3, 4, 5)\n"
        ),
        # only two of the three numbers fit at the end
        (
            ["1", "2", "3", "4", "5", "4", "5", "1"],
            "(4, 5, 1) is not a subtuple of (1, 2, 3, 4, 5)\n"
        ),
        # repeated numbers
        (
            ["7", "7", "7", "7", "7", "7", "7", "7"],
            "(7, 7, 7) is a subtuple of (7, 7, 7, 7, 7)\n"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = ""

    idx = 0

    # First tuple input prompts
    while idx < 5:
        expected_output += f"Provide a number for the first tuple: > {inputs[idx]}\n"
        idx += 1

    idx = 0
    # Second tuple input prompts
    while idx < 3:
        expected_output += f"Provide a number for the second tuple: > {inputs[idx + 5]}\n"
        idx += 1

    expected_output += expected

    run_script(__file__, inputs, expected_output)



@pytest.mark.parametrize(
    "xs,ys,expected",
    [
        ((1, 2, 3, 4, 5), (2, 3, 4), True),
        ((1, 2, 3, 4, 5), (1, 3, 4), False),
        ((1, 2, 3, 4, 5), (1, 2, 3), True),
        ((1, 2, 3, 4, 5), (3, 4, 5), True),
        ((1, 2, 3, 4, 5), (4, 5, 6), False),
        ((1, 2, 1, 2, 3), (1, 2, 3), True),
        ((5, 4, 3, 2, 1), (1, 2, 3), False),
    ]
)
def test_function_is_subtuple(pytestconfig, xs, ys, expected):
    result = call_function(__file__, "is_subtuple", [xs, ys])
    assert result == expected, f"is_subtuple({xs}, {ys}) should return {expected}, but returned {result!r}"
