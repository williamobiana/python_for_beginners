# What is JSON, and why is it useful?
# What module needs to be imported to work with JSON in Python?
# What are serialization and deserialization?
# How to load JSON data from a file? How is it different from loading from a string?
# What data type in JSON does a dict correspond to?
# What data types cannot be keys in a dict?
# How to sort a dict by values in reverse order?


# JSON (JavaScript Object Notation) is a popular data format used for representing structured data.
# It's common to transmit and receive data between a server and web application in JSON format.

# JSON exists as a string. 
# For example:
# p = '{"name": "Bob", "languages": ["Python", "Java"]}'
# It's also common to store a JSON object in a file.

######## Import json Module ##########
# we need to import the module before you can use it
# import json

######## PARSE JSON #########
######Example 1: (JSON to dict)#########
# You can parse a JSON string using json.loads() method. The method returns a dictionary.
#import json
#
#person = '{"name": "Bob", "languages": ["English", "French"]}'
#person_dict = json.loads(person)
#
#print(person_dict)
## Output: {'name': 'Bob', 'languages': ['English', 'French']}
#
#print(person_dict['languages'])
## Output: ['English', 'French']
# in the example, person is a JSON string, and person_dict is a dictionary

########Example 2: Read JSON file########
# You can use json.load() method to read a file containing JSON object
# Suppose, you have a file named person.json which contains a JSON object. 

#{"name": "Bob", 
#"languages": ["English", "French"]
#}

# Here's how you can parse this file:
# import json
# 
# with open('person.json', 'r') as f:
#   data = json.load(f)
# 
# print(data)
# Output: {'name': 'Bob', 'languages': ['English', 'French']}
# Here, we have used the open() function to read the json file. 
# Then, the file is parsed using json.load() method which gives us a dictionary named data.


######### CONVERT TO JSON STRING ##############
# You can convert a dictionary to JSON string using json.dumps() method.
########Example 3: Convert dict to JSON############
# import json
# 
# person_dict = {'name': 'Bob',
# 'age': 12,
# 'children': None
# }
# person_json = json.dumps(person_dict)
# 
# print(person_json)
# Output: {"name": "Bob", "age": 12, "children": null}

# Python objects and their equivalent conversion to JSON
# dict = object	
# list, tuple = array		
# str = string		
# int, float, int = number		
# True = true		
# False = false		
# None = null


####### WRITING JSON TO A FILE ##########
# To write JSON to a file in Python, we can use json.dump() method.
##########Example 4: Writing JSON to a file#############
# import json
# 
# person_dict = {"name": "Bob",
# "languages": ["English", "French"],
# "married": True,
# "age": 32
# }
# 
# with open('person.txt', 'w') as json_file:
#   json.dump(person_dict, json_file)
# Here, we have opened a file named person.txt in writing mode using 'w'. 
# If the file doesn't already exist, it will be created. 
# Then, json.dump() transforms person_dict to a JSON string which will be saved in the person.txt file

######### PRETTY PRINT JSON ##########
# To analyze and debug JSON data, we may need to print it in a more readable format
# This can be done by passing additional parameters 'indent' and 'sort_keys' to json.dumps() and json.dump() method.
#########Example 5: Python pretty print JSON###########
# import json
# 
# person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
# 
# # Getting dictionary
# person_dict = json.loads(person_string)
# 
# # Pretty Printing JSON string back
# print(json.dumps(person_dict, indent = 4, sort_keys=True))
# 
# the Output will be:
# {
#     "languages": "English",
#     "name": "Bob",
#     "numbers": [
#         2,
#         1.6,
#         null
#     ]
# }
# Here, we used 4 spaces for indentation. And, the keys are sorted in ascending order
# By default the value of indent is None. And, the default value of sort_keys is False.


# Note:
# The process of converting JSON object to string is called serialization
# The process of converting string to JSON object is called deserialization
# Nested dictionarys and lists cannot be keys in a dictionary

# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# 
# A dictionary item contains a k:v pair, which is 2 indexes 0, 1
# lambda (argument):(return)
#
# sort_by_key = dict(sorted(x.items(),key=lambda item:item[0]))
# sort_by_value = dict(sorted(x.items(), key=lambda item:item[1]))
# reverse_sort_by_value = dict(sorted(x.items(), key=lambda item:item[1], reverse=True))
#
# print("sort_by_key:", sort_by_key)
# print("sort_by_value:", sort_by_value)
# print("reverse_sort_by_value:", reverse_sort_by_value)


####### TASK #######
import json
from collections import Counter
def summary(filename, summarize_by):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            for k,v in data.items():
                if summarize_by in k:
                    value = dict(Counter(v))
                    summary_dict = dict(sorted(value.items(), key=lambda x:x[1], reverse=True))
                    return summary_dict


            for k,v in data.items():
                if summarize_by not in k:
                    a=[]
                    data.setdefault(summarize_by)
                    a.append(data[summarize_by])
                    value = dict(Counter(a))
                    summary_dict = dict(sorted(value.items(), key=lambda x:x[1], reverse=True))
                    return summary_dict

    except:
        print('Error in decoding JSON.')
        






    









