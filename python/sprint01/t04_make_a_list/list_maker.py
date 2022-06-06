# Lists are used to store multiple items in a single variable.

# strings vs list
# A string is a sequence of characters. Strings are immutable, i.e., they cannot be changed.
# A list can contain strings, integers, as well as objects.
# Lists are mutable, i.e., they can be altered once declared.

# Converting a string to list:
# using delimiters
# def Convert(string):
#     li = list(string.split(" ")) #string.split(delimiter) #delimiter for space is an empty bracket
#     return li 
# str1 = "Hi there"
# print(Convert(str1))
# 'Hi there' becomes ['Hi', 'there']

# using slicing
# def Convert(string):
#     list1=[]
#     list1[:0]=string #this means from the begining to the first letter should be a string.
#     return list1
#  Driver code
# str1="Hi there"
# print(Convert(str1))
# 'Hi there' becomes ['H', 'i', ' ', 't', 'h', 'e', 'r', 'e']

# to add/append a value to a list
# list.append(value)
# https://www.programiz.com/python-programming/methods/list/append

# to append a list in another list
# list1.append(list2) #list 2 will be inside list1

# to add 2 lists to become 1
# list1.extend(list2)

# convert list to string
# we can define a function for this
# def convert(list): 
#     str1 = "" 
#     for element in list: 
#         str1 += element #concatenate and equal to 
#     return str1        
# list = ['Geeks', 'for', 'Geeks']
# print(convert(list)) 

# we can use .join()
# def listToString(s): 
#     str1 = " " #define the string as empty
#     return (str1.join(s)) 
# s = ['Geeks', 'for', 'Geeks']
# print(listToString(s)) 
# https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/


# Getting started:
# 1. create an empty list
# list = []
# print(list)

# 2. create a list with 3 element of diff data-types, print the index 1, print the lenght of list
# list = ['Hello', 'number', 1]
# print(list[1])
# print(len(list))


def list_maker(line, delim):
    li = list(line.split(delim))
    return li
