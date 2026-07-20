
from p1_util.tests.test_util import run_script

import pytest


@pytest.mark.parametrize(
    "inputs,expected_cakes",
    [
        (["0"], 0),
        (["4"], 0),
        (["5"], 1),
        (["14"], 2),
        (["15"], 3),
        (["16"], 3),
        (["27"], 5),
    ]
)
def test_function(pytestconfig, inputs, expected_cakes):
    expected_output = (
        f"How many eggs do you have? > {inputs[0]}\n"
        f"You can bake {expected_cakes} cakes.\n"
    )

    run_script(__file__, inputs, expected_output)
