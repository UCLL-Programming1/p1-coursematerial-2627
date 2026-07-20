from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["+", 2.5, 3], 5.5),
        (["*", 3, 2.3], 6.8999999999999995),
        (["/", -10.0, 2.5], -4.0),
        (["-", 7.1, 1.4], 5.699999999999999)
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"Provide the symbol of the operation you want to perform: > {inputs[0]}\nProvide your first number: > {inputs[1]}\nProvide your second number: > {inputs[2]}\nYour resulting value is {expected}.\n"
    run_script(__file__, inputs, expected_output)

