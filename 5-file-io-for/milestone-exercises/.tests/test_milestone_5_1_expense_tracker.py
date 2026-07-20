from p1_util.tests.test_util import run_script, get_script_dir, restore_files

import pytest

MENU = (
    "(A) Add expense\n"
    "(L) List expenses\n"
    "(T) Total spent\n"
    "(C) Category total\n"
    "(H) Highest expense\n"
    "(E) Exit\n"
)
PROMPT = "What do you want to do? > "
EXIT = PROMPT + "E\nAll expenses have been saved.\n"
START = "Food,15\nTransport,4\nFood,8\nGames,20\n"


@pytest.mark.parametrize(
    "inputs,file_content,expected_output,expected_file",
    [
        # total
        (
            ["T", "E"],
            START,
            PROMPT + "T\n"
            "You spent 47 euros in total.\n",
            START,
        ),
        # category total
        (
            ["C", "Food", "E"],
            START,
            PROMPT + "C\n"
            "Which category? > Food\n"
            "You spent 23 euros on Food.\n",
            START,
        ),
        # a category without any expenses
        (
            ["C", "Books", "E"],
            START,
            PROMPT + "C\n"
            "Which category? > Books\n"
            "You spent 0 euros on Books.\n",
            START,
        ),
        # highest expense (the last one in the file)
        (
            ["H", "E"],
            START,
            PROMPT + "H\n"
            "The highest expense is Games: 20 euros.\n",
            START,
        ),
        # highest expense (the first one in the file)
        (
            ["H", "E"],
            "Rent,500\nFood,15\nGames,20\n",
            PROMPT + "H\n"
            "The highest expense is Rent: 500 euros.\n",
            "Rent,500\nFood,15\nGames,20\n",
        ),
        # adding and listing; the added expense is saved when exiting
        (
            ["A", "Books", "12", "L", "E"],
            START,
            PROMPT + "A\n"
            "What category? > Books\n"
            "What amount? > 12\n"
            "Expense added.\n"
            + PROMPT + "L\n"
            "Food: 15\n"
            "Transport: 4\n"
            "Food: 8\n"
            "Games: 20\n"
            "Books: 12\n",
            START + "Books,12\n",
        ),
        # added expenses count for the total, the category total and the highest expense
        (
            ["A", "Food", "5", "T", "C", "Food", "A", "Car", "300", "H", "E"],
            START,
            PROMPT + "A\n"
            "What category? > Food\n"
            "What amount? > 5\n"
            "Expense added.\n"
            + PROMPT + "T\n"
            "You spent 52 euros in total.\n"
            + PROMPT + "C\n"
            "Which category? > Food\n"
            "You spent 28 euros on Food.\n"
            + PROMPT + "A\n"
            "What category? > Car\n"
            "What amount? > 300\n"
            "Expense added.\n"
            + PROMPT + "H\n"
            "The highest expense is Car: 300 euros.\n",
            START + "Food,5\nCar,300\n",
        ),
        # starting from an empty file
        (
            ["L", "T", "A", "Books", "12", "H", "E"],
            "",
            PROMPT + "L\n"
            + PROMPT + "T\n"
            "You spent 0 euros in total.\n"
            + PROMPT + "A\n"
            "What category? > Books\n"
            "What amount? > 12\n"
            "Expense added.\n"
            + PROMPT + "H\n"
            "The highest expense is Books: 12 euros.\n",
            "Books,12\n",
        ),
        # exiting right away still saves the (unchanged) expenses
        (
            ["E"],
            START,
            "",
            START,
        ),
    ]
)
def test_function(pytestconfig, inputs, file_content, expected_output, expected_file):
    script_dir = get_script_dir(__file__)

    with restore_files(__file__, "expenses.txt"):
        with open(script_dir / "expenses.txt", "w") as file:
            file.write(file_content)

        run_script(__file__, inputs, MENU + expected_output + EXIT)

        with open(script_dir / "expenses.txt") as file:
            content = file.read()

        assert content == expected_file, (
            f"After exiting, expenses.txt should contain:\n{expected_file!r}\n"
            f"but it contains:\n{content!r}"
        )
