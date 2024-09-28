import pytest
import sys
sys.path.append('/Desktop/python_learning/python/python_code/hardway/Day-6/space_game')
from ex48.room import Room

def test_room():
    room = Room("Test Room", "This is a test room.")
    assert room.name == "Test Room"
    assert room.description == "This is a test room."
    assert room.paths == {}

def test_room_paths():
    central_hub = Room("Central Hub", "You are in the central hub.")
    engine_room = Room("Engine Room", "You are in the engine room.")
    central_hub.add_paths({'south': engine_room})
    assert central_hub.go('south') == engine_room
    assert central_hub.go('north') is None
