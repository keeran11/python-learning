class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


if __name__ == "__main__":
    # Example of creating rooms and navigating
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    
    start.add_paths({'west': west})
    west.add_paths({'east': start})
    
    # Simple game loop
    current_room = start
    while True:
        print(f"You are in the {current_room.name}.")
        print(current_room.description)
        command = input("What do you want to do? (type 'quit' to exit) ").strip().lower()

        if command == 'quit':
            break
        
        next_room = current_room.go(command)
        if next_room:
            current_room = next_room
        else:
            print("You can't go that way.")
