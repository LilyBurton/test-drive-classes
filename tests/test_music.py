from lib.music import MusicTracker
import pytest
"""
Adds tracks to a list and return as a list
"""
def test_music_tracker():
    music_tracker = MusicTracker()
    music_tracker.add("Macarena")
    music_tracker.add("Running Up That Hill")
    music_tracker.add("You've got a friend in me")
    
def test_music_tracker_error():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as err:
        music_tracker.add("")
        assert str(err.value) == "No music track"