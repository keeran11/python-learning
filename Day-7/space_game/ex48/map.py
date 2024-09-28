
from room import Room

def create_game_map():
    control_room = Room("Control Room", "You are in the spaceship's control room.")
    engine_room = Room("Engine Room", "The ship's engines are here. It's noisy and hot.")
    cargo_bay = Room("Cargo Bay", "A large bay filled with crates.")
    alien_room = Room("Alien Lair", "A dark room with an alien creature.")
    treasure_room = Room("Treasure Room", "A chamber filled with alien artifacts.")
    escape_pod = Room("Escape Pod", "A small pod to escape the ship.")

   
    control_room.add_paths({'south': engine_room, 'east': cargo_bay})
    engine_room.add_paths({'north': control_room, 'down': alien_room})
    cargo_bay.add_paths({'west': control_room, 'down': treasure_room})
    alien_room.add_paths({'up': engine_room, 'escape': escape_pod})
    treasure_room.add_paths({'up': cargo_bay})

    return control_room  
