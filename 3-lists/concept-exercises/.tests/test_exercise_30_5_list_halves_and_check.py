
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected_first,expected_second,check_item,expected_result",
    [
        # Example 1
        (
            ["apple", "banana", "cherry", "mango", "Q", "banana"],
            "['apple', 'banana']",
            "['cherry', 'mango']",
            "banana",
            "banana is in the list.\n"
        ),
        # Example 2 (six items, the checked item is the last one)
        (
            ["a", "b", "c", "d", "e", "f", "Q", "f"],
            "['a', 'b', 'c']",
            "['d', 'e', 'f']",
            "f",
            "f is in the list.\n"
        ),
        # Example 3 (item not in list)
        (
            ["bread", "soup", "cheese", "tomato", "Q", "pie"],
            "['bread', 'soup']",
            "['cheese', 'tomato']",
            "pie",
            "pie is not in the list.\n"
        ),
        # Example 4 (two items, the checked item is the first one)
        (
            ["red", "blue", "Q", "red"],
            "['red']",
            "['blue']",
            "red",
            "red is in the list.\n"
        ),
        # Example 5 (empty list)
        (
            ["Q", "yellow"],
            "[]",
            "[]",
            "yellow",
            "yellow is not in the list.\n"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected_first, expected_second, check_item, expected_result):
    # Build initial prompts dynamically
    expected_output = ""
    for i in range(len(inputs) - 1):  # all inputs except the check item
        expected_output += f"Give me an item to add to the list, or (Q) quit adding: > {inputs[i]}\n"

    # Reconstruct full list (excluding Q)
    full_list = []
    for val in inputs:
        if val == "Q":
            break
        full_list.append(val)

    expected_output += f"Your list is: {full_list}\n"
    expected_output += f"First half of the list: {expected_first}\n"
    expected_output += f"Second half of the list: {expected_second}\n"
    expected_output += f"Which item do you want to check? > {inputs[-1]}\n"
    expected_output += expected_result

    run_script(__file__, inputs, expected_output)
