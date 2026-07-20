from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "title,artist,duration",
    [
        ("Bohemian Rhapsody", "Queen", 354),
        ("Hey Jude", "The Beatles", 431),
        ("Blinding Lights", "The Weeknd", 200),
    ]
)
def test_function(pytestconfig, title, artist, duration):
    song = call_function(__file__, "Song", [title, artist, duration])
    assert song.title == title, f"Expected title {title!r}, got {song.title!r}"
    assert song.artist == artist, f"Expected artist {artist!r}, got {song.artist!r}"
    assert song.duration == duration, f"Expected duration {duration!r}, got {song.duration!r}"
