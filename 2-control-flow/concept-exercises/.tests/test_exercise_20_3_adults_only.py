from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([15],False),
        ([17],False),
        ([18],True),
        ([19],True),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"How old are you? > {inputs[0]}\n"
    if expected:
        expected_output += "Welcome!\n"
    else:
        expected_output += "You are not old enough to enter.\n"
    run_script(__file__, inputs, expected_output)
