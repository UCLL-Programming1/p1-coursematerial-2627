from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "word",
    [
        "Python",
        "go",
        "a",
        "Hello",
    ]
)
def test_function(pytestconfig, word):
    expected_output = (
        f"Enter a word: > {word}\n"
        f"First character: {word[0]}\n"
        f"Last character: {word[-1]}\n"
    )
    run_script(__file__, [word], expected_output)
