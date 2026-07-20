
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
    (ns, [2 * n for n in ns][0:-1])
    for ns in [
        ['Q'],
        [0, 'Q'],
        [10, 46, 20, 14, 12, 156, 'Q'],
        [0, 1, 2, 3, 'Q'],
        [9, 4, 5, 8, 7, 6, 2, 1, 'Q'],
    ]
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = ""
    for i in range(0,len(inputs)):
        expected_output += f"Give me a number to put in the list, or (Q) quit adding: > {inputs[i]}\n"

    expected_output += f"After doubling, the list is: {expected}\n"
    run_script(__file__, inputs, expected_output)
