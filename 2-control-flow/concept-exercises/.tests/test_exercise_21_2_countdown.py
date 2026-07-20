from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "start",
    [
        (0),
        (1),
        (3),
        (10),
    ]
)
def test_function(pytestconfig, start):
    expected_output = f"Count down from: > {start}\n"
    n = start
    while n > 0:
        expected_output += f"{n}\n"
        n = n - 1
    expected_output += "Lift off!\n"
    run_script(__file__, [start], expected_output)
