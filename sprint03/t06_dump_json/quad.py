# https://www.programiz.com/python-programming/json
# https://pynative.com/python-json-dumps-and-dump-for-json-encoding/
# https://www.programiz.com/python-programming/examples/quadratic-roots


# How to create a JSON string from a Python dict?
# How to make a JSON string indented?
# What's the difference between json.dump() and json.dumps() ?
# What is a quadratic equation?
# Why can't 'a' be zero in a quadratic equation?
# How to tell how many real solutions a quadratic equation will have from the value of the discriminant?
# How to check if a value is one of several data types with a single call to isinstance() ?
# How to round a number to a certain number of decimal places?

#How to create a JSON string from a Python dict?
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

#How to make a JSON string indented? (pretty print JSON)
# import json
# 
# person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
# 
# # Getting dictionary
# person_dict = json.loads(person_string)
# 
# # Pretty Printing JSON string back
# print(json.dumps(person_dict, indent = 4, sort_keys=True))

#What's the difference between json.dump() and json.dumps() ?
# json.dump() = write Python serialized object as JSON formatted data into a file.
# json.dumps() = encodes any Python object into JSON formatted String

#What is a quadratic equation?
# An equation where the highest exponent of the variable (usually "x") is a square
# equation: ax² + bx + c = 0  (a, b and c are real numbers and a ≠ 0)
# solution formula: (-b±√(b²-4ac))/(2a) or (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

#Why can't 'a' be zero in a quadratic equation?
# it becomes a line bx + c, and no longer a quadratic

#Example: Solve the quadratic equation ax**2 + bx + c = 0
# # import complex math module
# import cmath
# 
# a = 1
# b = 5
# c = 6
# 
# # calculate the discriminant
# d = (b**2) - (4*a*c)
# 
# # find two solutions
# sol1 = (-b-cmath.sqrt(d))/(2*a)
# sol2 = (-b+cmath.sqrt(d))/(2*a)
# 
# print('The solution are {0} and {1}'.format(sol1,sol2))

#How to tell how many real solutions a quadratic equation will have from the value of the discriminant?
# d = (b**2) - (4*a*c)
# if d > 0 (2 real solutions)
# if d = 0 (1 real solution)
# if d < 0 (imaginary solution)

## How to check if a value is one of several data types with a single call to isinstance() ?
# https://www.guru99.com/type-isinstance-python.html
# syntax: isinstance(object, classtype)
# example: 
# age = isinstance(51,int)
# output: True

#How to round a number to a certain number of decimal places?
# value = 5.34343
# rounded_value = round(value, 2)
# output: 5.34


# pretty print info about quad equation. "indent=3"

# def quad(a):
#     v1=isinstance(a,int) and isinstance(a,float)
#     v2=isinstance(b,int) and isinstance(b,float)
#     v3=isinstance(c,int) and isinstance(c,float)
#     #isinstance(a,float)
#     #isinstance(b,float)
#     #isinstance(c,float)
#     a == 0
#     error = 'Cannot generate a quadratic eqaution.'

import json
import cmath
def quad(a,b,c):
    # validate the argument
    v1 = isinstance(a,int) or isinstance(a,float)
    v2 = isinstance(b,int) or isinstance(b,float)
    v3 = isinstance(c,int) or isinstance(c,float)
     
    if a == 0:
        return 'Cannot generate a quadratic eqaution.'
    elif v1 and v2 and v3:
        equation = "{0}x^2+{1}x+{2}=0".format(a,b,c)

        # calculate the discriminant
        d = float((b**2) - (4*a*c))

        # define solution condition, if d > 0: find 2 solutions, if d == 0: find 1 solution.
        if d > 0:
            sol1 = (-b-cmath.sqrt(d))/(2*a) 
            sol2 = (-b+cmath.sqrt(d))/(2*a)
            m = sol1.real
            n = sol2.real

            # make solution a dictionary
            solution = {"discriminant": d, "x": [m,n]}

        elif d == 0:
            sol = (-b /(2*a))
            m = sol.real 

            # make solution a dictionary
            solution = {"discriminant": d, "x": m}

        else:
            solution = {"discriminant": d, "x": 'null'}

        # add all key values to main dictionary object
        quad_dict = {}
        quad_dict['equation'] = equation
        quad_dict['solution1'] = solution

        # print in json
        return json.dumps(quad_dict, indent = 3)

    else:
        return 'Cannot generate a quadratic eqaution.'



# reference:
# how to print out real and imaginary numbers
# https://stackoverflow.com/questions/24592803/separate-real-and-imaginary-part-of-a-complex-number-in-python
# https://www.geeksforgeeks.org/python-output-formatting/
# https://docs.python.org/3/tutorial/inputoutput.html
# https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3

