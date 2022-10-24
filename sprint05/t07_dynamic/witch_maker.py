# How to create a class dynamically?
# In what real-life cases would it be useful to create classes dynamically?
# How to get the name of a function?

# https://www.geeksforgeeks.org/create-classes-dynamically-in-python/

# Classes can be dynamically created using the type() function in Python
# type(object)

# type(name, bases, attributes) 
# 
# Parameters:
# name: The user defined name of the class
# bases: A list of base classes, and its type is tuple
# attributes: the data members and methods contained in the class

# Example
# constructor
# def constructor(self, arg):
#     self.constructor_arg = arg
# 
# # method
# def displayMethod(self, arg):
#     print(arg)
# 
# # class method
# @classmethod
# def classMethod(cls, arg):
#     print(arg)
# 
# # creating class dynamically
# # type(name, bases, attributes)
# Geeks = type("Geeks", (object, ), {
#     # constructor
#     "__init__": constructor,
# 
#     # data members
#     "string_attribute": "Geeks 4 geeks !",
#     "int_attribute": 1706256,        
# 
#     # member functions
#     "func_arg": displayMethod,
#     "class_func": classMethod
# })
# 
# # create objects
# obj = Geeks("constructor argument")
# print(obj.constructor_arg)
# print(obj.string_attribute)
# print(obj.int_attribute)
# 
# obj.func_arg("Geeks for Geeks")
# Geeks.class_func("Class Dynamically Created !")



class Witch:
    def __init__(self, name):
        self.name = name

def get_witch_class(class_name, specialty, skills):
    # dynamically create a class with type(name, bases, attributes)
    new_class = type(class_name, (Witch,), dict(specialty=specialty))

    #skills is a list of functions, 
    #we want to take a function and set its attributubes to the new_class as its methods
    for method in skills:
        setattr(new_class, method.__name__, method)
    return new_class





