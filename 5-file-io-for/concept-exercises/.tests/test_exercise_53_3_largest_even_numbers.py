from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (
            ["10", "18"],
            "[18, 16, 14, 12, 10]"
        ),
        (
            ["0", "10"],
            "[10, 8, 6, 4, 2, 0]"
        ),
        (
            ["3", "8"],
            "[8, 6, 4]"
        ),
        (
            ["8", "8"],
            "[8]"
        ),
        (
            ["7", "8"],
            "[8]"
        ),
        (
            ["0", "0"],
            "[0]"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = (
        f"What is the starting number of your sequence: > {inputs[0]}\n"
        f"What is the ending number of your sequence: > {inputs[1]}\n"
        f"The even numbers in this sequence from largest to smallest are: {expected}\n"
    )

    run_script(__file__, inputs, expected_output)


@pytest.mark.parametrize(
    "sorted_list,expected",
    [
        ([10, 11, 12, 13, 14, 15, 16, 17, 18], [18, 16, 14, 12, 10]),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 8, 6, 4, 2, 0]),
        ([1, 2, 3, 4], [4, 2]),
        ([4], [4]),
        ([3, 4], [4]),
    ]
)
def test_function_get_largest_even_numbers(pytestconfig, sorted_list, expected):
    result = call_function(__file__, "get_largest_even_numbers", [list(sorted_list)])
    assert result == expected, (
        f"get_largest_even_numbers({sorted_list}) should return {expected}, but returned {result!r}"
    )
