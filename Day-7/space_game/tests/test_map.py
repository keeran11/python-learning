import sys
sys.path.append('/Desktop/python_learning/python/python_code/hardway/Day-6/space_game')
from ex48.map import create_game_map

def test_game_map():
    start_room = create_game_map()
    

    assert start_room.go('south').name == "Engine Room"
    assert start_room.go('east').name == "Cargo Bay"
    assert start_room.go('south').go('down').name == "Alien Lair"
    

    cargo_bay = start_room.go('east')
    assert cargo_bay.go('down').name == "Treasure Room"
    
    
    alien_room = start_room.go('south').go('down')
    assert alien_room.go('escape').name == "Escape Pod"
