import random

from p1_util.tests.test_util import call_function, run_script

import pytest

SEED = 17
SUITS = ["H", "D", "C", "S"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
FULL_DECK = [suit + rank for suit in SUITS for rank in RANKS]


def make_card(value):
    return call_function(__file__, "Card", [value])


def make_deck():
    return call_function(__file__, "Deck", [])


def values(cards):
    return [f"{card.suit}{card.rank}" for card in cards]


def deal_the_same_cards():
    """Rebuild the deal the program gets from random.seed(SEED): the deck is
    built in the same order and every card is drawn with the same randrange
    call, so the test knows exactly which cards end up where."""
    rng = random.Random(SEED)
    deck = list(FULL_DECK)

    def draw(number=1):
        return [deck.pop(rng.randrange(len(deck))) for _ in range(number)]

    return deck, draw


# --- Card ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "value,suit,rank",
    [("DA", "D", "A"), ("C10", "C", "10"), ("H8", "H", "8"), ("SK", "S", "K")]
)
def test_function(pytestconfig, value, suit, rank):
    card = make_card(value)
    assert card.suit == suit, f"Card({value!r}).suit should be {suit!r}, got {card.suit!r}."
    assert card.rank == rank, f"Card({value!r}).rank should be {rank!r}, got {card.rank!r}."


@pytest.mark.parametrize("value", ["DA", "C10", "H8", "SK"])
def test_function_repr(pytestconfig, value):
    card = make_card(value)
    assert repr(card) == value, (
        f"A Card should be printed as {value!r}, but printing Card({value!r}) "
        f"shows {repr(card)}. Have a look at __repr__."
    )
    assert str([card]) == f"[{value}]", (
        f"A hand of cards should print as [{value}], but it printed {str([card])}."
    )


# --- Deck ----------------------------------------------------------------------

def test_function_deck(pytestconfig):
    deck = make_deck()
    assert len(deck.cards) == 52, (
        f"A new Deck should hold 52 cards, but it holds {len(deck.cards)}."
    )
    assert sorted(values(deck.cards)) == sorted(FULL_DECK), (
        "A new Deck should hold every card of a regular deck exactly once. "
        f"These are wrong or missing: {sorted(set(values(deck.cards)) ^ set(FULL_DECK))}"
    )


def test_function_deal_card(pytestconfig):
    deck = make_deck()
    before = values(deck.cards)
    card = deck.deal_card()
    assert len(deck.cards) == 51, (
        f"deal_card() should take the card out of the deck, leaving 51 cards, "
        f"but the deck has {len(deck.cards)}."
    )
    value = f"{card.suit}{card.rank}"
    assert value in before, f"deal_card() returned {value!r}, which is not a card of the deck."
    assert value not in values(deck.cards), (
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
    assert len(set(values(hand))) == number, (
        f"deal_cards({number}) returned the same card more than once: {hand!r}."
    )


# --- DiscardPile ---------------------------------------------------------------

@pytest.mark.parametrize("value", ["D7", "S10"])
def test_function_discard_pile(pytestconfig, value):
    pile = call_function(__file__, "DiscardPile", [make_card(value)])
    assert values(pile.cards) == [value], (
        f"A new DiscardPile should start with the card it was given, "
        f"but its cards are {pile.cards!r}."
    )
    top = pile.top_card()
    assert f"{top.suit}{top.rank}" == value, (
        f"top_card() should return the card on top ({value}), but it returned {top!r}."
    )


# --- Player --------------------------------------------------------------------

def test_function_player(pytestconfig):
    cards = [make_card("H7"), make_card("C10")]
    player = call_function(__file__, "Player", [cards])
    assert values(player.cards) == ["H7", "C10"], (
        f"A Player should keep the cards it was given in its 'cards' attribute, "
        f"but it holds {player.cards!r}."
    )


# --- setting up the game -------------------------------------------------------

def test_function_script(pytestconfig):
    _, draw = deal_the_same_cards()
    hand_1, hand_2, pile = draw(5), draw(5), draw(1)
    expected = (
        f"Top card: {pile[0]}\n"
        f"Top suit: {pile[0][0]}\n"
        f"Player 1 hand: [{', '.join(hand_1)}]\n"
        f"Player 2 hand: [{', '.join(hand_2)}]\n"
        f"Cards left in the deck: 41\n"
    )
    random.seed(SEED)
    run_script(__file__, [], expected)
