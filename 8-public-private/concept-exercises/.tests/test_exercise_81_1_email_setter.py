from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "raw_email,clean_email",
    [
        (" Alice@Gmail.Com ", "alice@gmail.com"),
        ("BOB@ucll.be\n", "bob@ucll.be"),
        ("james@gmail.com", "james@gmail.com"),
        ("  UPPER@CASE.COM", "upper@case.com"),
    ]
)
def test_function(pytestconfig, raw_email, clean_email):
    contact = call_function(__file__, "Contact", ["Alice", raw_email])
    assert contact.email == clean_email, (
        f"Creating a Contact with email {raw_email!r} should store {clean_email!r}, got {contact.email!r}"
    )

@pytest.mark.parametrize(
    "raw_email,clean_email",
    [
        ("Alice@UCLL.be\n", "alice@ucll.be"),
        (" NEW@Email.Com ", "new@email.com"),
    ]
)
def test_function_setter(pytestconfig, raw_email, clean_email):
    contact = call_function(__file__, "Contact", ["Alice", "alice@gmail.com"])
    contact.set_email(raw_email)
    assert contact.email == clean_email, (
        f"set_email({raw_email!r}) should store {clean_email!r}, got {contact.email!r}"
    )
