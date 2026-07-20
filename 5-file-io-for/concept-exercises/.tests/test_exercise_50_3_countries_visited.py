
from p1_util.tests.test_util import run_script, get_script_dir, restore_files

import pytest
import os

@pytest.mark.parametrize(
    "inputs,added_country",
    [
        (["Portugal"], "Portugal"),
        (["Turkey"], "Turkey"),
    ]
)
def test_function(pytestconfig, inputs, added_country):
    script_dir = get_script_dir(__file__)

    with restore_files(__file__, "countries.txt"):
        # Ensure a clean starting file
        with open(script_dir / "countries.txt", "w") as f:
            f.write("France\nGermany\nBelgium\n")

        expected_output = (
            f"Which country do you want to add? > {inputs[0]}\n"
            f"{added_country} has been added to the list.\n"
        )

        run_script(__file__, inputs, expected_output)

        # Verify file content after execution
        with open(script_dir / "countries.txt") as f:
            content = f.read()

        expected_content = (
            "France\n"
            "Germany\n"
            "Belgium\n"
            f"{added_country}\n"
        )

        assert content == expected_content
