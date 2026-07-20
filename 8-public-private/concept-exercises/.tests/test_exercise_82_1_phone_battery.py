from p1_util.tests.test_util import call_function, run_script

import pytest

def test_function(pytestconfig):
    phone = call_function(__file__, "Phone", ["Fairphone"])
    assert phone.brand == "Fairphone", f"Expected brand 'Fairphone', got {phone.brand!r}"
    assert phone.get_battery() == 100, f"A new phone should have battery level 100, got {phone.get_battery()!r}"

def test_function_private_attribute(pytestconfig):
    phone = call_function(__file__, "Phone", ["Fairphone"])
    assert hasattr(phone, "_battery"), "The battery level should be stored in a private attribute '_battery'"
    assert not hasattr(phone, "battery"), "The battery level should only be stored in the private attribute '_battery', not in a public attribute 'battery'"

@pytest.mark.parametrize(
    "new_battery,expected",
    [
        (40, 40),
        (0, 0),
        (100, 100),
        (-1, 0),
        (-30, 0),
        (101, 100),
        (150, 100),
    ]
)
def test_function_setter(pytestconfig, new_battery, expected):
    phone = call_function(__file__, "Phone", ["Fairphone"])
    phone.set_battery(new_battery)
    result = phone.get_battery()
    assert result == expected, f"set_battery({new_battery}) - Expected battery level: {expected}, Result: {result}"
