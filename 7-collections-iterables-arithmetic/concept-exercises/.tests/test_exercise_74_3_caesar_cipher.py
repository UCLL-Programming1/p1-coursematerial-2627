
from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,encrypted",
    [
        (
            ["THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", "3"],
            "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
        ),
        (
            ["HELLO WORLD", "5"],
            "CZGGJ RJMGY"
        ),
        (
            ["ABC XYZ", "1"],
            "ZAB WXY"
        ),
        (
            ["PYTHON", "13"],
            "CLGUBA"
        ),
        (
            ["SECRET MESSAGE", "26"],
            "SECRET MESSAGE"
        ),
        # a shift of more than 26 wraps around the whole alphabet
        (
            ["THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", "29"],
            "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
        ),
        (
            ["ABC XYZ", "53"],
            "ZAB WXY"
        ),
        # a shift of 0 changes nothing
        (
            ["HELLO WORLD", "0"],
            "HELLO WORLD"
        ),
        # the last letters of the alphabet with the biggest possible shift
        (
            ["AZ", "25"],
            "BA"
        ),
    ]
)
def test_function(pytestconfig, inputs, encrypted):
    original_message = inputs[0]

    expected_output = (
        f"Pass a message to encrypt: > {inputs[0]}\n"
        f"Provide the shift to encrypt it with: > {inputs[1]}\n"
        f"Your encrypted message is : {encrypted}\n"
        f"Your decrypted message is : {original_message}\n"
    )

    run_script(__file__, inputs, expected_output)
