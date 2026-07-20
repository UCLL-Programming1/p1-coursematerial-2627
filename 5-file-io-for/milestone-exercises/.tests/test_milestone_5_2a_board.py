from p1_util.tests.test_util import call_function, run_script

import pytest


def board_to_text(board):
    return "".join(" ".join(row) + "\n" for row in board)


def empty_board():
    return [["-"] * 7 for _ in range(6)]


def build_expected(inputs):
    """Play the moves and build everything the program should print."""
    board = empty_board()
    current_player = "X"
    output = ""

    for i, move in enumerate(inputs):
        output += board_to_text(board)
        output += f"Player {current_player}, choose a column (1-7): > {move}\n"

        column = int(move) - 1
        free_rows = [row for row in range(5, -1, -1) if board[row][column] == "-"]
        if not free_rows:
            output += "That column is full!\n"
            continue

        board[free_rows[0]][column] = current_player

        if all("-" not in row for row in board):
            assert i == len(inputs) - 1, "test error: the board is full before all moves are played"
            output += board_to_text(board)
            output += "The board is full!\n"
            return output

        current_player = "O" if current_player == "X" else "X"

    raise AssertionError("test error: the board never gets full with these moves")


FILL_IN_ORDER = [str(column) for column in range(1, 8) for _ in range(6)]
FILL_BACKWARDS = [str(column) for column in range(7, 0, -1) for _ in range(6)]
# filling the board row by row, so no column is ever full before the end
FILL_ROW_BY_ROW = [str(column) for _ in range(6) for column in range(1, 8)]
# after filling the first column, players keep trying that full column
FULL_COLUMN = ["1"] * 6 + ["1", "2", "1", "1", "2"] + FILL_IN_ORDER[8:]
# the very last free space is filled after a couple of attempts on full columns
FULL_AT_THE_END = FILL_IN_ORDER[:-1] + ["1", "6", "7"]


@pytest.mark.parametrize(
    "inputs",
    [FILL_IN_ORDER, FILL_BACKWARDS, FILL_ROW_BY_ROW, FULL_COLUMN, FULL_AT_THE_END],
    ids=["in order", "backwards", "row by row", "full column", "full column at the end"],
)
def test_function(pytestconfig, inputs):
    run_script(__file__, inputs, build_expected(inputs))


def test_function_print_board(pytestconfig):
    board = empty_board()
    board[5][0] = "X"
    board[5][1] = "O"
    board[0][6] = "X"
    call_function(__file__, "print_board", [board], expected_output=board_to_text(board))


@pytest.mark.parametrize("column", [0, 3, 6])
def test_function_drop_piece(pytestconfig, column):
    board = empty_board()
    pieces = ["X", "O", "X", "O", "X", "O"]
    for number, piece in enumerate(pieces):
        result = call_function(__file__, "drop_piece", [board, column, piece])
        assert result is True, (
            f"drop_piece should return True when the piece fits in column {column}, but it returned {result!r}"
        )
        row = 5 - number
        assert board[row][column] == piece, (
            f"Piece number {number + 1} dropped in column {column} should land on row {row}, "
            f"but the board is:\n{board_to_text(board)}"
        )
    before = [list(row) for row in board]
    result = call_function(__file__, "drop_piece", [board, column, "X"])
    assert result is False, (
        f"drop_piece should return False when column {column} is full, but it returned {result!r}"
    )
    assert board == before, "Dropping a piece in a full column should not change the board"


def test_function_board_full(pytestconfig):
    board = empty_board()
    assert call_function(__file__, "board_full", [board]) is False, "An empty board is not full"
    for row in range(6):
        for column in range(7):
            board[row][column] = "X" if (row + column) % 2 else "O"
    assert call_function(__file__, "board_full", [board]) is True, "A board without any '-' is full"
    for row, column in [(0, 0), (0, 6), (5, 6), (2, 3)]:
        board[row][column] = "-"
        result = call_function(__file__, "board_full", [board])
        assert result is False, (
            f"A board with a free space on row {row}, column {column} is not full, but board_full returned {result!r}"
        )
        board[row][column] = "X"
