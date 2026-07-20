from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "phone,country_code",
    [
        ("0470123456", "32"),
        ("0123456789", "1"),
        ("0987654321", "44"),
    ]
)
def test_function(pytestconfig, phone, country_code):
    expected_output = (
        f"Enter a 10-digit phone number: > {phone}\n"
        f"Enter your country code: > {country_code}\n"
        f"Full phone number: +{country_code}{phone[1:]}\n"
    )
    run_script(__file__, [phone, country_code], expected_output)
