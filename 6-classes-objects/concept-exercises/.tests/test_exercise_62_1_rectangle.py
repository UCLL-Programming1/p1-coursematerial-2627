from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "width,height,area,perimeter",
    [
        (4, 3, 12, 14),
        (5, 5, 25, 20),
        (1, 10, 10, 22),
        (7, 2, 14, 18),
    ]
)
def test_function(pytestconfig, width, height, area, perimeter):
    rectangle = call_function(__file__, "Rectangle", [width, height])
    assert rectangle.width == width, f"Expected width {width!r}, got {rectangle.width!r}"
    assert rectangle.height == height, f"Expected height {height!r}, got {rectangle.height!r}"

    actual_area = rectangle.area()
    assert actual_area == area, f"Rectangle({width}, {height}).area() - Expected: {area}, Result: {actual_area}"

    actual_perimeter = rectangle.perimeter()
    assert actual_perimeter == perimeter, f"Rectangle({width}, {height}).perimeter() - Expected: {perimeter}, Result: {actual_perimeter}"
