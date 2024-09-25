#object oriented programming
'''The process is as follows:
1.Write or draw about the problem.
2.Extract key concepts from #1 and research them.
3.Create a class hierarchy and object map for the concepts.
4.Code the classes and a test to run them.
5.Repeat and reﬁne.'''


'''* Map
- next_scene
- opening_scene
* Engine
- play
* Scene
- enter
* Death
* Central Corridor
* Laser Weapon Armory
* The Bridge
* Escape Pod'''

from sys import exit

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('escape_pod')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            
            if next_scene_name is None:
                print(f"Error: No scene returned from {current_scene}. Exiting game.")
                break

            current_scene = self.scene_map.next_scene(next_scene_name)

           
            if current_scene is None:
                print(f"Error: Scene '{next_scene_name}' not found. Exiting game.")
                break
            

       
        current_scene.enter()
class Death(Scene):
    def enter(self):
        print("You died. Game over!")
        return 'finished'
    
class Finished(Scene):
    def enter(self):
        print("The game is over. Thanks for playing!")
        return 0

class CentralCorridor(Scene):
    def enter(self):
        print("You're in the Central Corridor. A Gothon is blocking your way!")
        print("What do you do?")
        print("1. Shoot the Gothon")
        print("2. Tell a joke")

        action = input("> ")

        if action == "1":
            print("The Gothon shoots you back. You died.")
            return 'death'
        elif action == "2":
            print("The Gothon laughs, and you sneak by!")
            return 'laser_weapon_armory'
        
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print("You've entered the Laser Weapon Armory.")
        print("You need the code to unlock the bomb. The code is 3 digits.")
        print("hint:there is a virus which afect you")
        code = "143"
        guess = input("[keypad]> ")

        if guess == code:
            print("you are correct , you are smarter then me")
            print("You got the bomb!")
            return 'the_bridge'
        else:
            print("Wrong code! The alarms go off.")
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print("You're on the bridge with the bomb.")
        print("What do you do?")
        print("1. Place the bomb")
        print("2. Throw the bomb at the Gothons")

        action = input("> ")

        if action == "1":
            print("You placed the bomb and now need to escape!")
            return 'escape_pod'
        else:
            print("The bomb explodes, and you die.")
            return 'finished'

class EscapePod(Scene):
    def enter(self):
        print("You've reached the escape pods. Choose one to escape!")
        print("There are 5 pods. Which one do you take?")

        good_pod = "3"
        guess = input("[pod #]> ")

        if guess == good_pod:
            print("You escaped safely! You win!")
            return 'finished'
        else:
            print("The pod explodes. You died.")
            return 'death'

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
