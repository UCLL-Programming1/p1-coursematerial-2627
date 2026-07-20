from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (["abc"],False),
        (["1234567"],False),
        (["12345678"],True),
        (["supersecret"],True),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"Choose a password: > {inputs[0]}\n"
    if expected:
        expected_output += "Password accepted.\n"
    else:
        expected_output += "Password is too short.\n"
    run_script(__file__, inputs, expected_output)
