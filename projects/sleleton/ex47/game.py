class Room(object):
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.paths = {}
        self.items = items or []

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def test_room(self, gold):
        self.gold = gold
        
        
        


if __name__ == "__main__":
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
    
    
    current_room = start
    while True:
        print(f"You are in the {current_room.name}.")
        print(current_room.description)
        print(f"Available exits: {', '.join(current_room.paths.keys())}")
        
        command = input("What do you want to do? (type 'quit' to exit) ").strip().lower()
        
        if command == 'q':
            break
        
        if command not in current_room.paths:
            print("Invalid command. Available directions are: " + ", ".join(current_room.paths.keys()))
            continue
        
        next_room = current_room.go(command)
        if next_room:
            current_room = next_room
        else:
            print("You can't go that way.")
