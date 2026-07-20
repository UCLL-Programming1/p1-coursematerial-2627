
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,first,last",
    [
        (["Python is fun"], "Python", "fun"),
        (["Hello world"], "Hello", "world"),
        (["One two three four"], "One", "four"),
        (["Python is really fun"], "Python", "fun"),
        (["Hello"], "Hello", "Hello"),
    ]
)
def test_function(pytestconfig, inputs, first, last):
    expected_output = (
        f"Enter a sentence: > {inputs[0]}\n"
        f"First word: {first}\n"
        f"Last word: {last}\n"
    )

    run_script(__file__, inputs, expected_output)
