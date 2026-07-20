from p1_util.tests.test_util import run_script

import pytest

MENU = "Do you want to change (C) your todo-item, show (S) your current item or Exit (E) the application? > "

@pytest.mark.parametrize(
    "inputs",
    [
        (["E"]),
        (["S", "E"]),
        (["C", "finish the report", "S", "E"]),
        (["S", "C", "finish the report", "S", "E"]),
        (["C", "buy milk", "C", "walk the dog", "S", "E"]),
    ]
)
def test_function(pytestconfig, inputs):
    todo_focus = "nothing in particular"
    expected_output = "Welcome to your todo app!\n"

    index = 0
    choice = ""
    while choice != "E":
        expected_output += MENU + inputs[index] + "\n"
        choice = inputs[index]
        index += 1
        if choice == "C":
            expected_output += f"Type your todo: > {inputs[index]}\n"
            todo_focus = inputs[index]
            index += 1
        if choice == "S":
            expected_output += "Your most important todo is: " + todo_focus + "\n"

    run_script(__file__, inputs, expected_output)
