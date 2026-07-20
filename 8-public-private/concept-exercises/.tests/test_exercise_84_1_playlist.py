from p1_util.tests.test_util import call_function, run_script

import pytest

def test_function(pytestconfig):
    playlist = call_function(__file__, "Playlist", ["Road Trip"])
    assert playlist.name == "Road Trip", f"Expected name 'Road Trip', got {playlist.name!r}"
    assert playlist.get_songs() == [], f"A new playlist should have no songs, got {playlist.get_songs()!r}"

def test_function_add_songs_in_order(pytestconfig):
    playlist = call_function(__file__, "Playlist", ["Road Trip"])
    playlist.add_song("Hey Jude")
    playlist.add_song("Let It Be")
    playlist.add_song("Yesterday")
    expected = ["Hey Jude", "Let It Be", "Yesterday"]
    result = playlist.get_songs()
    assert result == expected, f"Songs should be returned in the order they were added.\nExpected: {expected}\nResult: {result}"

def test_function_returns_copy(pytestconfig):
    playlist = call_function(__file__, "Playlist", ["Road Trip"])
    playlist.add_song("Hey Jude")
    playlist.add_song("Let It Be")

    songs = playlist.get_songs()
    songs.pop(0)
    result = playlist.get_songs()
    assert result == ["Hey Jude", "Let It Be"], (
        f"Changing the list returned by get_songs() should not change the playlist itself.\n"
        f"Expected: ['Hey Jude', 'Let It Be']\nResult: {result}"
    )

    assert playlist.get_songs() is not playlist.get_songs(), (
        "get_songs() should return a new copy of the list every time it is called"
    )
