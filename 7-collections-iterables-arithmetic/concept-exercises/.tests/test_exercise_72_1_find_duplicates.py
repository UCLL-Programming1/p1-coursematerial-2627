
from p1_util.tests.test_util import call_function, run_script

import pytest


# The order of the duplicates doesn't matter, so the program is only checked with
# lists that have at most one duplicate. The function itself is checked separately
# below, where the order of the result is ignored.
@pytest.mark.parametrize(
    "inputs,expected",
    [
        (
            ["1", "2", "Q"],
            "[]"
        ),
        (
            ["1", "2", "1", "Q"],
            "[1]"
        ),
        (
            ["5", "5", "5", "5", "Q"],
            "[5]"
        ),
        (
            ["3", "1", "4", "1", "5", "Q"],
            "[1]"
        ),
        # an empty list
        (
            ["Q"],
            "[]"
        ),
        # a single number
        (
            ["7", "Q"],
            "[]"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = ""

    for entry in inputs:
        expected_output += f"Provide a number for the list or (Q) quit: > {entry}\n"

    expected_output += f"The duplicates are: {expected}\n"

    run_script(__file__, inputs, expected_output)


@pytest.mark.parametrize(
    "xs,expected",
    [
        ([1, 2], []),
        ([1, 2, 1], [1]),
        ([1, 2, 1, 3, 2, 1, 1], [1, 2]),
        ([], []),
        ([4], []),
        ([4, 4], [4]),
        ([9, 8, 7, 7, 8, 9], [7, 8, 9]),
        ([1, 2, 3, 4, 5, 1], [1]),
    ]
)
def test_function_find_duplicates(pytestconfig, xs, expected):
    result = call_function(__file__, "find_duplicates", [list(xs)])
    assert isinstance(result, list), f"find_duplicates should return a list, but it returned {result!r}"
    assert len(result) == len(set(result)), (
        f"find_duplicates({xs}) should mention every duplicate only once, but returned {result}"
    )
    assert sorted(result) == sorted(expected), (
        f"find_duplicates({xs}) should return the duplicates {expected} (in any order), but returned {result}"
    )
