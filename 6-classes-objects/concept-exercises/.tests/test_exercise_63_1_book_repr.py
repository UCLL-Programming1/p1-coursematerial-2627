from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "title,author",
    [
        ("Dune", "Frank Herbert"),
        ("Emma", "Jane Austen"),
        ("1984", "George Orwell"),
    ]
)
def test_function(pytestconfig, title, author):
    book = call_function(__file__, "Book", [title, author])
    assert book.title == title, f"Expected title {title!r}, got {book.title!r}"
    assert book.author == author, f"Expected author {author!r}, got {book.author!r}"

    expected = f'Book("{title}", "{author}")'
    actual = repr(book)
    assert actual == expected, f"Expected the string representation {expected!r}, got {actual!r}"

def test_function_in_list(pytestconfig):
    book_1 = call_function(__file__, "Book", ["Dune", "Frank Herbert"])
    book_2 = call_function(__file__, "Book", ["Emma", "Jane Austen"])

    expected = '[Book("Dune", "Frank Herbert"), Book("Emma", "Jane Austen")]'
    actual = f"{[book_1, book_2]}"
    assert actual == expected, (
        f"Printing a list of books should also use your string representation.\n"
        f"Expected: {expected}\nResult: {actual}"
    )
