# What are generators
# Why and when can they be used
# What does the keyword yield mean in generators
# https://www.programiz.com/python-programming/generator

# A generator is a function that returns an object (iterator)...
# ...which we can loop over (one value at a time).

# they can be used when working with data streams or large files to prevent "MemoryError" ...
# ...since they produce data 1 at a time.

# when running generators we define our generator as a function,... 
# .. and use "yeild" statement instead of "return" to return values
# you can have multiple yield statements .

# to loop through the functions (on the python Interpreter) we use next()

# when the number of yield statments has successfully returned values,...
# ...it terminates and begin to return 'StopIteration' traceback

#eg:
#def my_gen():
#    n = 1
#    print('This is printed first')
#    yield n
#
#    n += 1
#    print('This is printed at last')
#    yield n
#
#>>> a = my_gen()
#>>> next(a)
#This is printed first
#1
#>>> next(a)
#This is printed at last
#2
#>>> next(a)
#...
#StopIteration

## USING LOOPS
# we can use loops directly in the function.
# a 'for' loop iterates the function using next() and automatically stops at StopIteration.
#def my_gen():
#    n = 1
#    print('This is printed first')
#    yield n
#
#    n += 1
#    print('This is printed at last')
#    yield n
#
#for item in my_gen():
#    print(item)

## example of a generator that reverses a string
# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length - 1, -1, -1): #gets the index in reverse order with range(start, stop, step) 
#         yield my_str[i]
# 
## For loop to reverse the string
# for char in rev_str("hello"):
#     print(char)

## Generator Expression
# The syntax for generator expression is similar to that of a list comprehension in Python. 
# But the square brackets are replaced with round parentheses.
#
# eg:
# my_list = [1, 3, 6, 10]
# 
# square each term using list comprehension
# list_ = [x**2 for x in my_list]
#
# which is the same as ....
# list_ = []
# for x in my_list:
#    list_.append(x ** 2)
#
# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
# generator = (x**2 for x in my_list)
#
# print(list_)
# print(generator)
# 
# output:
# [1, 9, 36, 100]
# <generator object <genexpr> at 0x7f5d4eb4bf50>
# 
# the print(generator) returned a generator object, which produces items only on demand.
# to start getting items from the generator we can use next()
#my_list = [1, 3, 6, 10]
#a = (x**2 for x in my_list)
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#next(a)

# Generator expressions can be used as function arguments
#print(sum(x**2 for x in my_list))
#print(max(x**2 for x in my_list))

# use of python generators
# https://www.programiz.com/python-programming/generator

## TASK
# Create a cube() generator function that takes an 'integer'(n) and 'returns' the cube (** 3) of 
# the given number as long as the passed number is greater than zero (while n > 0)
# The number decreases by one at each iteration. (n -= 1)

def cube(n):
    while n > 0:
        yield n ** 3
        n -= 1




