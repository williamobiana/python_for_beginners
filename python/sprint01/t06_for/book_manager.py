# A "for" loop is used for iterating over a sequence
# unlike the "while" loop, the "for" loop does not require an indexing variable to set beforehand.
# example:
# for x in "banana":
#   print(x)
#
# The difference between "for" loop and "while" loop is that in "for" loop the number of iterations 
# ... to be done is already known and is used to obtain a certain result 
# whereas in "while" loop the command runs until a certain condition is reached and the statement 
# ...is proved to be false.
#
# typical example of using for loop without index
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
# print(x)
# 
# output:
# apple
# banana
# cherry
# 
# to use for loop with index, read the link:
# https://www.pythontutorial.net/python-basics/python-for-loop-list/
#
# The range() Function:
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, 
# ...and increments by 1 (by default), and ends at a specified number.
# example:
# for x in range(6):
#   print(x)
#
# output:
# 0
# 1
# 2 
# 3
# 4 
# 5 #note the values 0 to 5 (but not including 6)
#
# however it is possible to specify the starting value by adding a parameter: range(2, 6), 
# ... which means values from 2 to 6 (but not including 6):
# exmaple:
# for x in range(2, 6):
#   print(x)
#
# output:
# 2
# 3
# 4
# 5
#
# The range() function defaults to increment the sequence by 1, however 
# ... it is possible to specify the increment value by adding a third parameter: range(2, 10, 3):
# example: Increment the sequence with 3
# for x in range(2, 10, 3):
#   print(x)
#
# output:
# 2
# 5
# 8


def get_anonymous(books):
    empty_book_list = []
    for book_title in books:
        if ' by ' in book_title:
            continue
        empty_book_list.append(book_title)
    return empty_book_list


# the main challenge i faced was "indentation" of the return function
# and understanting that i had to create a new variable list
# and append the book_title to.        
        
        


