from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (["Paris"],True),
        (["paris"],True),
        (["PARIS"],True),
        (["Berlin"],False),
        (["London"],False),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"What is the capital of France? > {inputs[0]}\n"
    if expected:
        expected_output += "that's correct!\n"
    else:
        expected_output += "Not quite, try again!\n"
    run_script(__file__, inputs, expected_output)
