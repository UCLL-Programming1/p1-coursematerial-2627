
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,first,last,provider",
    [
        (["john.doe@hotmail.com"], "john", "doe", "hotmail"),
        (["alice.smith@gmail.com"], "alice", "smith", "gmail"),
        (["bob.jones@yahoo.com"], "bob", "jones", "yahoo"),
    ]
)
def test_function(pytestconfig, inputs, first, last, provider):
    expected_output = (
        f"Enter an e-mail: > {inputs[0]}\n"
        f"First name: {first}\n"
        f"Last name: {last}\n"
        f"Provider: {provider}\n"
    )

    run_script(__file__, inputs, expected_output)
