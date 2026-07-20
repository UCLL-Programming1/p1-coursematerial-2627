import random

from p1_util.tests.test_util import (call_function, capture_outputs,
                                     get_script_dir, restore_files, run_script)

import pytest

SUITS = ["H", "D", "C", "S"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
FULL_DECK = [suit + rank for suit in SUITS for rank in RANKS]

PROMPT = "Play card or draw (D): > "
SUIT_PROMPT = "Choose suit (H D C S): > "
NOT_IN_HAND = "You don't have this card in your hand, play again\n"
NO_MATCH = "The card you want to play doesn't match the suit nor rank of the top card\n"
def drew(name):
    return f"{name} drew a card\n"

NAMES = ["Alice", "Bob", "Carol"]
SCORES = "scores.txt"
START_OF_FILE = "Alice:3\nBob:1\n"

# Complete scripted games, each with the seed that deals its cards: the number of
# players, their names, and then every line the players type, in order.
# The last value is the scoreboard the file should hold after the game.
GAMES = [
    (7, ["3"] + NAMES + ["ca", "h10", "d8", "S", "sa", "s3", "s6", "h6", "h5",
                         "h10", "h9", "h3", "h4", "c4", "d", "c2"],
     {"Alice": 4, "Bob": 1}),
    (72, ["2", "Alice", "Bob", "d", "dq", "s8", "S", "s10", "sk", "s6", "sa", "ca",
          "d", "cq"],
     {"Alice": 3, "Bob": 2}),
    (97, ["4", "Carol", "Dave", "Alice", "Bob", "c3", "s3", "sa", "c8", "D", "dq",
          "d10", "h10", "d", "hk", "h2", "h6", "d", "h4", "h5", "d", "d", "d", "h3"],
     {"Alice": 3, "Bob": 1, "Dave": 1}),
    # the second player wins by playing an 8 as their last card
    (10, ["3"] + NAMES + ["cj", "c9", "d", "c3", "d3", "h8", "h", "h3", "ha", "hk", "d", "ck", "sk", "s2", "d8", "h"],
     {"Alice": 3, "Bob": 2}),
]


# --- building objects out of the student's classes -----------------------------
# call_function loads the script's definitions without running main(), so every
# helper below hands back a real object of the student's own class.

def make_card(value):
    return call_function(__file__, "Card", [value])


def make_deck(values=None):
    deck = call_function(__file__, "Deck", [])
    if values is not None:
        deck.cards = [make_card(value) for value in values]
    return deck


def make_pile(top, current_suit=None, below=()):
    pile = call_function(__file__, "DiscardPile", [make_card(top)])
    pile.cards = [make_card(value) for value in below] + [make_card(top)]
    pile.current_suit = current_suit if current_suit is not None else top[0]
    return pile


def make_player(name, values):
    return call_function(__file__, "Player",
                         [name, [make_card(value) for value in values]])


def turn_text(top, current_suit, hand, typed, after=""):
    """What one pass through the turn loop prints."""
    return (
        f"Top card: {top}\n"
        f"Top suit: {current_suit}\n"
        f"Your hand: [{', '.join(hand)}]\n"
        f"{PROMPT}{typed}\n"
        f"{after}"
        "\n"
    )


def scores_file():
    return get_script_dir(__file__) / SCORES


def read_scoreboard():
    """The scoreboard as it is in the file right now."""
    scoreboard = {}
    for line in scores_file().read_text(encoding="utf-8").splitlines():
        if line.strip():
            name, wins = line.strip().split(":")
            scoreboard[name] = int(wins)
    return scoreboard


def deal_the_same_cards(seed):
    """Rebuild the deal the program gets from random.seed(seed): the deck is
    built in the same order and every card is drawn with the same randrange
    call, so the test knows exactly which cards end up where."""
    rng = random.Random(seed)
    deck = list(FULL_DECK)

    def draw(number=1):
        return [deck.pop(rng.randrange(len(deck))) for _ in range(number)]

    return deck, draw


def build_expected(inputs, seed):
    """Play the scripted game and build everything the program prints."""
    moves = iter(inputs)
    deck, draw = deal_the_same_cards(seed)
    scoreboard = read_scoreboard()

    out = []
    number_of_players = next(moves)
    out.append(f"How many players are playing? > {number_of_players}\n")
    names, hands = [], []
    for i in range(int(number_of_players)):
        name = next(moves)
        out.append(f"Enter the name for player {i + 1}: > {name}\n")
        out.append(f"Current number of wins for {name}: {scoreboard.get(name, 0)}\n")
        names.append(name)
        hands.append(draw(5))

    pile = draw(1)
    suit = pile[0][0]

    player = 0
    while True:
        name, hand = names[player], hands[player]
        out.append(f"{name}'s turn!\n")

        finish_turn = False
        while not finish_turn:
            # what the program prints before it knows what the player will type
            top_card, shown_suit, shown_hand = pile[-1], suit, list(hand)
            typed = next(moves)
            move = typed.upper()
            after = ""

            if move == "D":
                finish_turn = True
                after = drew(name)
                hand.extend(draw(1))
                if not deck:
                    while len(pile) > 1:
                        deck.append(pile.pop(0))

            elif move not in hand:
                after = NOT_IN_HAND

            elif not (move[0] == suit or move[1:] == top_card[1:] or move[1:] == "8"):
                after = NO_MATCH

            else:
                finish_turn = True
                hand.remove(move)
                pile.append(move)
                if move[1] == "8":
                    chosen = next(moves)
                    after = SUIT_PROMPT + chosen + "\n"
                    suit = chosen.upper()
                else:
                    suit = move[0]

            out.append(turn_text(top_card, shown_suit, shown_hand, typed, after))

        if not hand:
            scoreboard[name] = scoreboard.get(name, 0) + 1
            out.append(f"{name} wins! They now have {scoreboard[name]} wins!\n")
            return "".join(out)
        player = (player + 1) % len(names)


# --- Card ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "value,suit,rank",
    [("DA", "D", "A"), ("C10", "C", "10"), ("H8", "H", "8"), ("SK", "S", "K")]
)
def test_function(pytestconfig, value, suit, rank):
    card = make_card(value)
    assert card.suit == suit, f"Card({value!r}).suit should be {suit!r}, got {card.suit!r}."
    assert card.rank == rank, f"Card({value!r}).rank should be {rank!r}, got {card.rank!r}."
    assert repr(card) == value, (
        f"A Card should be printed as {value!r}, but printing Card({value!r}) "
        f"shows {repr(card)}."
    )


@pytest.mark.parametrize(
    "value,top,current_suit,expected",
    [
        ("C10", "C3", "C", True),    # same suit as the current suit
        ("D9", "S9", "S", True),     # same rank as the top card
        ("H8", "SK", "S", True),     # an 8 can always be played
        ("H7", "SK", "D", False),    # neither the suit nor the rank matches
        ("D5", "D8", "S", False),    # the top card is an 8, but the suit was changed to S
        ("S5", "D8", "S", True),     # ... so a spade is what matches now
        ("HK", "SK", "D", True),     # the rank matches even though the suit does not
    ]
)
def test_function_is_playable(pytestconfig, value, top, current_suit, expected):
    card = make_card(value)
    pile = make_pile(top, current_suit)
    result = card.is_playable(pile)
    assert result == expected, (
        f"With {top} on top of the discard pile and {current_suit} as the current suit, "
        f"{value}.is_playable(discard_pile) should be {expected}, but it returned {result!r}."
    )


# --- Deck ----------------------------------------------------------------------

def test_function_deck(pytestconfig):
    deck = make_deck()
    assert len(deck.cards) == 52, (
        f"A new Deck should hold 52 cards, but it holds {len(deck.cards)}."
    )
    values = [f"{card.suit}{card.rank}" for card in deck.cards]
    assert sorted(values) == sorted(FULL_DECK), (
        "A new Deck should hold every card of a regular deck exactly once. "
        f"These are wrong or missing: {sorted(set(values) ^ set(FULL_DECK))}"
    )
    assert not deck.is_empty(), "is_empty() should return False for a deck that still has cards."
    deck.cards = []
    assert deck.is_empty(), "is_empty() should return True for a deck without cards."


def test_function_deal_card(pytestconfig):
    deck = make_deck()
    before = [f"{card.suit}{card.rank}" for card in deck.cards]
    card = deck.deal_card()
    assert len(deck.cards) == 51, (
        f"deal_card() should take the card out of the deck, leaving 51 cards, "
        f"but the deck has {len(deck.cards)}."
    )
    value = f"{card.suit}{card.rank}"
    assert value in before, f"deal_card() returned {value!r}, which is not a card of the deck."
    assert value not in [f"{c.suit}{c.rank}" for c in deck.cards], (
        f"deal_card() returned {value!r}, but that card is still in the deck."
    )


@pytest.mark.parametrize("number", [0, 1, 5, 13])
def test_function_deal_cards(pytestconfig, number):
    deck = make_deck()
    hand = deck.deal_cards(number)
    assert len(hand) == number, (
        f"deal_cards({number}) should return {number} cards, but it returned {len(hand)}."
    )
    assert len(deck.cards) == 52 - number, (
        f"After deal_cards({number}) the deck should have {52 - number} cards left, "
        f"but it has {len(deck.cards)}."
    )
    assert len(set(f"{card.suit}{card.rank}" for card in hand)) == number, (
        f"deal_cards({number}) returned the same card more than once: {hand!r}."
    )


# --- DiscardPile ---------------------------------------------------------------

def test_function_discard_pile(pytestconfig):
    pile = call_function(__file__, "DiscardPile", [make_card("D7")])
    assert [f"{c.suit}{c.rank}" for c in pile.cards] == ["D7"], (
        f"A new DiscardPile should start with the card it was given, "
        f"but its cards are {pile.cards!r}."
    )
    assert f"{pile.top_card().suit}{pile.top_card().rank}" == "D7", (
        f"top_card() should return the card on top (D7), but it returned {pile.top_card()!r}."
    )
    assert pile.current_suit == "D", (
        f"The current suit of a pile started with D7 should be 'D', "
        f"but it is {pile.current_suit!r}."
    )


def test_function_add(pytestconfig):
    pile = make_pile("D7")
    with capture_outputs([]) as output:
        pile.add(make_card("S7"), "S")
    assert output.capture() == "", (
        f"add() should only put the card on the pile, "
        f"but it printed {output.capture()!r}."
    )
    assert f"{pile.top_card().suit}{pile.top_card().rank}" == "S7", (
        f"After add(S7, 'S') the top card should be S7, but it is {pile.top_card()!r}."
    )
    assert pile.current_suit == "S", (
        f"After add(S7, 'S') the current suit should be 'S', but it is {pile.current_suit!r}."
    )


def test_function_add_eight(pytestconfig):
    pile = make_pile("D7")
    with capture_outputs([]) as output:
        pile.add(make_card("S8"), "H")
    assert output.capture() == "", (
        f"Choosing a new suit after an 8 is up to play_turn: add() should not "
        f"ask the player anything, but it printed {output.capture()!r}."
    )
    assert f"{pile.top_card().suit}{pile.top_card().rank}" == "S8", (
        f"After add(S8, 'H') the top card should be S8, but it is {pile.top_card()!r}."
    )
    assert pile.current_suit == "H", (
        f"add(card, suit) should store the suit it is given as the current suit. "
        f"After add(S8, 'H') it should be 'H', but it is {pile.current_suit!r}."
    )


def test_function_refill_deck(pytestconfig):
    pile = make_pile("S7", below=["D3", "H9", "CK"])
    deck = make_deck([])
    pile.refill_deck(deck)
    assert [f"{c.suit}{c.rank}" for c in pile.cards] == ["S7"], (
        f"refill_deck() should leave only the top card on the pile, "
        f"but the pile holds {pile.cards!r}."
    )
    assert sorted(f"{c.suit}{c.rank}" for c in deck.cards) == ["CK", "D3", "H9"], (
        f"refill_deck() should put the other cards back into the deck, "
        f"but the deck holds {deck.cards!r}."
    )


# --- Player --------------------------------------------------------------------

def test_function_player_name(pytestconfig):
    player = make_player("Alice", ["H7"])
    assert player.name == "Alice", (
        f"A Player should keep the name it was given in its 'name' attribute, "
        f"but player.name is {player.name!r}."
    )


@pytest.mark.parametrize(
    "looking_for,found",
    [("H7", True), ("C10", True), ("S3", False), ("H10", False), ("D", False)]
)
def test_function_find_card(pytestconfig, looking_for, found):
    player = make_player("Alice", ["H7", "C10", "DK"])
    card = player.find_card(looking_for)
    if found:
        assert card is not None, (
            f"find_card({looking_for!r}) should return the card, but it returned None."
        )
        assert f"{card.suit}{card.rank}" == looking_for, (
            f"find_card({looking_for!r}) returned {card!r} instead."
        )
    else:
        assert card is None, (
            f"The player does not have {looking_for!r}, so find_card({looking_for!r}) "
            f"should return None, but it returned {card!r}."
        )


def test_function_play_turn(pytestconfig):
    player = make_player("Alice", ["H7", "S3"])
    deck = make_deck(["D4"])
    pile = make_pile("HK")
    with capture_outputs(["h7"]) as output:
        player.play_turn(deck, pile)
    assert output.capture() == turn_text("HK", "H", ["H7", "S3"], "h7"), (
        f"Playing a card that matches should end the turn. Got:\n{output.capture()}"
    )
    assert [f"{c.suit}{c.rank}" for c in player.cards] == ["S3"], (
        f"The played card should be gone from the hand, but it holds {player.cards!r}."
    )
    assert f"{pile.top_card().suit}{pile.top_card().rank}" == "H7", (
        f"The played card should be on the discard pile, but its top card is {pile.top_card()!r}."
    )
    assert pile.current_suit == "H", (
        f"After playing H7 the current suit should be 'H', but it is {pile.current_suit!r}."
    )


@pytest.mark.parametrize(
    "value,top,expected",
    [("S9", "H9", "S"), ("D7", "C7", "D")]  # same rank, other suit
)
def test_function_play_turn_changes_suit(pytestconfig, value, top, expected):
    player = make_player("Alice", [value, "H3"])
    deck = make_deck(["D4"])
    pile = make_pile(top)
    with capture_outputs([value.lower()]) as output:
        player.play_turn(deck, pile)
    assert output.capture() == turn_text(top, top[0], [value, "H3"], value.lower()), (
        f"Playing a card with the same rank should end the turn. Got:\n{output.capture()}"
    )
    assert pile.current_suit == expected, (
        f"Playing {value} on {top} changes the suit that has to be matched, so the "
        f"current suit should be {expected!r}, but it is {pile.current_suit!r}."
    )


def test_function_play_turn_rejects(pytestconfig):
    player = make_player("Alice", ["H7", "S3"])
    deck = make_deck(["D4"])
    pile = make_pile("HK")
    with capture_outputs(["d9", "s3", "h7"]) as output:
        player.play_turn(deck, pile)
    expected = (
        turn_text("HK", "H", ["H7", "S3"], "d9", NOT_IN_HAND)
        + turn_text("HK", "H", ["H7", "S3"], "s3", NO_MATCH)
        + turn_text("HK", "H", ["H7", "S3"], "h7")
    )
    assert output.capture() == expected, (
        f"A card the player doesn't have and a card that doesn't match should both be "
        f"refused, after which the player may try again. Got:\n{output.capture()}"
    )


def test_function_play_turn_draws(pytestconfig):
    player = make_player("Alice", ["H7"])
    deck = make_deck(["D4", "C2"])
    pile = make_pile("HK")
    with capture_outputs(["d"]) as output:
        player.play_turn(deck, pile)
    assert output.capture() == turn_text("HK", "H", ["H7"], "d", drew("Alice")), (
        f"Typing 'd' should draw a card and end the turn. Got:\n{output.capture()}"
    )
    assert len(player.cards) == 2, (
        f"After drawing, the player should hold 2 cards, but they hold {player.cards!r}."
    )
    assert len(deck.cards) == 1, (
        f"After drawing, the deck should have 1 card left, but it has {len(deck.cards)}."
    )


def test_function_play_turn_refills_the_deck(pytestconfig):
    player = make_player("Alice", ["H7"])
    deck = make_deck(["D4"])
    pile = make_pile("SK", below=["D3", "H9"])
    with capture_outputs(["d"]) as output:
        player.play_turn(deck, pile)
    assert [f"{c.suit}{c.rank}" for c in pile.cards] == ["SK"], (
        f"Drawing the last card of the deck should refill it from the discard pile, "
        f"leaving only the top card there. The pile holds {pile.cards!r}."
    )
    assert sorted(f"{c.suit}{c.rank}" for c in deck.cards) == ["D3", "H9"], (
        f"The cards of the discard pile should be back in the deck, "
        f"but the deck holds {deck.cards!r}."
    )


def test_function_play_turn_eight(pytestconfig):
    player = make_player("Alice", ["H8", "S3"])
    deck = make_deck(["D4"])
    pile = make_pile("CK")
    with capture_outputs(["h8", "d"]) as output:
        player.play_turn(deck, pile)
    assert output.capture() == turn_text("CK", "C", ["H8", "S3"], "h8",
                                         SUIT_PROMPT + "d\n"), (
        f"Playing an 8 should ask the player which suit they want. Got:\n{output.capture()}"
    )
    assert pile.current_suit == "D", (
        f"After choosing 'd', the current suit should be 'D', but it is {pile.current_suit!r}."
    )


# --- Scoreboard ----------------------------------------------------------------

def make_scoreboard():
    return call_function(__file__, "Scoreboard", [str(scores_file())])


SCOREBOARD_FILES = {
    "regular": ("Alice:3\nBob:1\n", {"Alice": 3, "Bob": 1}),
    "more than 9 wins": ("Alice:12\nBob:100\nCarol:7\n", {"Alice": 12, "Bob": 100, "Carol": 7}),
    "no newline at the end": ("Alice:3\nBob:1", {"Alice": 3, "Bob": 1}),
    "empty (nobody won yet)": ("", {}),
    "names that start the same": ("Al:2\nAlice:5\n", {"Al": 2, "Alice": 5}),
}


@pytest.mark.parametrize("content,scores", list(SCOREBOARD_FILES.values()), ids=list(SCOREBOARD_FILES))
def test_function_get_number_of_wins(pytestconfig, content, scores):
    with restore_files(__file__, SCORES):
        scores_file().write_text(content, encoding="utf-8")
        scoreboard = make_scoreboard()
        for name in list(scores) + ["Carol", "Bo", "Alic", "alice"]:
            expected = scores.get(name, 0)
            result = scoreboard.get_number_of_wins(name)
            assert result == expected, (
                f"With {SCORES} containing {content!r}, get_number_of_wins({name!r}) "
                f"should return {expected}, but it returned {result!r}."
            )


def test_function_add_win(pytestconfig):
    with restore_files(__file__, SCORES):
        scores_file().write_text(START_OF_FILE, encoding="utf-8")
        scoreboard = make_scoreboard()

        scoreboard.add_win("Alice")
        assert scoreboard.get_number_of_wins("Alice") == 4, (
            f"Alice had 3 wins, so after add_win('Alice') she should have 4, "
            f"but she has {scoreboard.get_number_of_wins('Alice')}."
        )
        scoreboard.add_win("Carol")
        assert scoreboard.get_number_of_wins("Carol") == 1, (
            f"Carol was not on the scoreboard yet, so after add_win('Carol') she should "
            f"have 1 win, but she has {scoreboard.get_number_of_wins('Carol')}."
        )
        scoreboard.add_win("Carol")
        assert scoreboard.get_number_of_wins("Carol") == 2, (
            f"After a second add_win('Carol') she should have 2 wins, "
            f"but she has {scoreboard.get_number_of_wins('Carol')}."
        )
        assert scoreboard.get_number_of_wins("Bob") == 1, (
            "Adding a win for one player should leave the others alone, "
            f"but Bob now has {scoreboard.get_number_of_wins('Bob')} wins."
        )


def test_function_add_win_from_nine_to_ten(pytestconfig):
    with restore_files(__file__, SCORES):
        scores_file().write_text("Alice:9\n", encoding="utf-8")
        scoreboard = make_scoreboard()
        scoreboard.add_win("Alice")
        assert scoreboard.get_number_of_wins("Alice") == 10, (
            f"Alice had 9 wins, so after add_win('Alice') she should have 10, "
            f"but she has {scoreboard.get_number_of_wins('Alice')}."
        )


@pytest.mark.parametrize("content,scores", list(SCOREBOARD_FILES.values()), ids=list(SCOREBOARD_FILES))
def test_function_save(pytestconfig, content, scores):
    with restore_files(__file__, SCORES):
        scores_file().write_text(content, encoding="utf-8")
        scoreboard = make_scoreboard()
        scoreboard.add_win("Alice")
        scoreboard.add_win("Dave")
        scoreboard.save()
        expected = dict(scores)
        expected["Alice"] = expected.get("Alice", 0) + 1
        expected["Dave"] = expected.get("Dave", 0) + 1
        assert read_scoreboard() == expected, (
            f"save() should write the whole scoreboard back to {SCORES} in the same "
            f"'name:wins' format. The file now holds:\n{scores_file().read_text()}"
        )
        reread = make_scoreboard()
        for name, wins in expected.items():
            assert reread.get_number_of_wins(name) == wins, (
                "A Scoreboard should be able to read back the file that save() wrote, "
                f"but after reading it again, {name} has {reread.get_number_of_wins(name)} "
                f"wins instead of {wins}."
            )


# --- the whole game ------------------------------------------------------------

@pytest.mark.parametrize("seed,game,final_scores", GAMES,
                         ids=["3 players", "2 players", "4 players", "win with an 8"])
def test_function_script(pytestconfig, seed, game, final_scores):
    with restore_files(__file__, SCORES):
        scores_file().write_text(START_OF_FILE, encoding="utf-8")
        expected = build_expected(game, seed)
        random.seed(seed)
        run_script(__file__, game, expected)
        assert read_scoreboard() == final_scores, (
            f"When the program ends, {SCORES} should hold the win of this game's winner: "
            f"{final_scores}. The file holds:\n{scores_file().read_text()}"
        )
