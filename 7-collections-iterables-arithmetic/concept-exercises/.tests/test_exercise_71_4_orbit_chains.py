
from p1_util.tests.test_util import run_script

import pytest


@pytest.mark.parametrize(
    "inputs,expected_chain",
    [
        (
            ["Earth"],
            "['Earth', 'Sun', 'Sagittarius A*']"
        ),
        (
            ["Moon"],
            "['Moon', 'Earth', 'Sun', 'Sagittarius A*']"
        ),
        (
            ["Phobos"],
            "['Phobos', 'Mars', 'Sun', 'Sagittarius A*']"
        ),
        (
            ["Europa"],
            "['Europa', 'Jupiter', 'Sun', 'Sagittarius A*']"
        ),
        (
            ["Sun"],
            "['Sun', 'Sagittarius A*']"
        ),
        # the end of every chain: it does not orbit anything in the dictionary
        (
            ["Sagittarius A*"],
            "['Sagittarius A*']"
        ),
        (
            ["Ganymede"],
            "['Ganymede', 'Jupiter', 'Sun', 'Sagittarius A*']"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected_chain):
    expected_output = (
        f"Provide a celestial body to construct the orbit chain for: > {inputs[0]}\n"
        f"The orbit chain is: {expected_chain}\n"
    )

    run_script(__file__, inputs, expected_output)
