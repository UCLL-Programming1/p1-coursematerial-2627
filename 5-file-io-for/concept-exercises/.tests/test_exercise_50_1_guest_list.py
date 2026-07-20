
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (["Barack Obama"], "Barack Obama is on the guest list!\n"),
        (["Freddie Mercury"], "Freddie Mercury is not on the guest list!\n"),
        # the last name in the file (this line has no newline at the end)
        (["Elliot Page"], "Elliot Page is on the guest list!\n"),
        (["Ada Lovelace"], "Ada Lovelace is on the guest list!\n"),
        # only part of a name on the list is not enough
        (["Barack"], "Barack is not on the guest list!\n"),
        (["Page"], "Page is not on the guest list!\n"),
    ]
)
def test_function(pytestconfig, inputs, expected):
    expected_output = (
        f"What is the name of the guest? > {inputs[0]}\n"
        f"{expected}"
    )

    run_script(__file__, inputs, expected_output)
