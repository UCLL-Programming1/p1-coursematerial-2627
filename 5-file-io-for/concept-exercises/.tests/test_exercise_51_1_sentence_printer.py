
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([],[])
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = 'Jane noticed Jacks\'s car was parked in the wrong spot. "Jack, I saw that you have been ignoring parking regulations lately." She said. "What do you have to say for yourself?"\n'
    run_script(__file__, inputs, expected_output)