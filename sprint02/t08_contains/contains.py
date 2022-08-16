# Create a function contains() that takes a string and a list of substrings(characters in a string).
# The function checks if each substring(character) is present in the string
# and returns a list of substrings(characters) that are in the string.
# otherwise, it returns an empty list.
# the function must ignore case.

def contains(str, substr):
    newlist = []
    for char in substr:
        if char in str.casefold():
            newlist.append(char)
    return newlist
