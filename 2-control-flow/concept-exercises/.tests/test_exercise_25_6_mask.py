from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "password",
    [
        "hunter2",
        "abc",
        "x",
        "correcthorse",
    ]
)
def test_function(pytestconfig, password):
    expected_output = f"Enter the password to mask: > {password}\nMasked password: {'*' * len(password)}\n"
    run_script(__file__, [password], expected_output)
