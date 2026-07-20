
from p1_util.tests.test_util import run_script

import pytest


@pytest.mark.parametrize(
    "inputs,expected_keys",
    [
        (
            [
                "a,1",
                "b,1",
                "c,2",
                "Q",
                "1"
            ],
            "['a', 'b']"
        ),
        (
            [
                "cat,animal",
                "dog,animal",
                "car,vehicle",
                "Q",
                "vehicle"
            ],
            "['car']"
        ),
        (
            [
                "x,10",
                "y,20",
                "z,30",
                "Q",
                "40"
            ],
            "[]"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected_keys):
    expected_output = ""

    idx = 0

    while inputs[idx] != "Q":
        expected_output += f"Provide a key and value for the first dictionary, or (Q) quit: > {inputs[idx]}\n"
        idx += 1

    expected_output += f"Provide a key and value for the first dictionary, or (Q) quit: > {inputs[idx]}\n"
    idx += 1

    expected_output += f"Provide a value to find the corresponding keys for: > {inputs[idx]}\n"
    expected_output += f"The resulting keys are: {expected_keys}\n"

    run_script(__file__, inputs, expected_output)
