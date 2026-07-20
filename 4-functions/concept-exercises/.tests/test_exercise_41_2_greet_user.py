from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize("name", [("Alice"), ("Bob"), ("James")])
def test_function(pytestconfig, name):
    return_value = call_function(__file__, "greet", [name], expected_output=f"Hello, {name}! Nice to meet you.\n")
    assert return_value is None, "The function greet(name) is not supposed to return anything."

def test_function_script(pytestconfig):
    run_script(__file__, [], "Hello, Alice! Nice to meet you.\n")
