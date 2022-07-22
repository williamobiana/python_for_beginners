# What is a dict in Python?
# https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3
# The dictionary is Python’s built-in mapping type. 
# dictionaries map "keys" to "values" and these key-value pairs 
# ...provide a useful way to store data in Python.


# Accessing Data Items with Keys
# Because dictionaries offer key-value pairs for storing data,
# ...we can isolate a key in the dictionary and get its related value

# sammy = {'value': 'sammy-shark', 'online': True, 'followers': 987}
# sammy['value']
# output:
# 'sammy-shark'

## or

# car = {"brand": "Ford", "model": "Mustang", "year": 1964}
# x = car.get("model")
# print(x)
# output:
# Mustang

## if you tried to access a missing key in this way, 
# sammy = {'value': 'sammy-shark', 'online': True, 'followers': 987}
# sammy['no key like this']
# output:
# Traceback ... KeyError: 'no key like this'


# What is the advantage of using the method get() ?
# the get method does offer the advantage of not raising the Traceback 'KeyError' exception 
# ...when the specified key isn't in the dataary
# sammy = {'value': 'sammy-shark', 'online': True, 'followers': 987}
# x = sammy.get('no key like this')
# print(x)
# output:
# None


# What data types can be keys in a dict ?
# Strings, numbers, and tuples work as keys, and any type can be a value. 
# (strings and tuples work cleanly since they are immutable)


# define the function with 3 arguments
# https://www.geeksforgeeks.org/python-dictionary/


def search_cookbook(cookbook, recipe, section):
    error_statement_1 = f'There is no {recipe} recipe in the cookbook.'
    error_statement_2 = f'There is no section {section} in the {recipe} recipe.'

    if recipe in cookbook.keys():
        reci = cookbook.get(recipe)
        if section in reci.keys():
            sect = reci.get(section)
            return sect
        else:
            return error_statement_2
    else:
       return error_statement_1        





# so i dont get confused, i spread out the question
# i defined the cookbook dataary
# cookbook = {'recipe': {'section': 'section_value'}}
# 
# i searched for the recipe with .get() and made it a variable, so i can call it
# recipe = cookbook.get('recipe')

# i searched for the section with .get() and made it a variable, so i can call it
# section = recipe.get('section')

# mistakes i made:
#1. i defined the cookbook and while running, it conflicted with the script's coookbook definition
#2. using print in the if/else statement always printed the value of None as well.
#3. Not changing the name for the variable made the return statement print out the value of the argument
