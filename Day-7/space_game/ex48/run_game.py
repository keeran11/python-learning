import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from map import create_game_map 


if __name__ == "__main__":
    current_room = create_game_map()

    while True:
        print(f"\nYou are in {current_room.name}")
        print(current_room.description)
        print(f"Available exits: {', '.join(current_room.paths.keys())}")
        # direction = input("Which way would you like to go? ")
        command = input("which way would you like to go? (type 'quit' to exit) ").strip().lower()

        direction = command
        if command == 'q':
            break
        if command not in current_room.paths:
            print("Invalid command. Available directions are: " + ", ".join(current_room.paths.keys()))
            continue
        next_room = current_room.go(direction)

        if next_room:
            current_room = next_room
        else:
            print("You can't go that way!")
