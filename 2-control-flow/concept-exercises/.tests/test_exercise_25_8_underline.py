from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "title",
    [
        "Chapter One",
        "Hi",
        "Strings",
    ]
)
def test_function(pytestconfig, title):
    expected_output = (
        f"Enter the title to underline: > {title}\n"
        f"{title}\n"
        f"{'-' * len(title)}\n"
    )
    run_script(__file__, [title], expected_output)
