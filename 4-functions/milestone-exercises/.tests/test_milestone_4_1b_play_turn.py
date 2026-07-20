from p1_util.tests.test_util import call_function, run_script

import pytest

PROMPT = "Enter the index of the field you would like to place your tick on: > "
BAD_MOVE = "Bad move, needs to be 0-8 and can't be on an occupied space!\n"
EMPTY = [" "] * 9


def render_field(field):
    return (
        f"{field[0]} | {field[1]} | {field[2]}\n"
        f"{field[3]} | {field[4]} | {field[5]}\n"
        f"{field[6]} | {field[7]} | {field[8]}\n"
        "\n"
    )


def render_board_update(field):
    output = "\n"
    output += "The current board is:\n"
    output += render_field(field)
    output += "The indices of these board spaces are:\n"
    output += render_field([0, 1, 2, 3, 4, 5, 6, 7, 8])
    return output


def turn_output(player, field_after, attempts):
    # attempts is the list of moves the player types; every attempt except the
    # last is rejected, and the last one is the valid move that ends the turn.
    output = f"{player}, it's your turn.\n"
    output += PROMPT + attempts[0] + "\n"
    for i in range(len(attempts) - 1):
        output += BAD_MOVE
        output += PROMPT + attempts[i + 1] + "\n"
    output += render_board_update(field_after)
    return output


# --- is_valid_move: a plain true/false function --------------------------------

@pytest.mark.parametrize(
    "move,field,expected",
    [
        ("0", list(EMPTY), True),
        ("4", list(EMPTY), True),
        ("8", list(EMPTY), True),
        ("9", list(EMPTY), False),
        ("-1", list(EMPTY), False),
        ("x", list(EMPTY), False),
        ("", list(EMPTY), False),
        ("4", [" ", " ", " ", " ", "X", " ", " ", " ", " "], False),
    ]
)
def test_function(pytestconfig, move, field, expected):
    result = call_function(__file__, "is_valid_move", [move, list(field)])
    assert result == expected, (
        f"is_valid_move({move!r}, {field}) should return {expected}, "
        f"but it returned {result!r}."
    )


# --- ask_player_move: prints a prompt and returns what was typed ---------------

@pytest.mark.parametrize("typed", ["4", "0", "banana"])
def test_function_ask_player_move(pytestconfig, typed):
    result = call_function(__file__, "ask_player_move", [], inputs=[typed],
                               expected_output=PROMPT + typed + "\n")
    assert result == typed, (
        f"ask_player_move() should return exactly what the player typed ({typed!r}), "
        f"but it returned {result!r}."
    )


# --- play_turn: prompts, rejects bad moves, fills in the field, prints board ----

@pytest.mark.parametrize(
    "player,tick,start,place_at,attempts",
    [
        ("Player 1", "X", list(EMPTY), 4, ["4"]),
        ("Player 2", "O", [" ", " ", " ", " ", "X", " ", " ", " ", " "], 0, ["0"]),
        ("Player 1", "X", list(EMPTY), 4, ["9", "x", "4"]),
        ("Player 2", "O", ["X", " ", " ", " ", " ", " ", " ", " ", " "], 4, ["0", "4"]),
    ]
)
def test_function_play_turn(pytestconfig, player, tick, start, place_at, attempts):
    field = list(start)
    expected_field = list(start)
    expected_field[place_at] = tick
    result = call_function(__file__, "play_turn", [player, tick, field],
                               inputs=attempts,
                               expected_output=turn_output(player, expected_field, attempts))
    # the function should fill in the move in place
    assert field == expected_field, (
        f"After play_turn, {tick!r} should be placed on space {place_at}. "
        f"Expected the board to be {expected_field}, but it was {field}."
    )
    # play_turn does its work by side effect, not by returning
    assert result is None, (
        f"play_turn should not return anything, but it returned {result!r}."
    )


# --- the whole program: an empty board, then Player 1 plays their turn ----------

@pytest.mark.parametrize("attempts,place_at", [(["4"], 4), (["8"], 8), (["9", "0"], 0)])
def test_function_script(pytestconfig, attempts, place_at):
    field_after = list(EMPTY)
    field_after[place_at] = "X"
    run_script(__file__, attempts, turn_output("Player 1", field_after, attempts))
