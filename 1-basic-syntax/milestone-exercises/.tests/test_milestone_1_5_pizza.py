from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([2, 4], 2.0),
        ([3, 9], 3.0),
        ([2, 5], 2.5),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"How many people are you? > {inputs[0]}\nAnd how many pizza's do you have for sharing? > {inputs[1]}\nYou will have {expected} pizza's per person!\n"
    run_script(__file__, inputs, expected_output)

