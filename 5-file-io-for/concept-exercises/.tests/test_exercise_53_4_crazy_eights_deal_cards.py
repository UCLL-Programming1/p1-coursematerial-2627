import ast
from pathlib import Path

from p1_util.tests.test_util import call_function, get_script_dir

import pytest

SUITS = ["H", "D", "C", "S"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
FULL_DECK = [suit + rank for suit in SUITS for rank in RANKS]


def loops_in(function_name):
    """The kinds of loop used anywhere inside one function of the student's script."""
    script = get_script_dir(__file__) / Path(__file__).name[len("test_"):]
    tree = ast.parse(script.read_text(encoding="utf-8"), filename=str(script))
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            return [type(child).__name__ for child in ast.walk(node)
                    if isinstance(child, (ast.For, ast.While))]
    raise AssertionError(
        f"\n❌ No function named '{function_name}' was found in {script.name}.\n")


def test_function(pytestconfig):
    loops = loops_in("deal_cards")
    assert "While" not in loops, (
        "deal_cards still uses a while loop. Rewrite it with a for loop instead."
    )
    assert "For" in loops, (
        "deal_cards should use a for loop to do its repetition, "
        "but no for loop was found in it."
    )


@pytest.mark.parametrize("number", [0, 1, 5, 52])
def test_function_deal_cards(pytestconfig, number):
    deck = list(FULL_DECK)
    hand = call_function(__file__, "deal_cards", [deck, number], expected_output="")
    assert len(hand) == number, (
        f"deal_cards(deck, {number}) should return {number} cards, "
        f"but it returned {len(hand)}: {hand!r}."
    )
    assert len(deck) == len(FULL_DECK) - number, (
        f"After deal_cards(deck, {number}) the deck should have "
        f"{len(FULL_DECK) - number} cards left, but it has {len(deck)}."
    )
    assert sorted(hand + deck) == sorted(FULL_DECK), (
        "The dealt cards and the cards left in the deck should together "
        "make up the full deck again."
    )
