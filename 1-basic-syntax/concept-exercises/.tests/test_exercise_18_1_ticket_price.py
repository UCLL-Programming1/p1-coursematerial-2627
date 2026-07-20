from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([0],0),
        ([5],0),
        ([6],4),
        ([15],4),
        ([17],4),
        ([18],12),
        ([62],12),
        ([64],12),
        ([65],7),
        ([80],7)
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"Welcome to the museum!\nWhat is your age? > {inputs[0]}\n"
    if expected == 0:
        expected_output += "Your ticket is free!\n"
    else:
        expected_output += f"Your ticket costs {expected} EUR.\n"
    run_script(__file__, inputs, expected_output)
