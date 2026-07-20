from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "destination,distance_km,miles",
    [
        ("Paris", 300, 186.4),
        ("Berlin", 650, 403.9),
        ("Amsterdam", 180, 111.8),
    ]
)
def test_function(pytestconfig, destination, distance_km, miles):
    trip = call_function(__file__, "Trip", [destination, distance_km])
    assert trip.destination == destination, f"Expected destination {destination!r}, got {trip.destination!r}"
    assert trip.distance_km == distance_km, f"Expected distance_km {distance_km!r}, got {trip.distance_km!r}"

    result = trip._to_miles()
    assert result == miles, f"Trip({destination!r}, {distance_km})._to_miles() - Expected: {miles}, Result: {result}"

@pytest.mark.parametrize(
    "destination,distance_km,miles",
    [
        ("Paris", 300, 186.4),
        ("Berlin", 650, 403.9),
    ]
)
def test_function_display(pytestconfig, capsys, destination, distance_km, miles):
    trip = call_function(__file__, "Trip", [destination, distance_km])
    trip.display()
    expected = f"Trip to {destination}: {distance_km} km / {miles} miles\n"
    actual = capsys.readouterr().out
    assert actual == expected, f"display() output mismatch.\nExpected: {expected!r}\nResult: {actual!r}"
