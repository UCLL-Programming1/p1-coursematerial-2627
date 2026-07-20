
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected_lists",
    [
        (
            [
                "A", "cook dinner",
                "A", "clean kitchen",
                "A", "sweep floor",
                "S",
                "R", "cook dinner",
                "S",
                "E"
            ],
            [
                "['cook dinner', 'clean kitchen', 'sweep floor']",
                "['clean kitchen', 'sweep floor']"
            ]
        ),
        (
            [
                "A", "task1",
                "A", "task2",
                "S",
                "R", "nonexistent",
                "S",
                "E"
            ],
            [
                "['task1', 'task2']",
                "['task1', 'task2']"
            ]
        ),
        (
            ["E"],
            []
        ),
        (
            [
                "S",
                "R", "task1",
                "S",
                "A", "task1",
                "S",
                "R", "task1",
                "S",
                "E"
            ],
            ["[]", "[]", "['task1']", "[]"]
        ),
        (
            [
                "A", "first",
                "A", "middle",
                "A", "last",
                "R", "last",
                "S",
                "R", "first",
                "S",
                "E"
            ],
            ["['first', 'middle']", "['middle']"]
        ),
    ]
)
def test_function(pytestconfig, inputs, expected_lists):
    expected_output = "Welcome to your todo app!\n"

    # First interaction (repeat prompts dynamically)
    idx = 0
    list_print_index = 0

    while idx < len(inputs):
        expected_output += "Do you want to (A) add a new todo, remove (R) a todo, show (S) all your current todos or exit (E) the application? > " + inputs[idx] + "\n"

        command = inputs[idx]
        idx += 1

        if command == "A":
            expected_output += f"Type your todo: > {inputs[idx]}\n"

            idx += 1  # skip todo input

        elif command == "S":
            expected_output += f"Your todos are: {expected_lists[list_print_index]}\n"
            list_print_index += 1

        elif command == "R":
            expected_output += f"What todo do you want to remove? > {inputs[idx]}\n"
            idx += 1  # skip remove input

        elif command == "E":
            break

    run_script(__file__, inputs, expected_output)
