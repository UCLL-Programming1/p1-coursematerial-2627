import random

from p1_util.tests.test_util import call_function, capture_outputs, run_script

import pytest

SEED = 17
SUITS = ["H", "D", "C", "S"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
FULL_DECK = [suit + rank for suit in SUITS for rank in RANKS]

PROMPT = "Play card or draw (D): > "
SUIT_PROMPT = "Choose suit (H D C S): > "
NOT_IN_HAND = "You don't have this card in your hand, play again\n"
NO_MATCH = "The card you want to play doesn't match the suit nor rank of the top card\n"
DREW = "Player drew a card\n"


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


def make_player(values):
    return call_function(__file__, "Player", [[make_card(value) for value in values]])


def values(cards):
    return [f"{card.suit}{card.rank}" for card in cards]


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


def deal_the_same_cards():
    """Rebuild the deal the program gets from random.seed(SEED): the deck is
    built in the same order and every card is drawn with the same randrange
    call, so the test knows exactly which cards end up where."""
    rng = random.Random(SEED)
    deck = list(FULL_DECK)

    def draw(number=1):
        return [deck.pop(rng.randrange(len(deck))) for _ in range(number)]

    return deck, draw


def make_pile(top, below=()):
    """A discard pile with `top` face-up. The pile does not keep track of the
    current suit yet, so play_turn is told what it is."""
    pile = call_function(__file__, "DiscardPile", [make_card(top)])
    pile.cards = [make_card(value) for value in below] + [make_card(top)]
    return pile


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
    result = card.is_playable(make_card(top), current_suit)
    assert result == expected, (
        f"With {top} on top of the discard pile and {current_suit} as the current suit, "
        f"{value}.is_playable({top}, {current_suit!r}) should be {expected}, "
        f"but it returned {result!r}."
    )


# --- Player.find_card ----------------------------------------------------------

@pytest.mark.parametrize(
    "looking_for,found",
    [("H7", True), ("C10", True), ("S3", False), ("H10", False), ("D", False)]
)
def test_function_find_card(pytestconfig, looking_for, found):
    player = make_player(["H7", "C10", "DK"])
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


# --- Player.play_turn ----------------------------------------------------------

def test_function_play_turn(pytestconfig):
    player = make_player(["H7", "S3"])
    deck = make_deck(["D4"])
    pile = make_pile("HK")
    with capture_outputs(["h7"]) as output:
        result = player.play_turn(deck, pile, "H")
    assert output.capture() == turn_text("HK", "H", ["H7", "S3"], "h7"), (
        f"Playing a card that matches should end the turn. Got:\n{output.capture()}"
    )
    assert values(player.cards) == ["S3"], (
        f"The played card should be gone from the hand, but it holds {player.cards!r}."
    )
    assert values(pile.cards) == ["HK", "H7"], (
        f"The played card should be on top of the discard pile, "
        f"but the pile holds {pile.cards!r}."
    )
    assert result == "H", (
        f"play_turn should return the suit that has to be matched from now on. "
        f"After playing H7 that is 'H', but it returned {result!r}."
    )


@pytest.mark.parametrize(
    "value,top,expected",
    [("S9", "H9", "S"), ("D7", "C7", "D")]  # same rank, other suit
)
def test_function_play_turn_changes_suit(pytestconfig, value, top, expected):
    player = make_player([value, "H3"])
    deck = make_deck(["D4"])
    pile = make_pile(top)
    with capture_outputs([value.lower()]) as output:
        result = player.play_turn(deck, pile, top[0])
    assert output.capture() == turn_text(top, top[0], [value, "H3"], value.lower()), (
        f"Playing a card with the same rank should end the turn. Got:\n{output.capture()}"
    )
    assert values(pile.cards) == [top, value], (
        f"The played card should be on top of the discard pile, "
        f"but the pile holds {pile.cards!r}."
    )
    assert result == expected, (
        f"Playing {value} on {top} changes the suit that has to be matched, so "
        f"play_turn should return {expected!r}, but it returned {result!r}."
    )


def test_function_play_turn_rejects(pytestconfig):
    player = make_player(["H7", "S3"])
    deck = make_deck(["D4"])
    pile = make_pile("HK")
    with capture_outputs(["d9", "s3", "h7"]) as output:
        player.play_turn(deck, pile, "H")
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
    player = make_player(["H7"])
    deck = make_deck(["D4", "C2"])
    pile = make_pile("HK")
    with capture_outputs(["d"]) as output:
        result = player.play_turn(deck, pile, "H")
    assert output.capture() == turn_text("HK", "H", ["H7"], "d", DREW), (
        f"Typing 'd' should draw a card and end the turn. Got:\n{output.capture()}"
    )
    assert len(player.cards) == 2, (
        f"After drawing, the player should hold 2 cards, but they hold {player.cards!r}."
    )
    assert len(deck.cards) == 1, (
        f"After drawing, the deck should have 1 card left, but it has {len(deck.cards)}."
    )
    assert result == "H", (
        f"Drawing a card does not change the suit that has to be matched, so play_turn "
        f"should return 'H', but it returned {result!r}."
    )


def test_function_play_turn_refills_the_deck(pytestconfig):
    player = make_player(["H7"])
    deck = make_deck(["D4"])
    pile = make_pile("SK", below=["D3", "H9"])
    with capture_outputs(["d"]) as output:
        player.play_turn(deck, pile, "S")
    assert values(pile.cards) == ["SK"], (
        f"Drawing the last card of the deck should put the cards of the discard pile "
        f"back into the deck, leaving only the top card there. "
        f"The pile holds {pile.cards!r}."
    )
    assert sorted(values(deck.cards)) == ["D3", "H9"], (
        f"The cards of the discard pile should be back in the deck, "
        f"but the deck holds {deck.cards!r}."
    )


def test_function_play_turn_eight(pytestconfig):
    player = make_player(["H8", "S3"])
    deck = make_deck(["D4"])
    pile = make_pile("CK")
    with capture_outputs(["h8", "d"]) as output:
        result = player.play_turn(deck, pile, "C")
    assert output.capture() == turn_text("CK", "C", ["H8", "S3"], "h8",
                                         SUIT_PROMPT + "d\n"), (
        f"Playing an 8 should ask the player which suit they want. Got:\n{output.capture()}"
    )
    assert result == "D", (
        f"After playing an 8 and choosing 'd', play_turn should return 'D', "
        f"but it returned {result!r}."
    )


# --- a single turn of the whole program ----------------------------------------

def test_function_script(pytestconfig):
    _, draw = deal_the_same_cards()
    hand = draw(5)
    draw(5)
    pile = draw(1)
    expected = (
        "Player 1 Turn!\n"
        + turn_text(pile[0], pile[0][0], hand, "h3", NOT_IN_HAND)
        + turn_text(pile[0], pile[0][0], hand, "ca", NO_MATCH)
        + turn_text(pile[0], pile[0][0], hand, "c8", SUIT_PROMPT + "S\n")
    )
    random.seed(SEED)
    run_script(__file__, ["h3", "ca", "c8", "S"], expected)
