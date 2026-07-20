from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "day",
    [
        "Monday",
        "Friday",
        "Sunday",
        "Wednesday",
    ]
)
def test_function(pytestconfig, day):
    expected_output = f"Enter a day name: > {day}\nThe abbreviation is {day[:3]}.\n"
    run_script(__file__, [day], expected_output)
