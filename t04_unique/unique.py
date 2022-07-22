# How to create a dictionary of lists?
# How to iterate over the values of a dictionary?
# How to get unique values from a list?
# How can the set() function help you get a unique list?

# Getting unique values in a list simply means to remove the duplicate values
# eg:
# numbers = [1, 1, 2, 3, 3, 4]
# unique_numbers = [1, 2, 3, 4]  #desired result


# Creating a dictionary
# dictionaries map "keys" to "values"
# dict = {'a': 'b'}
# a = key, b = value
# 
# Creating a dictionary of list
# List are unhashable and cannot be added to dictionary directly.
# Using substring
# # Creating an empty dictionary
# myDict = {}
#   
# Adding list as value
# myDict['a'] = [1, 2, 3]
# myDict['b'] = ['four', 'five']
#    
# print(myDict)

# Loop/iterate over the key, values of a dictionary?
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for key, value in my_dict.items():
#     print(f'{key}: {value}')
#
# Loop/iterate over the keys of a dictionary?
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for key in my_dict.keys():
#     print(key)
#
# Loop/iterate over the values of a dictionary?
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for value in my_dict.values():
#     print(value)

# How to get unique values from a list?
# using transversal method
# using set
# using numpy
# using collections.counter
# https://www.geeksforgeeks.org/python-get-unique-values-list/
#
# function to get unique values using set
# list1 = [10, 20, 10, 30, 40, 40]
# def unique(list1):
#  
#     # insert the list to the set
#     list_set = set(list1)
#     # convert the set to the list
#     unique_list = (list(list_set))
#     for x in unique_list:
#         print(x)
# 
# unique(list1)
#
#
# function to get unique values using set
# list1 = [1, 2, 2, 3, 3, 4, 5]
# def unique(list1):
#     unique_list = []
#     unique_number = set(list1)
#     for x in unique_number:
#         unique_list.append(x)
#     return unique_list
# 
# print(unique(list1))
# 
## OR for a shorter approach
#
# numbers = [1, 2, 2, 3, 3, 4, 5]
# unique_numbers = list(set(numbers))
# print(unique_numbers)
# 
# additional ref: https://www.freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array/



def make_unique(myDict):
    formatted_dict = {} #create a new dictionary to store the modified values
    for key, value in myDict.items(): #use a loop to run through the myDict key:value pairs
        unique_value = sorted(list(set(value)))  #make values unique and sort it  
        formatted_dict[key] = unique_value   #add the key and unique values to the empty dict
    
    return formatted_dict





