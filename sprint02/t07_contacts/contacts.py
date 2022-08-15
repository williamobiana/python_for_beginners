# What dictionary method removes and returns an element by a given key?
# What is a 'word character' in the context of regex?

## What dictionary method removes and returns an element by a given key?
# https://www.programiz.com/python-programming/methods/dictionary/pop
# The pop() method removes and returns an element from a dictionary having the given key.
# example: create a dictionary
# marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }
# 
# element = marks.pop('Chemistry')
# print('Popped Marks:', element)
# 
# Output: Popped Marks: 72

# Syntax of Dictionary pop():
# dictionary.pop(key[, default])
#     key - key which is to be searched for removal
#     default - value which is to be returned when the key is not in the dictionary
# The pop() method returns:
#     If key is found - removed/popped element from the dictionary
#     If key is not found - value specified as the second argument (default)
#     If key is not found and default argument is not specified - KeyError exception is raised

# Example: Pop an element from the dictionary 'random sales dictionary'
# sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
# 
# element = sales.pop('apple')
# 
# print('The popped element is:', element)
# print('The dictionary is:', sales)
#
# Output:
# The popped element is: 2
# The dictionary is: {'orange': 3, 'grapes': 4}

# Example: Pop an element not present from the dictionary 'random sales dictionary'
# sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
# 
# element = sales.pop('guava')
# 
# Output: KeyError: 'guava'

# Example: Pop an element not present from the dictionary, provided a default value
# sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
# 
# element = sales.pop('guava', 'banana')
# 
# print('The popped element is:', element)
# print('The dictionary is:', sales)
#
# Output:
# The popped element is: banana
# The dictionary is: {'orange': 3, 'apple': 2, 'grapes': 4}


## What is a 'word character' in the context of regex?
# \w (word character) matches any single letter, number or underscore (same as [a-zA-Z0-9_] )
# \W (non-word-character) matches any single character that doesn't match by \w (same as [^a-zA-Z0-9_] )


# TASK
# In this task you will be working with a dictionary of email contacts. 
# Each entry has an 'email' as the key, and a 'dictionary of personal information' as the value.
# email_contacts = {'email': {personal_information}}

# Create a script with a function contacts() that can:
#   * add a new entry to this dictionary of email contacts (or replace if exists)
#     email_contacts[key] = value
#   * update an existing entry
#     email_contacts.update({'key': 'value'})
#   * delete an existing entry
#     del email_contacts[key]

# The function takes two dictionaries and a string, and returns a boolean

# The function contacts():
#  1. takes the arguments (container, info, operation)
#       container: dictionary of email contacts (it can be empty)
#             email_contacts = {}
#             container = email_contacts
#
#       info: dictionary of personal information that
#           * contain an item with: 
#               key - 'name', 
#               value - non empty string with only word char or spaces
#               'name': '\w+\s+'
#           * contain an item with:
#               key - 'email'
#               value - non empty string that matches pattern [not `@`]@[not `@`].[not `@`]'
#               'email': '^[\w]+[\.]?[\w]+[@][\w]+[.][\w{2,3}$]'
#
#       operation: string with name of operation
#               'add' or 'update' or 'delete'
#
#  2. returns False if either the info or the operation is not valid
#       if info is not valid or operation is not valid
#           return false
#
#  3. performs an action corresponding to the given operation argument:
#       * add - add an item to the container
#           key - info dictionary email_value
#           key - '^[\w]+[\.]?[\w]+[@][\w]+[.][\w{2,3}$]'
#           value - the info dict without 'email' item
#           value - {'name': '\w+\s+'}
#           if container item key is present:
#               container.update(key)
#               return true
#
#       * update or delete - looks for a contact in container with a key matching email from info
#           if container doesnt have an item with key:
#              return false
#           else:
#              update - update the found contact (the element in the container)
#                key == email value of info 
#                * if key is not in contact:
#                       add key-value pair from info to the found contact (dont add email item from info)
#                * update the values of the element, keys are already in contact
#   
#                  For example, updating a container:
#                  'a@a.a': {'name': 'a', 'age': 25}, 'b@b.b': {'name': 'b', 'age': 37}
#       
#                  with an info :
#                  'email': 'a@a.a', 'name': 'x', 'id': '5'
#       
#                  will result in the container becoming:
#                  'a@a.a': {'name': 'x', 'age': 25, 'id': '5'}, 'b@b.b': {'name': 'b', 'age': 37}
#       
#                  Returns True after the update
#       
#               delete - removes the found contact (element in the container)
#                 key == email value of info
#                  Returns true.



# # Template
# email_contacts = {key: value}
# key = 'email'
# value = personal_info
# personal_info = {'name': 'value', 'age': 'value'}

# # Add new entry
# email_contacts['new_email'] = {'new_personal_info'}
# # Update an existing entry
# email_contacts.update({'new_email': {'updated_personal_info'}})
# # Delete an exisiting entry
# del email_contacts['new_email']

# con = {}
# inf = {'name': '\w+\s*', 'email': '[^@]+[@][^@][.][^@]'} or #'[\w]+[\.]?[\w]+[@][\w]+[.][\w]{2,3}' 
# opr = ['add', 'delete', 'update']

# Define the arguments (2 dictionaries(container, info), 1 string(operation))
import re
def contacts(con, inf, opr):
    #info
    if 'name' in inf.keys():
        name_regex = '\w+\s*'
        name_value = inf['name']
        name_match = re.search(name_regex, name_value)
    if 'email' in inf.keys():
        email_regex =  '[^@]+@[^@\.]+.[^@]+' 
        email_value = inf['email']
        email_match = re.search(email_regex, email_value)
    else:
        return False
    
    #validate
    if name_match and email_match and opr == 'add' or opr == 'update' or opr == 'delete':
        #add
        if opr == 'add':
            key = inf['email']
            inf.pop('email')
            value = inf
            con[key] = value
        #update
        if opr == 'update':
            key = inf['email']
            if key not in con.keys():
                return False
            else:
                inf.pop('email')
                con[key].update(inf)
                return True
        #delete
        if opr == 'delete':
            key = inf['email']
            if key not in con.keys():
                return False
            else:
                del con[key]
                return True  
        return True
    else:
        return False

          
  

    
    














