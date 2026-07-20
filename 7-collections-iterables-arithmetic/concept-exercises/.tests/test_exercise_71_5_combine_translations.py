
from p1_util.tests.test_util import run_script

import pytest


@pytest.mark.parametrize(
    "inputs,expected_dict",
    [
        (
            [
                "cat,kat",
                "dog,hond",
                "elephant,olifant",
                "Q",
                "kat,chat",
                "hond,chien",
                "zeehond,phoque",
                "Q",
            ],
            "{'cat': 'chat', 'dog': 'chien'}"
        ),
        (
            [
                "red,rood",
                "blue,blauw",
                "Q",
                "rood,rouge",
                "blauw,bleu",
                "Q",
            ],
            "{'red': 'rouge', 'blue': 'bleu'}"
        ),
        (
            [
                "house,huis",
                "tree,boom",
                "Q",
                "huis,maison",
                "Q",
            ],
            "{'house': 'maison'}"
        ),
        (
            [
                "Q",
                "Q",
            ],
            "{}"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected_dict):
    expected_output = ""

    idx = 0

    # First dictionary prompts
    while inputs[idx] != "Q":
        expected_output += f"Provide a key and value for the first dictionary, or (Q) quit: > {inputs[idx]}\n"
        idx += 1

    expected_output += f"Provide a key and value for the first dictionary, or (Q) quit: > {inputs[idx]}\n"
    idx += 1

    # Second dictionary prompts
    while inputs[idx] != "Q":
        expected_output += f"Provide a key and value for the second dictionary, or (Q) quit: > {inputs[idx]}\n"
        idx += 1

    expected_output += f"Provide a key and value for the second dictionary, or (Q) quit: > {inputs[idx]}\n"

    expected_output += f"The combined dictionary is: {expected_dict}\n"

    run_script(__file__, inputs, expected_output)
