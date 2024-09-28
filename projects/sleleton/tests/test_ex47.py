import pytest
import sys
sys.path.append('/home/keeran/Desktop/python_learning/python/python_code/hardway/projects/sleleton')
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom", "This room has gold in it you can grab. There's a door to the north.")
    assert gold.name == "GoldRoom"
    assert gold.paths == {}

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")
    
    center.add_paths({'north': north, 'south': south})
    assert center.go('north') == north
    assert center.go('south') == south

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up or explore further.")
    up = Room("Up", "If you go up, there is a lion waiting for you.")
    gold = Room("Gold", "Finally, you arrive in the gold room. Take as much as you can.")
    lion = Room("Kill", "Take a gun and kill the lion.")
    
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start, 'gold': gold, 'lion': lion})  
    up.add_paths({'down': down})
    lion.add_paths({'lion': lion})
    
    
    assert start.go('west') == west
    assert start.go('west').go('east') == start  
    assert start.go('down') == down  
    assert down.go('gold') == gold  
    
 

