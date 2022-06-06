# error types in python: 
# https://www.tutorialsteacher.com/python/error-types-in-python
# https://docs.python.org/3/tutorial/errors.html
# https://docs.python.org/3/library/exceptions.html

# common types of error:
# NameError: Shown when an object could not be found.
# TypeError: Shown when an operation or function is applied to an object of an inappropriate type. 
# ValueError: Shown when a function's argument is of an inappropriate type.
# etc..

# As errors could be fatal, 
# recover gracefully from unexpected errors.  
# error handling is one of the crucial areas for application designers and developers

# 'Try' and 'Execpt' can be used instead of a traceback error.
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.

# a ValueError is shown when a function's argument is of an inappropriate type.
# we can handle it using a "try" and "execpt ValueError"
# try:
#     print(math.sqrt(-1))
# except ValueError: #you can choose to indicate the specific error type if you choose
#     print('Note')

def patoi(arg):
    try:
        value = int(arg)
        return value
    except:
        return False