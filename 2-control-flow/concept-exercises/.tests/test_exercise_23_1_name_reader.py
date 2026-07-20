from p1_util.tests.test_util import run_script

import pytest

MENU = "What would you like to do? (R)ead my name, (Q)uit: > "

READINGS = {
    "A": "Names starting with A belong to natural leaders. People follow you without knowing why.",
    "B": "Names starting with B belong to deeply loyal people. You never forget a friend.",
    "C": "Names starting with C belong to the curious. You open every door just to see what is behind it.",
    "D": "Names starting with D belong to dreamers. Your best ideas arrive right before you fall asleep.",
    "E": "Names starting with E belong to the restless. Sitting still was never really your thing.",
    "F": "Names starting with F belong to the fiercely honest. People always know where they stand with you.",
}
UNKNOWN_LETTER = "I do not have a reading for that letter yet. Your name keeps its secrets."


@pytest.mark.parametrize(
    "inputs",
    [
        ["Q"],
        ["R", "Alice", "Q"],
        ["R", "Felix", "Q"],
        ["R", "Boris", "R", "Eve", "Q"],
        ["R", "Zane", "Q"],
        ["X", "Q"],
        ["R", "Diana", "X", "R", "Cara", "Q"],
    ],
)
def test_function(pytestconfig, inputs):
    expected_output = "Welcome to the Name Reader!\n\n"
    i = 0
    while True:
        choice = inputs[i]
        i += 1
        expected_output += MENU + choice + "\n"
        if choice == "Q":
            break
        if choice == "R":
            name = inputs[i]
            i += 1
            expected_output += f"Enter your name: > {name}\n"
            first_letter = name[0]
            if first_letter in READINGS:
                expected_output += READINGS[first_letter] + "\n"
            else:
                expected_output += UNKNOWN_LETTER + "\n"
        else:
            expected_output += "Unknown option. Please enter R or Q.\n"
        expected_output += "\n"
    expected_output += "The name reading is complete. Go forth.\n"
    run_script(__file__, inputs, expected_output)
