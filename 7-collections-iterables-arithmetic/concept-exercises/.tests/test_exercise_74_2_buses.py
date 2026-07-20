from p1_util.tests.test_util import run_script

import pytest


@pytest.mark.parametrize(
    "inputs,expected_buses",
    [
        (["25", "10"], 3),
        (["501", "500"], 2),
        (["20", "20"], 1),
        (["21", "20"], 2),
        (["126", "20"], 7),
        (["100", "25"], 4),
        (["1", "50"], 1),
    ]
)
def test_function(pytestconfig, inputs, expected_buses):
    expected_output = (
        f"How many people do you need to transport? > {inputs[0]}\n"
        f"How many people can fit on the bus? > {inputs[1]}\n"
        f"You need {expected_buses} buses.\n"
    )

    run_script(__file__, inputs, expected_output)