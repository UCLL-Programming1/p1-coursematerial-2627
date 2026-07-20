from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "total,nb",
    [
        (10, 3),
        (9, 4),
        (7, 2),
        (1, 3),
        (5, 3),
        (2, 3),
        (10, 5),
        (4.5, 2),
    ]
)
def test_function(pytestconfig, total, nb):
    expected_output = (
        "Let's calculate the price per item!\n"
        f"How much did you pay in total? > {total}\n"
        f"How many items did that get you? > {nb}\n"
        f"The price per item is €{total/nb:.2f}.\n"
    )
    run_script(__file__, [total, nb], expected_output)
