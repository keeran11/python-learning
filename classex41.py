# class MyExplicitClass(object):
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"MyExplicitClass with name: {self.name}"

# # Create an instance
# obj = MyExplicitClass("Test")

# # Checking the object methods inherited from the 'object' class
# print(dir(obj))

# # Using the inherited __str__ method from 'object', which can be overridden
# print(obj)  # Output: MyExplicitClass with name: Test

#  Assigning a Class to a Variable
# You can assign a class to a variable and use that variable to create instances of the class.
class MyClass:
    def greet(self):
        return "Hello from MyClass"

# Assigning the class to a variable
MyClassAlias = MyClass

# Using the alias to create an instance
obj = MyClassAlias()
print(obj.greet())  # Output: Hello from MyClass


# 2. Passing a Class to a Function
# A class can be passed as an argument to a function, which can then create instances of the class or invoke class methods.


def create_instance(class_obj):
    return class_obj()

# Passing the class as an argument
instance = create_instance(MyClass)
print(instance.greet())  # Output: Hello from MyClass


# 3. Storing Classes in Data Structures
# Classes can be stored in data structures such as lists or dictionaries, making it easy to create instances dynamically.
class MyClass1:
    def greet(self):
        return "Hello from MyClass1"

class MyClass2:
    def greet(self):
        return "Hello from MyClass2"

# Storing classes in a list
classes = [MyClass1, MyClass2]

# Creating instances dynamically
for class_obj in classes:
    instance = class_obj()
    print(instance.greet())

# Output:
# Hello from MyClass1
# Hello from MyClass2


# 4. Returning Classes from Functions
# A function can return a class, allowing for dynamic class selection.

def choose_class(choice):
    if choice == 1:
        return MyClass1
    else:
        return MyClass2

# Using the function to get a class and create an instance
ChosenClass = choose_class(1)
instance = ChosenClass()
print(instance.greet())  # Output: Hello from MyClass1

# 5. Calling Class Methods Directly
# You can also treat the class itself as an object and call class methods (like classmethods or staticmethods) directly without creating an instance.
class MyClassWithStaticMethod:
    @staticmethod
    def static_greet():
        return "Hello from a static method"

# Calling the static method on the class without instantiating it
print(MyClassWithStaticMethod.static_greet())  # Output: Hello from a static method


'''In Python, classes are objects themselves, which means you can manipulate them just like any other object.
You can pass classes as arguments to functions, return them from functions, store them in collections, and assign them to variables.
This flexibility is a key feature of Python's dynamic and powerful object-oriented programming model.'''