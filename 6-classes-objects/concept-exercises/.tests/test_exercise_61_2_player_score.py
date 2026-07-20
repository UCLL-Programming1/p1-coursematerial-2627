from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "name",
    [
        "James",
        "Alice",
    ]
)
def test_function(pytestconfig, name):
    player = call_function(__file__, "Player", [name])
    assert player.name == name, f"Expected name {name!r}, got {player.name!r}"
    assert player.score == 0, f"A new player should start with score 0, got {player.score!r}"

def test_function_update_score(pytestconfig):
    player_1 = call_function(__file__, "Player", ["James"])
    player_2 = call_function(__file__, "Player", ["Alice"])

    player_1.score += 3
    assert player_1.score == 3, f"Expected score 3 after adding 3 points, got {player_1.score!r}"
    assert player_2.score == 0, f"The score of the other player should still be 0, got {player_2.score!r}"

    player_1.score += 2
    assert player_1.score == 5, f"Expected score 5 after adding 2 more points, got {player_1.score!r}"
