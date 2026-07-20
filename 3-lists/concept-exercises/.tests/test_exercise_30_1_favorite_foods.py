
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (["lasagna", "wraps", "fries", "lobster"],
         ("['lasagna', 'wraps', 'fries']","['lasagna', 'fries', 'lobster']")),
        (["pizza", "pasta", "salad", "burger"],
         ("['pizza', 'pasta', 'salad']","['pizza', 'salad', 'burger']")),
        (["soup", "soup", "rice", "soup"],
         ("['soup', 'soup', 'rice']","['soup', 'rice', 'soup']")),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = (
        f"What is your first favorite food? > {inputs[0]}\n"
        f"What is your second favorite food? > {inputs[1]}\n"
        f"What is your third favorite food? > {inputs[2]}\n"
        f"Your favorite foods are: {expected[0]}\n"
        f"Which food do you want to add? > {inputs[3]}\n"
        f"After adding and removing, your list is: {expected[1]}\n"
    )
    run_script(__file__, inputs, expected_output)
