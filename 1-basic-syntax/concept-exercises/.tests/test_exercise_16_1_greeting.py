from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs",
    [
        "Mary",
        "John",
        "Lisa"
    ]
)
def test_function(pytestconfig, inputs):
    expected_output = f"Welcome to the greeting program!\nWhat is your name? > {inputs}\nHello {inputs}!\n"
    run_script(__file__, [inputs], expected_output)

