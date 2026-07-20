from p1_util.tests.test_util import call_function

import pytest


# --- win_horizontally: any full row -------------------------------------------

@pytest.mark.parametrize(
    "field,tick,expected",
    [
        (["X", "X", "X", " ", " ", " ", " ", " ", " "], "X", True),
        ([" ", " ", " ", "O", "O", "O", " ", " ", " "], "O", True),
        ([" ", " ", " ", " ", " ", " ", "X", "X", "X"], "X", True),
        (["X", "X", "X", " ", " ", " ", " ", " ", " "], "O", False),
        (["X", "O", "X", "O", "X", "O", "X", "O", "X"], "X", False),
        # three in a row in the list, but spread over two rows of the board
        ([" ", " ", "X", "X", "X", " ", " ", " ", " "], "X", False),
        ([" ", "O", "O", "O", " ", " ", " ", " ", " "], "O", False),
        ([" ", " ", " ", " ", " ", "X", "X", "X", " "], "X", False),
        # a full column is not a horizontal win
        (["X", " ", " ", "X", " ", " ", "X", " ", " "], "X", False),
    ]
)
def test_function_win_horizontally(pytestconfig, field, tick, expected):
    result = call_function(__file__, "win_horizontally", [list(field), tick])
    assert result == expected, (
        f"win_horizontally({field}, {tick!r}) should return {expected}, "
        f"but it returned {result!r}."
    )


# --- win_vertically: any full column ------------------------------------------

@pytest.mark.parametrize(
    "field,tick,expected",
    [
        (["X", " ", " ", "X", " ", " ", "X", " ", " "], "X", True),
        ([" ", "O", " ", " ", "O", " ", " ", "O", " "], "O", True),
        ([" ", " ", "X", " ", " ", "X", " ", " ", "X"], "X", True),
        (["X", " ", " ", "X", " ", " ", " ", " ", " "], "X", False),
        (["X", "O", "X", "O", "X", "O", "O", "X", "O"], "X", False),
        # a full row is not a vertical win
        (["X", "X", "X", " ", " ", " ", " ", " ", " "], "X", False),
        ([" ", " ", "O", " ", " ", "O", " ", " ", " "], "O", False),
    ]
)
def test_function_win_vertically(pytestconfig, field, tick, expected):
    result = call_function(__file__, "win_vertically", [list(field), tick])
    assert result == expected, (
        f"win_vertically({field}, {tick!r}) should return {expected}, "
        f"but it returned {result!r}."
    )


# --- win_diagonally: either diagonal ------------------------------------------

@pytest.mark.parametrize(
    "field,tick,expected",
    [
        (["X", " ", " ", " ", "X", " ", " ", " ", "X"], "X", True),   # main diagonal
        ([" ", " ", "O", " ", "O", " ", "O", " ", " "], "O", True),   # anti-diagonal
        (["X", " ", " ", " ", "X", " ", " ", " ", "X"], "O", False),
        (["X", "X", " ", " ", "O", " ", " ", " ", " "], "X", False),
        ([" ", " ", "X", " ", "X", " ", " ", "X", " "], "X", False),
        (["X", " ", " ", " ", "X", " ", " ", "X", " "], "X", False),
        # a full row or column is not a diagonal win
        (["X", "X", "X", " ", " ", " ", " ", " ", " "], "X", False),
        ([" ", " ", "O", " ", " ", "O", " ", " ", "O"], "O", False),
    ]
)
def test_function_win_diagonally(pytestconfig, field, tick, expected):
    result = call_function(__file__, "win_diagonally", [list(field), tick])
    assert result == expected, (
        f"win_diagonally({field}, {tick!r}) should return {expected}, "
        f"but it returned {result!r}."
    )


# --- is_game_over: prints the outcome and reports whether the game ended --------

@pytest.mark.parametrize(
    "field,player,tick,message,expected",
    [
        # a win: prints "<player> won!"
        (["O", "O", "O", "X", "X", " ", " ", " ", " "], "Bob", "O", "Bob won!\n", True),
        (["X", " ", " ", "X", "O", " ", "X", " ", "O"], "Alice", "X", "Alice won!\n", True),
        ([" ", " ", "O", "X", "O", "X", "O", "X", " "], "Bob", "O", "Bob won!\n", True),
        # a win with the last free space is a win, not a draw
        (["X", "O", "X", "O", "X", "O", "O", "X", "X"], "Alice", "X", "Alice won!\n", True),
        # a full board with no line: a draw
        (["X", "X", "O", "O", "O", "X", "X", "X", "O"], "Alice", "X", "It's a draw!\n", True),
        (["X", "X", "O", "O", "O", "X", "X", "X", "O"], "Bob", "O", "It's a draw!\n", True),
        # the game is still going: no output, not over
        (["X", "O", " ", " ", " ", " ", " ", " ", " "], "Alice", "X", "", False),
        ([" ", " ", " ", " ", " ", " ", " ", " ", " "], "Bob", "O", "", False),
        # only the other player has a line: this player did not win
        (["O", "O", "O", "X", "X", " ", " ", " ", " "], "Alice", "X", "", False),
    ]
)
def test_function_is_game_over(pytestconfig, field, player, tick, message, expected):
    result = call_function(__file__, "is_game_over", [list(field), player, tick],
                               expected_output=message)
    assert result == expected, (
        f"is_game_over({field}, {player!r}, {tick!r}) should return {expected}, "
        f"but it returned {result!r}."
    )
