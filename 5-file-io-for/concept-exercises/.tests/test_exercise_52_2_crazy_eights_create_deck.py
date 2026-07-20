import ast
from pathlib import Path

from p1_util.tests.test_util import call_function, get_script_dir

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
    loops = loops_in("create_deck")
    assert "While" not in loops, (
        "create_deck still uses a while loop. Rewrite all of its loops as for loops."
    )
    assert loops.count("For") >= 2, (
        "create_deck should still have a loop over the suits and a loop over the ranks, "
        f"both written as for loops, but the number of for loops found is {loops.count('For')}."
    )


def test_function_create_deck(pytestconfig):
    deck = call_function(__file__, "create_deck", [], expected_output="")
    assert deck == FULL_DECK, (
        f"create_deck() should return the 52 cards of a deck, suit by suit: "
        f"{FULL_DECK[:5]} ... {FULL_DECK[-3:]}. It returned {deck!r}."
    )
