from p1_util.tests.test_util import run_script

import pytest

PROMPT = "Enter the index of the field you would like to place your tick on: > "
BAD_MOVE = "Bad move, needs to be 0-8 and can't be on an occupied space!\n"


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


def is_valid_move(move, field):
    return move in [str(i) for i in range(9)] and field[int(move)] == " "


def play_turn(out, player, tick, field, moves):
    out.append(f"{player}, it's your turn.\n")
    move = next(moves)
    out.append(PROMPT + move + "\n")
    while not is_valid_move(move, field):
        out.append(BAD_MOVE)
        move = next(moves)
        out.append(PROMPT + move + "\n")
    field[int(move)] = tick
    out.append(render_board_update(field))


def build_expected(inputs):
    moves = iter(inputs)
    out = ["Welcome to Tic Tac Toe!\n\n"]

    player_1 = next(moves)
    out.append(f"Please enter the name of player 1: > {player_1}\n")
    tick_1 = next(moves)
    out.append(f"{player_1}, choose a tick: > {tick_1}\n")
    player_2 = next(moves)
    out.append(f"Please enter the name of player 2: > {player_2}\n")
    tick_2 = next(moves)
    out.append(f"{player_2}, choose a tick: > {tick_2}\n")

    field = [" "] * 9
    out.append(render_board_update(field))

    game_over = False
    while not game_over:
        play_turn(out, player_1, tick_1, field, moves)
        game_over = " " not in field
        if not game_over:
            play_turn(out, player_2, tick_2, field, moves)
            game_over = " " not in field

    return "".join(out)


@pytest.mark.parametrize(
    "inputs",
    [
        ["Alice", "X", "Bob", "O", "0", "1", "2", "3", "4", "5", "6", "7", "8"],
        ["Alice", "X", "Bob", "O", "4", "0", "8", "2", "6", "1", "7", "3", "5"],
        # an invalid move on the very last turn is rejected before the board fills
        ["Alice", "X", "Bob", "O", "0", "1", "2", "3", "4", "5", "6", "7", "9", "8"],
    ]
)
def test_function(pytestconfig, inputs):
    run_script(__file__, inputs, build_expected(inputs))
