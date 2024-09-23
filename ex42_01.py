'''understanding the relationship in details'''
#animal is- object
class Animal(object):
    pass

##Dog is a subclass of animal
class Dog(Animal):
    #The __init__ method initializes an instance of the Dog class with a name attribute, so each Dog object will have a name when created.
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        #persion has a name a pet
        self.name = name
        self.pet = None


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass
#almon and halibut are fish
#Salmon is-a Fish
class Salmon(Fish):
    pass
#Halibut is-a Fish.
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet named satan
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 120000)


# frank has-a pet named rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
