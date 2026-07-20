from p1_util.tests.test_util import call_function, run_script

import pytest

EMPTY = [" "] * 9


def render_field(field):
    return (
        f"{field[0]} | {field[1]} | {field[2]}\n"
        f"{field[3]} | {field[4]} | {field[5]}\n"
        f"{field[6]} | {field[7]} | {field[8]}\n"
        "\n"
    )


def render_indices():
    return render_field([0, 1, 2, 3, 4, 5, 6, 7, 8])


def render_board_update(field):
    return (
        "\n"
        "The current board is:\n"
        + render_field(field)
        + "The indices of these board spaces are:\n"
        + render_indices()
    )


# --- initialize_field: returns a fresh, empty board ----------------------------

def test_function(pytestconfig):
    result = call_function(__file__, "initialize_field", [], expected_output="")
    assert result == [" "] * 9, (
        f"initialize_field() should return a list of 9 empty spaces "
        f"({[' '] * 9}), but it returned {result!r}."
    )


# --- print_field: prints one board, three rows plus a blank line ---------------

@pytest.mark.parametrize(
    "field",
    [
        list(EMPTY),
        [" ", " ", " ", "X", " ", " ", " ", " ", " "],
        ["O", "X", "O", "X", "O", "X", "O", "X", "O"],
    ]
)
def test_function_print_field(pytestconfig, field):
    result = call_function(__file__, "print_field", [list(field)],
                               expected_output=render_field(field))
    assert result is None, (
        f"print_field should print the board and not return anything, "
        f"but it returned {result!r}."
    )


# --- print_indices: always prints the numbered layout --------------------------

def test_function_print_indices(pytestconfig):
    result = call_function(__file__, "print_indices", [],
                               expected_output=render_indices())
    assert result is None, (
        f"print_indices should print the numbered layout and not return anything, "
        f"but it returned {result!r}."
    )


# --- print_board_update: the full board + indices block ------------------------

@pytest.mark.parametrize(
    "field",
    [
        list(EMPTY),
        [" ", " ", " ", "X", " ", " ", " ", " ", " "],
        ["O", " ", "X", " ", "X", " ", " ", " ", "O"],
    ]
)
def test_function_print_board_update(pytestconfig, field):
    result = call_function(__file__, "print_board_update", [list(field)],
                               expected_output=render_board_update(field))
    assert result is None, (
        f"print_board_update should print the board and not return anything, "
        f"but it returned {result!r}."
    )


# --- the whole program: place an X on space 3 and show the board ---------------

def test_function_script(pytestconfig):
    field = list(EMPTY)
    field[3] = "X"
    field[7] = "O"
    run_script(__file__, [], render_board_update(field))
