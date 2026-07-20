
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([],[])
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = "{'chocolate': '250g', 'eggs': '5', 'sugar': '125g', 'flour': '75g', 'butter': '175g'}\n"
    run_script(__file__, inputs, expected_output)