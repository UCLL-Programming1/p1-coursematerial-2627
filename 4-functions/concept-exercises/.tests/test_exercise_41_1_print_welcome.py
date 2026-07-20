from p1_util.tests.test_util import call_function, run_script

import pytest

WELCOME = "=== Welcome to Coffee Corner! ===\n"

def test_function(pytestconfig):
    return_value = call_function(__file__, "print_welcome", [], expected_output=WELCOME)
    assert return_value is None, "print_welcome() is not supposed to return anything"

def test_function_script(pytestconfig):
    run_script(__file__, [], WELCOME)
