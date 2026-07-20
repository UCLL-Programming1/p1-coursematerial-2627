from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (["yes"],True),
        (["yes please"],True),
        (["oh yes definitely"],True),
        (["please, yes!"],True),
        (["no"],False),
        (["nope"],False),
        (["maybe"],False),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"Do you want to continue? > {inputs[0]}\n"
    if expected:
        expected_output += "Then let's continue!\n"
    else:
        expected_output += "It ends here.\n"
    run_script(__file__, inputs, expected_output)
