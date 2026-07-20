from p1_util.tests.test_util import run_script

def test_function(pytestconfig):
    expected_output = f"Hello you!\n"
    run_script(__file__, [], expected_output)

