
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (["I love Python"], "Python love I"),
        (["Today it is very warm"], "warm very is it Today"),
        (["one two three four"], "four three two one"),
        (["Hello"], "Hello"),
        (["Hello world"], "world Hello"),
        (["We should go and get fries for dinner"], "dinner for fries get and go should We"),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = (
        f"Enter a sentence: > {inputs[0]}\n"
        f"Your reversed sentence is: {expected}\n"
    )

    run_script(__file__, inputs, expected_output)
