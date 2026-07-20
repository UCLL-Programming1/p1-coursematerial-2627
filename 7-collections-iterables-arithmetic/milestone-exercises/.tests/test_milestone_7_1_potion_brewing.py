
from p1_util.tests.test_util import call_function, run_script

import pytest


MENU = (
    "Welcome alchemist!\n"
    "Here are the actions you can perform:\n"
    "(V) View ingredients\n"
    "(A) Add ingredient to cauldron\n"
    "(C) View cauldron\n"
    "(B) Brew potion\n"
    "(Q) Quit\n"
)

INGREDIENTS = {
    "Mandrake Root": ("Nature", 5),
    "Dragon Scale": ("Fire", 8),
    "Mermaid Tear": ("Water", 6),
    "Storm Crystal": ("Electric", 7),
    "Phoenix Feather": ("Fire", 10),
    "Moon Flower": ("Nature", 4)
}

INGREDIENT_LIST = "".join(
    f"{name} ({element}) - Power {power}\n" for name, (element, power) in INGREDIENTS.items()
)


@pytest.mark.parametrize(
    "inputs,expected_output",
    [
        (
            [
                "A",
                "Dragon Scale",
                "B",
                "Q",
            ],
            MENU +
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Dragon Scale\n"
            "Ingredient added.\n"
            "What do you want to do? > B\n"
            "Potion brewed!\n"
            "Types used:\n"
            "Fire\n"
            "Total power: 8\n"
            "What do you want to do? > Q\n"
            "Goodbye, alchemist!\n"
        ),
        (
            [
                "A",
                "Dragon Scale",
                "A",
                "Moon Flower",
                "B",
                "Q",
            ],
            MENU +
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Dragon Scale\n"
            "Ingredient added.\n"
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Moon Flower\n"
            "Ingredient added.\n"
            "What do you want to do? > B\n"
            "Potion brewed!\n"
            "Types used:\n"
            "Fire\n"
            "Nature\n"
            "Total power: 12\n"
            "What do you want to do? > Q\n"
            "Goodbye, alchemist!\n"
        ),
        (
            [
                "A",
                "Dragon Scale",
                "A",
                "Dragon Scale",
                "Q",
            ],
            MENU +
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Dragon Scale\n"
            "Ingredient added.\n"
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Dragon Scale\n"
            "Ingredient was not added because it is unknown or already in the cauldron.\n"
            "What do you want to do? > Q\n"
            "Goodbye, alchemist!\n"
        ),
        (
            [
                "A",
                "Magic Bean",
                "Q",
            ],
            MENU +
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Magic Bean\n"
            "Ingredient was not added because it is unknown or already in the cauldron.\n"
            "What do you want to do? > Q\n"
            "Goodbye, alchemist!\n"
        ),
        # quitting right away
        (
            ["Q"],
            MENU +
            "What do you want to do? > Q\n"
            "Goodbye, alchemist!\n"
        ),
        # viewing the ingredients
        (
            ["V", "Q"],
            MENU +
            "What do you want to do? > V\n"
            + INGREDIENT_LIST +
            "What do you want to do? > Q\n"
            "Goodbye, alchemist!\n"
        ),
        # viewing an empty cauldron, and a cauldron with one ingredient
        (
            ["C", "A", "Moon Flower", "C", "Q"],
            MENU +
            "What do you want to do? > C\n"
            "The cauldron is empty.\n"
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Moon Flower\n"
            "Ingredient added.\n"
            "What do you want to do? > C\n"
            "Ingredients in the cauldron:\n"
            "Moon Flower\n"
            "What do you want to do? > Q\n"
            "Goodbye, alchemist!\n"
        ),
        # the types are sorted alphabetically, not in the order they were added
        (
            ["A", "Mermaid Tear", "A", "Dragon Scale", "A", "Storm Crystal", "B", "Q"],
            MENU +
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Mermaid Tear\n"
            "Ingredient added.\n"
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Dragon Scale\n"
            "Ingredient added.\n"
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Storm Crystal\n"
            "Ingredient added.\n"
            "What do you want to do? > B\n"
            "Potion brewed!\n"
            "Types used:\n"
            "Electric\n"
            "Fire\n"
            "Water\n"
            "Total power: 21\n"
            "What do you want to do? > Q\n"
            "Goodbye, alchemist!\n"
        ),
        # two ingredients of the same type: the type is only listed once
        (
            ["A", "Dragon Scale", "A", "Phoenix Feather", "B", "Q"],
            MENU +
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Dragon Scale\n"
            "Ingredient added.\n"
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Phoenix Feather\n"
            "Ingredient added.\n"
            "What do you want to do? > B\n"
            "Potion brewed!\n"
            "Types used:\n"
            "Fire\n"
            "Total power: 18\n"
            "What do you want to do? > Q\n"
            "Goodbye, alchemist!\n"
        ),
        # brewing empties the cauldron, so the same ingredient can be used again
        (
            ["A", "Dragon Scale", "B", "C", "A", "Dragon Scale", "A", "Moon Flower", "B", "Q"],
            MENU +
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Dragon Scale\n"
            "Ingredient added.\n"
            "What do you want to do? > B\n"
            "Potion brewed!\n"
            "Types used:\n"
            "Fire\n"
            "Total power: 8\n"
            "What do you want to do? > C\n"
            "The cauldron is empty.\n"
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Dragon Scale\n"
            "Ingredient added.\n"
            "What do you want to do? > A\n"
            "Which ingredient do you want to add? > Moon Flower\n"
            "Ingredient added.\n"
            "What do you want to do? > B\n"
            "Potion brewed!\n"
            "Types used:\n"
            "Fire\n"
            "Nature\n"
            "Total power: 12\n"
            "What do you want to do? > Q\n"
            "Goodbye, alchemist!\n"
        ),
    ]
)
def test_function(pytestconfig, inputs, expected_output):
    run_script(__file__, inputs, expected_output)


def test_function_show_ingredients(pytestconfig):
    call_function(__file__, "show_ingredients", [dict(INGREDIENTS)], expected_output=INGREDIENT_LIST)


def test_function_show_cauldron_empty(pytestconfig):
    call_function(__file__, "show_cauldron", [set()], expected_output="The cauldron is empty.\n")


def test_function_add_to_cauldron(pytestconfig):
    cauldron = set()
    for ingredient, expected, content in [
        ("Dragon Scale", True, {"Dragon Scale"}),
        ("Storm Crystal", True, {"Dragon Scale", "Storm Crystal"}),
        ("Dragon Scale", False, {"Dragon Scale", "Storm Crystal"}),
        ("Dragon Tooth", False, {"Dragon Scale", "Storm Crystal"}),
        ("dragon scale", False, {"Dragon Scale", "Storm Crystal"}),
    ]:
        result = call_function(__file__, "add_to_cauldron", [dict(INGREDIENTS), cauldron, ingredient])
        assert result is expected, (
            f"add_to_cauldron(ingredients, cauldron, {ingredient!r}) should return {expected}, but returned {result!r}"
        )
        assert cauldron == content, (
            f"After adding {ingredient!r}, the cauldron should be {content}, but it is {cauldron}"
        )


@pytest.mark.parametrize(
    "cauldron,types,power",
    [
        ({"Dragon Scale", "Storm Crystal"}, ["Electric", "Fire"], 15),
        ({"Mermaid Tear", "Mandrake Root", "Dragon Scale"}, ["Fire", "Nature", "Water"], 19),
        ({"Dragon Scale", "Phoenix Feather"}, ["Fire"], 18),
        ({"Moon Flower"}, ["Nature"], 4),
        (set(), [], 0),
    ]
)
def test_function_brew_potion(pytestconfig, cauldron, types, power):
    cauldron = set(cauldron)
    result = call_function(__file__, "brew_potion", [dict(INGREDIENTS), cauldron])
    assert tuple(result) == (types, power), (
        f"brew_potion should return ({types}, {power}), but returned {result!r}"
    )
    assert cauldron == set(), f"After brewing, the cauldron should be empty, but it holds {cauldron}"
