from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (["Monday"],True),
        (["Wednesday"],True),
        (["Friday"],True),
        (["Saturday"],False),
        (["Sunday"],False),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"What day is it today? > {inputs[0]}\n"
    if expected:
        expected_output += "The office is open today.\n"
    else:
        expected_output += "The office is closed today.\n"
    run_script(__file__, inputs, expected_output)
