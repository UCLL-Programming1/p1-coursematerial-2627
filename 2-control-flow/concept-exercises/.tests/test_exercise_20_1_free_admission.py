from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([8],True),
        ([11],True),
        ([12],False),
        ([40],False),
        ([65],False),
        ([66],True),
        ([70],True),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = f"How old are you? > {inputs[0]}\n"
    if expected:
        expected_output += "Free entrance!\n"
    else:
        expected_output += "The entrance fee is 8 EUR.\n"
    run_script(__file__, inputs, expected_output)
