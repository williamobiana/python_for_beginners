# A function is a block of code which only runs when it is called.
# You can pass data (aka parameters, aka block of code), into a function.
# A function will return data as a result.

# a function is defined using the "def" keyword
# example:
# def my_function():
#   print("Hello from a function")

# we can use file to store data and call the file with open() when we need it

# if __name__ == '__main__':
# when reading a source file, python sets the _name_ varible to have a value as _main_
# if the file is imported from another source, 
# the _name_ varible will be set to the imported source file's name 
# and the value to the imported source file's value.

# a source file is also called module.
# a module contains python definetions and statement.
# the file name is the module name with suffix ".py"
# example: 
# create file 1 called myscript.py
# def my_function():
#    print('I am an inside function')
# if __name__ == "__main__":
#     print("Executed when invoked directly")
# else:
#     print("Executed when imported")
# ---
# create file 2 test.py....excecute the command
# import myscript
# myscript.my_function()


# __file__ is a variable that contains the path to the module that is currently being imported.
# Python creates a __file__ variable for itself when it is about to import a module


# OS module is used for common path name manipulation
# to get a basename from a path name we use "os.path.basename()"

# how it happens internally, is with the os.path.split() divides the name into (heads,tails)
# os.path.basename() returns the tails part of the name.
# Example
# path = '/home/User/Documents'

# Above specified path will be splitted into (head, tail) pair as
# ('/home/User', 'Documents')

# basename = os.path.basename(path)
# print(basename)
# output: Documents

basename = __file__
def print_filename():
    print(basename)

print_filename()
