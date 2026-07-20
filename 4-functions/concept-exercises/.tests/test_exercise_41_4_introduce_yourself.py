from p1_util.tests.test_util import call_function, run_script

import pytest

CASES = [
    ("James", "Bond", 42),
    ("Ada", "Lovelace", 28),
    ("Grace", "Hopper", 85),
]

@pytest.mark.parametrize("first_name,last_name,age", CASES)
def test_function(pytestconfig, first_name, last_name, age):
    result = call_function(__file__, "introduce", [first_name, last_name, age],
                               expected_output=f"Hi! My name is {first_name} {last_name} and I am {age} years old.\n")
    assert result is None, "introduce() is not supposed to return anything"

@pytest.mark.parametrize("first_name,last_name,age", CASES)
def test_function_script(pytestconfig, first_name, last_name, age):
    expected_output = f"What is your first name? > {first_name}\n"
    expected_output += f"What is your last name? > {last_name}\n"
    expected_output += f"How old are you? > {age}\n"
    expected_output += f"Hi! My name is {first_name} {last_name} and I am {age} years old.\n"
    run_script(__file__, [first_name, last_name, age], expected_output)
