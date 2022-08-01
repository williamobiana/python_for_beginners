# What is a regular expression in Python?
# How to write regexes in Python?
# What module do you need to work with regular expressions?
# What functions does the module contain to search for a match in a string? 
# How is their work different?
# What are metacharacters?
# What is character escaping? Where can you need it?
# What is the difference between + and * in regex?
# What are anchors in regex? And what are the anchors for the start and end of a string?
# ref: https://realpython.com/regex-python/

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# Python has a module named 're' to work with RegEx. # re means regular expression
# eg: re.match(), re.search(), re.findall(), re.split(), re.sub()
# 
# import re
# 
# pattern = '^a...s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string)
# 
# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	
#
# METACHARACTERS
# Metacharacters are characters that are interpreted in a special way by a RegEx engine.
# eg: [] . ^ $ * + ? {} () \ |
# [] specifies a set of characters you wish to match.
# [abc] will match if the string you are trying to match contains any of the a, b or c
# you can invert the character set by using ^ symbol at the start of []
# [^abc] means any character except a or b or c
# [^0-9] means any non-digit character.
#
# . matches any single character (except newline '\n')
# ^ checks if a string starts with a certain character
# $ checks if a string ends with a certain character
# * matches 0 or more occurrences of the pattern left to it
# + matches 1 or more occurrences of the pattern left to it
# ? matches zero or one occurrence of the pattern left to it
#
# {} matches an explicitly specified number of repetitions
# {n,m} means at least n, and at most m repetitions of the pattern left to it
# [0-9]{2, 4} matches at least 2 digits but not more than 4 digits
# 
# | is used for alternation (or operator)
# () is used to group sub-patterns
#
# \ is used to ESCAPE various metacharacters 
# \$a match if a string contains $ followed by a. Here, $ is not interpreted as a regex bcus of \
# 
# ANCHORS (special sequences):
# https://www.programiz.com/python-programming/regex
# \A - Matches if the specified characters are at the start of a string
# \b - Matches if the specified characters are at the beginning or end of a word.
# \B - Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.
# \d - Matches any decimal digit. Equivalent to [0-9]
# \D - Matches any non-decimal digit. Equivalent to [^0-9]
# \s - Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v]
# \S - Matches where a string contains any non-whitespace character. Equivalent to [^ \t\n\r\f\v]
# \w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]...
# ... here _ is also considered an alphanumeric character.
# \W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]
# \Z - Matches if the specified characters are at the end of a string
#
#



# ukraine = '\w+'
# comma = '.'
# space = '\s'
# city = '\w*.\w*'  # using a wild character, to sub for \s and '-'
# street_name = '\w*.\w*'
# building_number = '\d{1,6}'
# index = '\d{5}'

import re

def check_address(myDict):
    regex = '\w+.\s\w*.\w*.\s\w*.\w*\s\d{1,6}.\s\d{5}'
    myList = []
    for key, value in myDict.items():
        match = re.search(regex, value)
        if match:
            myList.append(f'the address of {key} is valid.')
        else:
            myList.append(f'the address of {key} is invalid.')
    return myList









