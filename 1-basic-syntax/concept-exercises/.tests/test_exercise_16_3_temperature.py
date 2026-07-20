from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([32.0],0.0),
        ([70.0],21.11111111111111),
        ([98.6],36.99999999999999),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"What is your temperature in Fahrenheit? > {inputs[0]}\nThe converted temperature in Celcius is {expected}.\n"
    run_script(__file__, inputs, expected_output)
