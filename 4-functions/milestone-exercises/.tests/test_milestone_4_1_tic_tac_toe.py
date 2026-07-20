from p1_util.tests.test_util import run_script

import pytest

PROMPT = "Enter the index of the field you would like to place your tick on: > "
BAD_MOVE = "Bad move, needs to be 0-8 and can't be on an occupied space!\n"

LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (2, 4, 6), (0, 4, 8),              # diagonals
]


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


def has_won(field, tick):
    return any(all(field[i] == tick for i in line) for line in LINES)


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


def check_game_over(out, field, player, tick):
    if has_won(field, tick):
        out.append(f"{player} won!\n")
        return True
    if " " not in field:
        out.append("It's a draw!\n")
        return True
    return False


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

    stop = False
    while not stop:
        field = [" "] * 9
        out.append(render_board_update(field))

        game_over = False
        while not game_over:
            play_turn(out, player_1, tick_1, field, moves)
            game_over = check_game_over(out, field, player_1, tick_1)
            if not game_over:
                play_turn(out, player_2, tick_2, field, moves)
                game_over = check_game_over(out, field, player_2, tick_2)

        again = next(moves)
        out.append(f"Do you want to play again (Y/N)? > {again}\n")
        if again.lower() == "n":
            stop = True

    out.append("Thank you for playing!\n")
    return "".join(out)


@pytest.mark.parametrize(
    "inputs",
    [
        # player 1 wins the top row
        ["Alice", "X", "Bob", "O", "0", "3", "1", "4", "2", "n"],
        # player 1 wins the left column
        ["Alice", "X", "Bob", "O", "0", "1", "3", "2", "6", "n"],
        # player 2 wins on a diagonal
        ["Alice", "X", "Bob", "O", "1", "0", "2", "4", "5", "8", "n"],
        # a full board with no winner: a draw
        ["Alice", "O", "Bob", "X", "0", "2", "1", "3", "5", "4", "6", "8", "7", "n"],
        # player 1 wins with the very last free space: a win, not a draw
        ["Alice", "X", "Bob", "O", "0", "1", "2", "3", "4", "5", "7", "6", "8", "n"],
        # a draw, a rematch that is only stopped by N (any other answer continues), then a win
        ["Alice", "O", "Bob", "X", "0", "2", "1", "3", "5", "4", "6", "8", "7", "yes",
         "0", "3", "1", "4", "2", "N"],
        # invalid moves are rejected, and an uppercase N also quits
        ["Alice", "X", "Bob", "O", "9", "0", "3", "x", "1", "4", "2", "N"],
        # play a game, ask for a rematch, then quit
        ["Alice", "X", "Bob", "O", "0", "3", "1", "4", "2", "y",
         "0", "3", "1", "4", "2", "n"],
    ]
)
def test_function(pytestconfig, inputs):
    run_script(__file__, inputs, build_expected(inputs))
