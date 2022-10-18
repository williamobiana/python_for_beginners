# What is a decorator?
# What does a decorator take and what does it return?
# What are decorators for?
# What kind of decorators are there?
# If a decorator logs a message after a function call, and the function calls other 
# ...functions with the same decorator, what will be the order of the log messages? Would 
# ...it be different if the logging was before the function call?

# https://www.programiz.com/python-programming/decorator

# decorators are metaprograms they try to modify another part of the program at compile time.
# decorator is function that takes a function as first parameter and returns a function

# # create a function
# def ordinary():
#     print("I am ordinary")
# 
# # create a decorator function
# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
# 
# # This is similar to packing a gift with some extra goodies on the wrapper
# @make_pretty
# def ordinary():
#     print("I am ordinary")
# 
# # @make_pretty is the same as ordinary = make_pretty(ordinary)
# 
# ##### if with arguments parameters #####
# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
#         return func(a, b)
#     return inner
# 
# 
# @smart_divide
# def divide(a, b):
#     print(a/b)
# 
# #### if with multiple number of argument, and keyword arguments
# def works_for_all(func):
#     def inner(*args, **kwargs):
#         print("I can decorate any function")
#         return func(*args, **kwargs)
#     return inner
# 
# @works_for_all
# def divide(a, b):
#     print(a/b)
# 
# #### you can chain decorators ###
# 
# @smart_divide
# @works_for_all
# def divide(a, b):
#     print(a/b)
# 
# 

# create a log function decorator that print the class name and name of called function
# message should be logged on the info level to the stdout


## create a simple class
## * create a log
## define stdout function and it should
## * describe the log message on info level
## * print the log message
## define log function decorator and it should
## * call the class name 
## * call the log function name
#
#import logging
## create a class
#class Person:
#  def __init__(self, _name, _age):
#    self.name = _name
#    self.age = _age
# 
#  def say_hi(self):
#    print('Hello, my name is ' + self.name + ' and I am ' + self.age + ' years old!')
#
#    
#p = Person('Bob', '25')
#p.say_hi()
#
###################################3
#
## create a log decorator
#def log(func):
#    def class_name(*args, **kwargs):
#        print("I am the 'class.name'")
#        print("I am the 'function name'")
#        func(*args, **kwargs)
#    return class_name
#
## This is similar to packing a gift with some extra goodies on the wrapper
#@log
#def print_stdout(message):
#    
#    # basic config
#    logging.basicConfig(filename='logfile.log', format='%(asctime)s - %(message)s', level=logging.INFO)
#
#    # print log
#    #logging.info(f"{type(Person)}>: - {Person.self.name} method has been called.")
#
#print_stdout('Why hello there, I just logged a message')




import logging
import sys

# create a logger
logger = logging.getLogger()

# if logger config is not defined, then define it.
if not logger.hasHandlers():
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s %(message)s')

    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

# create a log decorator with inner functions
def log(func):
    def inner(*args):
        # call the given function
        res = func(*args)

        # print out the log message to call a class name and function 
        logger.info(f"<{type(args[0]).__name__}>: - {func.__name__} method has been called.")

        return res

    return inner

# define the cargo class
class Cargo:
    @log
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    @log
    def __str__(self):
        return f"Cargo to {self.destination} with weight {self.weight}"

    @log
    def __repr__(self):
        return f"Cargo(destination={self.destination}, weight={self.weight})"

# define the container class
class Container:
    @log
    def __init__(self, weight_limit, cargo=None):
        self.cargo = None
        self.weight_limit = weight_limit
        self.set_cargo(cargo)

    @log
    def set_cargo(self, other):
        if other and other.weight <= self.weight_limit:
            self.cargo = other
        else:
            pass

    @log
    def __str__(self):
        return f"Container up to {self.weight_limit} with {self.cargo}"

    @log
    def __repr__(self):
        return f"Container(weight_limit={self.weight_limit}, cargo={repr(self.cargo)})"

# define the ship class
class Ship:
    @log
    def __init__(self, route, containers):
        self.route = route
        self.containers = []
        self.add_containers(containers)

    @log
    def add_containers(self, conts):
        for c in conts:
            if c.cargo and c.cargo.destination in self.route:
                self.containers.append(c)

    @log
    def __str__(self):
        tmp = f"Ship to {self.route} with containers:"
        for c in self.containers:
            tmp += '\n' + str(c)
        return tmp

    @log
    def __repr__(self):
        return f"Ship(route={self.route}, containers={repr(self.containers)})"

