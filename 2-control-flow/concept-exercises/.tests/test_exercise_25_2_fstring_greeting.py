from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "name",
    [
        "Alice",
        "Bob",
        "Mohammed",
    ]
)
def test_function(pytestconfig, name):
    expected_output = f"What is your name? > {name}\nHello {name}, have a great day!\n"
    run_script(__file__, [name], expected_output)
