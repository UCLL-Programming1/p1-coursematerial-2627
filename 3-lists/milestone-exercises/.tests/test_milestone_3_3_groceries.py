
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected_lists",
    [
        (
            [
                "A", "toast, apricots, milk, bread",
                "S",
                "A", "cookies",
                "S",
                "A", "pasta, olive oil",
                "S",
                "R", "apricots, bread, cookies",
                "S",
                "R", "pasta, bananas",
                "S",
                "E"
            ],
            [
                "['toast', 'apricots', 'milk', 'bread']",
                "['toast', 'apricots', 'milk', 'bread', 'cookies']",
                "['toast', 'apricots', 'milk', 'bread', 'cookies', 'pasta', 'olive oil']",
                "['toast', 'milk', 'pasta', 'olive oil']",
                "['toast', 'milk', 'olive oil']",
            ]
        ),
        # items that are already on the list are not added again
        (
            [
                "A", "milk, bread",
                "A", "bread, eggs, milk",
                "S",
                "A", "jam, jam",
                "S",
                "R", "cheese",
                "S",
                "E"
            ],
            [
                "['milk', 'bread', 'eggs']",
                "['milk', 'bread', 'eggs', 'jam']",
                "['milk', 'bread', 'eggs', 'jam']",
            ]
        ),
        # showing and removing on an empty list
        (
            [
                "S",
                "R", "milk",
                "S",
                "E"
            ],
            ["[]", "[]"]
        ),
        (
            ["E"],
            []
        ),
    ]
)
def test_function(pytestconfig, inputs, expected_lists):
    expected_output = "Welcome to your groceries app!\n"

    idx = 0
    list_index = 0

    while idx < len(inputs):
        expected_output += "Do you want to (A) add new groceries, remove (R) groceries, show (S) all your current groceries or exit (E) the application? > " + inputs[idx] + "\n"
        command = inputs[idx]
        idx += 1

        if command == "A":
            expected_output += f"What do you want to add?: > {inputs[idx]}\n"
            idx += 1  # skip groceries input

        elif command == "S":
            expected_output += f"Your groceries list is: {expected_lists[list_index]}\n"
            list_index += 1

        elif command == "R":
            expected_output += f"What do you want to remove?: > {inputs[idx]}\n"
            idx += 1  # skip remove input

        elif command == "E":
            break

    run_script(__file__, inputs, expected_output)
