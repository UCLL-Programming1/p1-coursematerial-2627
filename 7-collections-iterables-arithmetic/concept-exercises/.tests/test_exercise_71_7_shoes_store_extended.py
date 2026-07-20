
from p1_util.tests.test_util import call_function, run_script

import pytest


@pytest.mark.parametrize(
    "inputs,stock_outputs",
    [
        (
            [
                "New Balance 530,44",
                "Q"
            ],
            [
                "{'New Balance 530': {44: 1, 45: 3, 47: 1}, 'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2}, 'Air Jordan 1 Retro': {46: 1}, 'Nike Air Max Tuned 1': {44: 2, 45: 1}, 'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3}, 'Vans Classic Slip-on Checkered': {43: 1}}"
            ]
        ),
        (
            [
                "Air Jordan 1 Retro,46",
                "Q"
            ],
            [
                "{'New Balance 530': {44: 2, 45: 3, 47: 1}, 'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2}, 'Nike Air Max Tuned 1': {44: 2, 45: 1}, 'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3}, 'Vans Classic Slip-on Checkered': {43: 1}}"
            ]
        ),
        (
            [
                "New Balance 530,43",
                "Q"
            ],
            [
                "{'New Balance 530': {44: 2, 45: 3, 47: 1}, 'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2}, 'Air Jordan 1 Retro': {46: 1}, 'Nike Air Max Tuned 1': {44: 2, 45: 1}, 'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3}, 'Vans Classic Slip-on Checkered': {43: 1}}"
            ]
        ),
        # a model that is not in stock at all leaves the stock untouched
        (
            [
                "Reebok Fury Pump,44",
                "Q"
            ],
            [
                "{'New Balance 530': {44: 2, 45: 3, 47: 1}, 'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2}, 'Air Jordan 1 Retro': {46: 1}, 'Nike Air Max Tuned 1': {44: 2, 45: 1}, 'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3}, 'Vans Classic Slip-on Checkered': {43: 1}}"
            ]
        ),
        # the last pair of one size is sold, but other sizes of the model remain
        (
            [
                "New Balance 530,47",
                "Q"
            ],
            [
                "{'New Balance 530': {44: 2, 45: 3}, 'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2}, 'Air Jordan 1 Retro': {46: 1}, 'Nike Air Max Tuned 1': {44: 2, 45: 1}, 'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3}, 'Vans Classic Slip-on Checkered': {43: 1}}"
            ]
        ),
        # several sales in a row: a size and then the whole model sell out, after which nothing more can be sold
        (
            [
                "Nike Air Max Tuned 1,45",
                "Nike Air Max Tuned 1,44",
                "Nike Air Max Tuned 1,44",
                "Nike Air Max Tuned 1,44",
                "Q"
            ],
            [
                "{'New Balance 530': {44: 2, 45: 3, 47: 1}, 'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2}, 'Air Jordan 1 Retro': {46: 1}, 'Nike Air Max Tuned 1': {44: 2}, 'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3}, 'Vans Classic Slip-on Checkered': {43: 1}}",
                "{'New Balance 530': {44: 2, 45: 3, 47: 1}, 'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2}, 'Air Jordan 1 Retro': {46: 1}, 'Nike Air Max Tuned 1': {44: 1}, 'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3}, 'Vans Classic Slip-on Checkered': {43: 1}}",
                "{'New Balance 530': {44: 2, 45: 3, 47: 1}, 'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2}, 'Air Jordan 1 Retro': {46: 1}, 'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3}, 'Vans Classic Slip-on Checkered': {43: 1}}",
                "{'New Balance 530': {44: 2, 45: 3, 47: 1}, 'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2}, 'Air Jordan 1 Retro': {46: 1}, 'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3}, 'Vans Classic Slip-on Checkered': {43: 1}}",
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
        expected_output += f"Which model do you want to sell at which size, or (Q) quit? > {command}\n"

        if command != "Q":
            expected_output += f"The stock is: {stock_outputs[stock_index]}\n"
            stock_index += 1

    run_script(__file__, inputs, expected_output)



@pytest.mark.parametrize(
    "stock,model,size,expected_result,expected_stock",
    [
        # a regular sale
        ({"A": {40: 2, 41: 1}}, "A", 40, True, {"A": {40: 1, 41: 1}}),
        # the last pair of a size: the size disappears
        ({"A": {40: 2, 41: 1}}, "A", 41, True, {"A": {40: 2}}),
        # the last pair of the model: the model disappears
        ({"A": {40: 1}, "B": {42: 1}}, "A", 40, True, {"B": {42: 1}}),
        # the size is not available
        ({"A": {40: 2}}, "A", 43, False, {"A": {40: 2}}),
        # the model is not available
        ({"A": {40: 2}}, "B", 40, False, {"A": {40: 2}}),
        # nothing in stock at all
        ({}, "A", 40, False, {}),
    ]
)
def test_function_sell(pytestconfig, stock, model, size, expected_result, expected_stock):
    stock = {name: dict(sizes) for name, sizes in stock.items()}
    result = call_function(__file__, "sell", [stock, model, size])
    assert result is expected_result, (
        f"sell(stock, {model!r}, {size}) should return {expected_result}, but returned {result!r}"
    )
    assert stock == expected_stock, (
        f"After sell(stock, {model!r}, {size}) the stock should be {expected_stock}, but it is {stock}"
    )
