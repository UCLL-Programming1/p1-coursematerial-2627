
from p1_util.tests.test_util import run_script, get_script_dir, restore_files

import pytest

@pytest.mark.parametrize(
    "inputs,previous_content",
    [
        # a book with a few sentences
        (
            ["This is the first sentence.", "Here comes another one.", "Writing files is fun.", "Q"],
            None,
        ),
        # a book with a single sentence
        (
            ["Winnie-the-Pooh.", "Q"],
            None,
        ),
        # an empty book: the file is created, but stays empty
        (
            ["Q"],
            None,
        ),
        # an existing book.txt is replaced by the new book
        (
            ["A brand new story.", "Q"],
            "An old story\nthat should be gone.\n",
        ),
    ]
)
def test_function(pytestconfig, inputs, previous_content):
    expected_output = ""
    for line in inputs:
        expected_output += f"Enter a sentence or (Q) quit: > {line}\n"

    script_dir = get_script_dir(__file__)

    with restore_files(__file__, "book.txt"):
        book = script_dir / "book.txt"
        if previous_content is None:
            book.unlink(missing_ok=True)
        else:
            book.write_text(previous_content)

        run_script(__file__, inputs, expected_output)

        assert book.exists(), "Your program should create the file book.txt"
        content = book.read_text()

        expected_file_content = ""
        for line in inputs[:-1]:
            expected_file_content += line + "\n"

        assert content == expected_file_content, (
            f"book.txt should contain:\n{expected_file_content!r}\nbut it contains:\n{content!r}"
        )
