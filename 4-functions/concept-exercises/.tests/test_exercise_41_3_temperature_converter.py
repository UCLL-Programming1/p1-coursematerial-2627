from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "fahrenheit,expected",
    [
        (32, 0.0),
        (212, 100.0),
        (68, 20.0),
        (50, 10.0),
        (14, -10.0),
        (5, -15.0),
        (95, 35.0),
    ]
)
def test_function(pytestconfig, fahrenheit, expected):
    result = call_function(__file__, "to_celsius", [fahrenheit])
    assert result == expected, f"to_celsius({fahrenheit}) - Expected: {expected}, Result: {result}"

@pytest.mark.parametrize(
    "fahrenheit,celsius",
    [
        (50, 10.0),
        (32, 0.0),
        (212, 100.0),
        (68, 20.0),
    ]
)
def test_function_script(pytestconfig, fahrenheit, celsius):
    expected_output = f"What is your temperature in Fahrenheit? > {fahrenheit}\n"
    expected_output += f"The converted temperature in Celsius is {celsius}.\n"
    run_script(__file__, [fahrenheit], expected_output)
