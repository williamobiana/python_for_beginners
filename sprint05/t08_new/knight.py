# What is the purpose of the method __new__() ?
# What does __new__() return?
# How to count the instances of a class?

# Constructors in Python (__init__ vs __new__)
# https://dev.to/pila/constructors-in-python-init-vs-new-2f9j

# __new__ is used when you need to control the creation of a new instance while 
# __init__ is used when you need to control the initialization of a new instance.

# In general, you shouldn't need to override __new__unless you're subclassing an immutable type like str, int, Unicode, or tuple

# Example 1: Using __init__ 
# class Point:
#     def __init__(self, data):
#         self.num = data
#     def print_num(self):
#         print(self.num)
# obj = Point(100)
# obj.print_num()

# Example 2: Using __new__
# class Person:
#     # __new__ creates a class
#     def __new__(cls):
#         return object.__new__(cls)
# 
#     # since __new__ has already created a class, we can call methods
#     def __init__(self):
#         self.instance_method()
# 
#     def instance_method(self):
#         print('success!')
# 
# personObj = Person()


# counting number of instances if a class
# https://www.geeksforgeeks.org/how-to-count-number-of-instances-of-a-class-in-python/

# class geeks:
#     
#     # this is used to print the number of instances of a class
#     counter = 0
#   
#     # Initialize the class
#     def __init__(self):
#         
#         # increment
#         geeks.counter += 1
#   
# # object or instance of geeks class
# g1 = geeks()
# g2 = geeks()
# g3 = geeks()
# print(geeks.counter)




#logger
#logger decorator
#class knight

# use __new__ to forbid instantiating the class 
# if there are already four instances made
# or if the constructor receives a named argument name with the value 'Arthur'.
# on attempts to do so, log a corresponding error message
# 
# create a log decorator,
# The decorator must log the name of the called method and the passed **kwargs in the format


import logging
import sys

logger = logging.getLogger()

if not logger.hasHandlers():
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s %(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

def log(func):
    def inner(*args, **kwargs):
        logger.info(f"{func.__name__} with {kwargs}")
        return func(*args, **kwargs)
    return inner

class Knight:
    counter = 0
    instances = []

    #create a class
    @log
    def __new__(cls, **kwargs):
        if cls.counter > 3:
            logger.error("Cannot create a Knight. The Round Table can only fit 4 Knights.")
            return None
        if kwargs.get('name') == 'Arthur':
            logger.error("Cannot create a Knight with the name Arthur. Arthur is the King.")
            return None 
        for key, value in kwargs.items():
            setattr(cls, key, value)
        
        cls.counter += 1
        return object.__new__(cls)
    
    #initialize the class
    @log
    def __init__(self, **kwargs):
        #set attribute to recieve data from dictionary
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.instances.append(self)




