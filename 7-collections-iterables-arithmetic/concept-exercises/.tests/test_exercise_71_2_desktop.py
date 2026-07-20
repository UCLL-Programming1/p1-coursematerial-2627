
from p1_util.tests.test_util import run_script

import pytest


@pytest.mark.parametrize(
    "inputs,expected_price",
    [
        (
            [
                "Intel Core i7 13700K",
                "Gigabyte Z790 AORUS ELITE AX",
                "Q",
            ],
            700,
        ),
        (
            [
                "Intel Core i5 13600K",
                "Corsair DDR5 Vengeance 2x16GB 5600",
                "Q",
            ],
            426,
        ),
        (
            [
                "MSI GeForce RTX 4070 VENTUS 3X 12G OC GPU",
                "Gigabyte GeForce RTX 4090 GAMING OC 24G GPU",
                "Q",
            ],
            2508,
        ),
        # no components at all
        (
            ["Q"],
            0,
        ),
        # the same component twice
        (
            [
                "Corsair DDR5 Vengeance 2x16GB 5600",
                "Corsair DDR5 Vengeance 2x16GB 5600",
                "Q",
            ],
            190,
        ),
        # a single component
        (
            ["Intel Core i7 13700K", "Q"],
            439,
        ),
    ]
)
def test_function(pytestconfig, inputs, expected_price):
    expected_output = ""

    for entry in inputs:
        expected_output += f"Provide a component to look up the price for or (Q) quit: > {entry}\n"

    expected_output += f"The price of the components is: {expected_price}\n"

    run_script(__file__, inputs, expected_output)
