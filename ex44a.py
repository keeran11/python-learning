'''Inheritance is used to indicate that one class will get most or all of its features from a parent class.'''
# #implicit inheritance
# class Parent(object):
#     def implicit(self):
#         print("parent implict()")

# class Child(Parent):
#     pass

# dad =Parent()
# son = Child()

# dad.implicit()
# son.implicit()


# #override Explicitly
# class Parent(object):
#     def Override(self):
#         print("parent override()")

# class Child(Parent):
#     def Override(self):
#         print("child override()")

# dad =Parent()
# son = Child()

# dad.Override()
# son.Override()


#Alter Before or After
# here we use built in funciton called super()

# class Parent(object):
#     def altered(self):
#         print("parent altered()")

# class Child(Parent):
#     def altered(self):
#         print("child , before parent altered()")
#         super(Child, self).altered()
        

# dad =Parent()
# son = Child()

# dad.altered()
# son.altered()



class Parent(object):
    def override(self):
        print("PARENT override()")


    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

    def altered(self):
        print ("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        # print ("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()