
from p1_util.tests.test_util import run_script

import pytest


@pytest.mark.parametrize(
    "inputs,stock_outputs",
    [
        (
            [
                "New Balance 530",
                "Air Jordan 1 Retro",
                "Q"
            ],
            [
                "{'New Balance 530': 4, 'Converse Chuck Taylor All Star 70 Hi': 2, 'Air Jordan 1 Retro': 8, 'Nike Air Max Tuned 1': 1, 'Adidas Superstar': 4, 'Vans Classic Slip-on Checkered': 15}",
                "{'New Balance 530': 4, 'Converse Chuck Taylor All Star 70 Hi': 2, 'Air Jordan 1 Retro': 7, 'Nike Air Max Tuned 1': 1, 'Adidas Superstar': 4, 'Vans Classic Slip-on Checkered': 15}",
            ]
        ),
        (
            [
                "Nike Air Max Tuned 1",
                "Q"
            ],
            [
                "{'New Balance 530': 5, 'Converse Chuck Taylor All Star 70 Hi': 2, 'Air Jordan 1 Retro': 8, 'Adidas Superstar': 4, 'Vans Classic Slip-on Checkered': 15}",
            ]
        ),
        # selling the same model until it is sold out
        (
            [
                "Converse Chuck Taylor All Star 70 Hi",
                "Converse Chuck Taylor All Star 70 Hi",
                "Q"
            ],
            [
                "{'New Balance 530': 5, 'Converse Chuck Taylor All Star 70 Hi': 1, 'Air Jordan 1 Retro': 8, 'Nike Air Max Tuned 1': 1, 'Adidas Superstar': 4, 'Vans Classic Slip-on Checkered': 15}",
                "{'New Balance 530': 5, 'Air Jordan 1 Retro': 8, 'Nike Air Max Tuned 1': 1, 'Adidas Superstar': 4, 'Vans Classic Slip-on Checkered': 15}",
            ]
        ),
        # selling the first and the last model of the stock
        (
            [
                "Vans Classic Slip-on Checkered",
                "New Balance 530",
                "Q"
            ],
            [
                "{'New Balance 530': 5, 'Converse Chuck Taylor All Star 70 Hi': 2, 'Air Jordan 1 Retro': 8, 'Nike Air Max Tuned 1': 1, 'Adidas Superstar': 4, 'Vans Classic Slip-on Checkered': 14}",
                "{'New Balance 530': 4, 'Converse Chuck Taylor All Star 70 Hi': 2, 'Air Jordan 1 Retro': 8, 'Nike Air Max Tuned 1': 1, 'Adidas Superstar': 4, 'Vans Classic Slip-on Checkered': 14}",
            ]
        ),
        # quitting right away
        (
            ["Q"],
            []
        ),
    ]
)
def test_function(pytestconfig, inputs, stock_outputs):
    expected_output = ""

    stock_index = 0

    for command in inputs:
        expected_output += f"Which model do you want to sell, or (Q) quit? > {command}\n"

        if command != "Q":
            expected_output += f"The stock is: {stock_outputs[stock_index]}\n"
            stock_index += 1

    run_script(__file__, inputs, expected_output)
