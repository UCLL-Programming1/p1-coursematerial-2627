
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected_lines",
    [
        (
            ["5"],
            [
                "*",
                "**",
                "***",
                "****",
                "*****",
            ]
        ),
        (
            ["3"],
            [
                "*",
                "**",
                "***",
            ]
        ),
        (
            ["1"],
            [
                "*",
            ]
        ),
    ]
)
def test_function(pytestconfig, inputs, expected_lines):
    expected_output = f"To which level do you want to build your pyramid? > {inputs[0]}\n"

    for line in expected_lines:
        expected_output += f"{line}\n"

    run_script(__file__, inputs, expected_output)
