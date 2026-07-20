from p1_util.tests.test_util import run_script

import pytest

OP_PROMPT = "Provide the symbol of the operation you want to perform or (S)top: > "


@pytest.mark.parametrize(
    "inputs",
    [
        ["S"],
        ["+", 5.0, 2.5, "S"],
        ["-", 7.1, 1.4, "S"],
        ["/", -10.0, 2.5, "S"],
        ["*", 3, 2.3, "S"],
        ["%", 4, 5, "S"],
        ["+", 1, 2, "-", 10, 4, "/", 9.0, 2.0, "S"],
    ],
)
def test_function(pytestconfig, inputs):
    expected_output = "Welcome to our calculator app!\n"
    i = 0
    while True:
        operation = inputs[i]
        i += 1
        expected_output += OP_PROMPT + str(operation) + "\n"
        if operation == "S":
            break
        first_number = float(inputs[i])
        i += 1
        second_number = float(inputs[i])
        i += 1
        expected_output += f"Provide your first number: > {inputs[i-2]}\n"
        expected_output += f"Provide your second number: > {inputs[i-1]}\n"
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "/":
            result = first_number / second_number
        else:
            result = first_number * second_number
        expected_output += "Your resulting value is " + str(result) + ".\n"
    run_script(__file__, inputs, expected_output)
