from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        (["Paris"]),
        (["London", "Paris"]),
        (["London", "Berlin", "Paris"]),
    ]
)
def test_function(pytestconfig, inputs):
    expected_output = ""
    for answer in inputs:
        expected_output += f"What is the capital of France? > {answer}\n"
        if answer != "Paris":
            expected_output += "That's not right, try again!\n"
    expected_output += "Correct!\n"
    run_script(__file__, inputs, expected_output)
