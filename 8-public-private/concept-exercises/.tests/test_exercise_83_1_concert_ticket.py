from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "concert,seat",
    [
        ("Coldplay", "B12"),
        ("Rock Werchter", "A1"),
        ("Stromae", "C104"),
    ]
)
def test_function(pytestconfig, concert, seat):
    ticket = call_function(__file__, "Ticket", [concert, seat])
    assert ticket.get_concert() == concert, f"Expected get_concert() to return {concert!r}, got {ticket.get_concert()!r}"
    assert ticket.get_seat() == seat, f"Expected get_seat() to return {seat!r}, got {ticket.get_seat()!r}"

def test_function_private_attributes(pytestconfig):
    ticket = call_function(__file__, "Ticket", ["Coldplay", "B12"])
    assert hasattr(ticket, "_concert"), "The concert should be stored in a private attribute '_concert'"
    assert hasattr(ticket, "_seat"), "The seat should be stored in a private attribute '_seat'"
    assert not hasattr(ticket, "concert"), "The concert should only be stored in the private attribute '_concert', not in a public attribute 'concert'"
    assert not hasattr(ticket, "seat"), "The seat should only be stored in the private attribute '_seat', not in a public attribute 'seat'"

def test_function_no_setters(pytestconfig):
    ticket = call_function(__file__, "Ticket", ["Coldplay", "B12"])
    assert not hasattr(ticket, "set_concert"), "A read-only attribute should not have a setter method (set_concert)"
    assert not hasattr(ticket, "set_seat"), "A read-only attribute should not have a setter method (set_seat)"
