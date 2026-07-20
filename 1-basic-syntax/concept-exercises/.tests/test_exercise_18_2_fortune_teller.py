from p1_util.tests.test_util import run_script

import pytest

@pytest.mark.parametrize(
    "inputs,fortune",
    [
        (["Aries"], "A bold opportunity is heading your way. Say yes."),
        (["Taurus"], "Good things come to those who wait. Keep waiting."),
        (["Gemini"], "You will soon hear from an old friend. Maybe two."),
        (["Cancer"], "Trust your instincts today. Especially about lunch."),
        (["Leo"], "The spotlight is yours. Try not to trip."),
        (["Virgo"], "Perfection is overrated. Ship it."),
        (["Libra"], "A decision you've been avoiding can wait no longer."),
        (["Scorpio"], "Someone is thinking about you right now. Weird, right?"),
        (["Sagittarius"], "An adventure is closer than you think. Pack light."),
        (["Capricorn"], "Hard work pays off. Eventually. Unless your coworker is the boss's son, he will get promoted over you."),
        (["Aquarius"], "Your most original idea yet is just around the corner."),
        (["Pisces"], "Go with the flow today. The flow knows."),
        (["Ophiuchus"], "The stars do not recognise that sign. Check your spelling."),
        (["leo"], "The stars do not recognise that sign. Check your spelling."),
        ([""], "The stars do not recognise that sign. Check your spelling."),
    ]
)
def test_function(pytestconfig, inputs, fortune):
    expected_output = f"Welcome to the Fortune Teller!\n\nEnter your star sign: > {inputs[0]}\n"
    expected_output += fortune + "\n"
    run_script(__file__, inputs, expected_output)
