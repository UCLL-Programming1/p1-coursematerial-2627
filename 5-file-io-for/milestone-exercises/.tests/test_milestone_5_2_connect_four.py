
from p1_util.tests.test_util import run_script

import pytest


def board_to_text(board):
    return "".join(" ".join(row) + "\n" for row in board)


def has_four(board, piece):
    for row in range(6):
        for column in range(7):
            for d_row, d_column in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
                cells = [(row + i * d_row, column + i * d_column) for i in range(4)]
                if all(0 <= r < 6 and 0 <= c < 7 and board[r][c] == piece for r, c in cells):
                    return True
    return False


def build_expected(inputs):
    """Play the moves and build everything the program should print."""
    board = [["-"] * 7 for _ in range(6)]
    current_player = "X"
    output = ""

    for i, move in enumerate(inputs):
        output += board_to_text(board)
        output += f"Player {current_player}, choose a column (1-7): > {move}\n"

        column = int(move)
        if column < 1 or column > 7:
            output += "Invalid column!\n"
            continue

        free_rows = [row for row in range(5, -1, -1) if board[row][column - 1] == "-"]
        if not free_rows:
            output += "That column is full!\n"
            continue

        board[free_rows[0]][column - 1] = current_player

        if has_four(board, current_player):
            assert i == len(inputs) - 1, "test error: the game ends before all moves are played"
            output += board_to_text(board)
            output += f"Player {current_player} wins!\n"
            return output

        current_player = "O" if current_player == "X" else "X"

    raise AssertionError("test error: nobody wins with these moves")


@pytest.mark.parametrize(
    "inputs",
    [
        # Horizontal win for X
        ["1", "1", "2", "2", "3", "3", "4"],
        # Horizontal win for X against the right edge of the board
        ["4", "4", "5", "5", "6", "6", "7"],
        # Vertical win for X
        ["1", "2", "1", "2", "1", "2", "1"],
        # Vertical win for O in the last column
        ["1", "7", "2", "7", "1", "7", "3", "7"],
        # Vertical win for X in the top four rows of a column
        ["2", "1", "3", "1", "1", "5", "1", "5", "1", "6", "1"],
        # Diagonal win for X
        ["1", "2", "2", "3", "7", "3", "3", "4", "7", "4", "7", "4", "4"],
        # Diagonal win for O, ending in the last column
        ["6", "4", "7", "6", "1", "6", "5", "5", "7", "7", "3", "7"],
        # Diagonal win touching the top row and the last column
        ["1", "5", "5", "6", "4", "2", "1", "6", "3", "5", "5", "4",
         "4", "2", "6", "6", "4", "4", "7", "4", "7", "7", "1", "5"],
        # A full column and invalid column numbers: the same player has to try again
        ["1", "1", "1", "1", "1", "1", "1", "0", "8", "2", "3", "2", "3", "2", "3", "2"],
        # Invalid column numbers for player O
        ["4", "-1", "10", "5", "4", "5", "4", "5", "4"],
    ]
)
def test_function(pytestconfig, inputs):
    run_script(__file__, inputs, build_expected(inputs))
