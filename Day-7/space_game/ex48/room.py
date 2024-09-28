class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def add_paths(self, paths):
        """Add possible directions and their corresponding rooms."""
        self.paths.update(paths)

    def go(self, direction):
        """Go in a direction if the path exists."""
        return self.paths.get(direction, None)
    def escape(self):
        print("You have chosen to escape the game. Goodbye!")
        exit()  