#is-A , Has-A, objects , and classes
'''A class is a bulueprint or template for\
      creating objects.it defines a dataype by 
      bunding data and methods that operate on the data
'''
# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
    
#     def start_engine(self):
#         print(f"The {self.make} {self.model}'s engine is starting!")


'''Objects:
an object  is an instance of a class. Once a class is defined you can create instance of that class, which are known as objects
Each object can have unique attributes, but they are created using the same class blueprint



'''
# my_car = Car("Toyota", "camry")
# my_car.start_engine()


'''\
    is-A relationship (inheritance):
   The Is-A relationship comes from inheritance in OOP. It means that a subclass is a specialized version of a superclass. 
   The subclass inherits properties and behaviors from the superclass. 
   This relationship is represented as SubClass Is-A SuperClass.
    
    '''
# class Vehicle:
#     def __init__(self, name):
#         self.name = name

# class Car(Vehicle):  # Car is-a Vehicle
#     def start_engine(self):
#         print(f"The {self.name}'s engine is starting!")

# my_car = Car("Honda Accord")
# my_car.start_engine()  # Outputs: "The Honda Accord's engine is starting!"


'''
 Has-A Relationship (Composition or Aggregation)
 The Has-A relationship is about composition or aggregation. 
 It means that a class contains (or has) one or more objects of other classes as part of its state.
    where one object has another as an attribute.
'''
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Car has-a Engine
    
    def start_engine(self):
        print(f"The {self.make} {self.model} with {self.engine.horsepower} HP is starting!")

engine = Engine(250)
my_car = Car("Mazda", "CX-5", engine)
my_car.start_engine()  # Outputs: "The Mazda CX-5 with 250 HP is starting!"

'''
classes defines the blueprint for objects.
objects are instance of classes.
is -A defines inheritance between a subclass and a superclass.
Has-A defines composition or aggregation, where one class contains another as a component.
'''

'''unterstanding the instance'''\

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# Creating instances of the class Dog
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Each instance has its own data
print(dog1.name)  # Outputs: Buddy
print(dog2.breed)  # Outputs: Bulldog

# Both instances can use the bark method
dog1.bark()  # Outputs: Buddy is barking!
dog2.bark()  # Outputs: Max is barking!

'''dog1 and dog2 are instances of the Dog class. They represent individual dogs with their own names and breeds.
Even though they share the same class (template), each instance has unique values for their attributes (name and breed in this case).
Instances can interact with the methods defined by the class (bark() method here).'''

'''A regular function is defined outside of a class.'''
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("kiran"))  # Outputs: "Hello, Alice!"


'''method
a method is defined inside a class and operate on instacces(objects) of that class.
'''
class Person:
    def __init__(self, name):
        self.name = name

    # This is a method because it's defined inside a class
    def greet(self):
        return f"Hello, {self.name}!"

# Creating an instance (object) of the Person class
person1 = Person("kiran")

# Calling the greet method on the instance
print(person1.greet())  # Outputs: "Hello, kiran!"
