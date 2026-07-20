from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "name,price,price_with_vat",
    [
        ("Keyboard", 50.0, 60.5),
        ("Monitor", 200, 242),
        ("Cable", 0.0, 0.0),
        ("USB stick", 10.0, 12.1),
    ]
)
def test_function(pytestconfig, name, price, price_with_vat):
    product = call_function(__file__, "Product", [name, price])
    assert product.name == name, f"Expected name {name!r}, got {product.name!r}"
    assert product.price == price, f"Expected price {price!r}, got {product.price!r}"
    assert product.price_with_vat == price_with_vat, (
        f"Expected price_with_vat {price_with_vat!r} for a price of {price!r}, got {product.price_with_vat!r}"
    )
