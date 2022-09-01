# How does the method filter() work?
# What are the requirements for the function that is passed to filter() ?
# What happens if you pass None instead of a function to filter() ?
# Does filter() modify an iterable in-place, or return the result?
# How to check if a value is of a certain data type?
# Why does this expression isinstance(False, int) return True?

# https://www.programiz.com/python-programming/methods/built-in/filter
# The filter() function extracts elements from an iterable (list, tuple etc.) 
# ... for which a function returns True.
# example:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# returns True if number is even
# def check_even(number):
#     if number % 2 == 0:
#           return True  
# 
#     return False
# 
# Extract elements from the numbers list for which check_even() returns True
# even_numbers_iterator = filter(check_even, numbers)
# 
# 
# converting to list
# even_numbers = list(even_numbers_iterator)
# 
# print(even_numbers)
# 
# Output: [2, 4, 6, 8, 10]
##############################################
# Filter() Syntax:
# filter(function, iterable)
# 
# The filter() function takes two arguments:
#   function - function should be defined (lambda can be used)
#   iterable - list, tuple
#
# When 'None' is used as the function for the filter(), 
# all elements that are true values (gives True if converted to boolean) are extracted.
# example:
# random_list = [1, 'a', 0, False, True, '0']
# 
# filtered_iterator = filter(None, random_list)
# 
# #converting to list
# filtered_list = list(filtered_iterator)
# 
# print(filtered_list)
# Output: [1, 'a', True, '0']
#
# filter() extracts and returns result from an iterable, it doesn not modify an iterable in-place



# To check value of a certain data type, we use type() and isinstance()
#
######### Type() #########
# type() helps you find the class type of the variable given as input
# 
# example:
# str = 'Hello world'
# type(str)
# output: <class 'str'>

######### Isinstance() ##########
# isinstance() takes in two arguments, and it returns true 
# ... if the first argument is an instance of the classinfo given as the second argument
# 
# syntax:
# isinstance(object, classtype)
# object: An object whose instance you are comparing with classtype. 
#         It will return true if the type matches otherwise false.
# classtype: A type or a class or a tuple of types and/or classes
#
# example:
# age = isinstance(51,int)
# print(age)
# output: True
#
# Note: the operation isinstance(False, int) returns True,
# because a boolean is a subclass of interger
# IDE example:
# >>> int.__subclasses__()
# [<type 'bool'>]


####### Difference Between type() and isinstance() ##########
# type(): helps you find the class type of the variable given as input
#         The return value is a type object
#
# isinstance(): compares the value with the type given
#               The return value is a Boolean i.e true or false.



######## TASK #######
# Create a script with a function extractor() 
# that filters a dictionary according to a certain data type of the values. 
#
# It takes two arguments: 
# a dictionary extractable and 
# a data type value_type (an instance of class type , e.g., int, bool, etc). 
# value_type has the default value of str.
#
# The function uses filter() to create a new dictionary that only contains the items from
# extractable that have a value of type value_type .

def extractor(extractable, value_type=str):
    filtered = {}
    for key, value in extractable.items():
        filter = isinstance(value, value_type)
        if filter == True:
            filtered[key] = value
    return filtered
    

