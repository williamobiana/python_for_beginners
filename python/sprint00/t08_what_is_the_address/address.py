# Python stores object in heap memory and reference of object(variables) in stack.
# The id() function returns a unique id for the specified object. All objects in Python has its own unique id. eg: id(object).
# The output is the identity of the object passed. This is random but when running in the same program, it generates unique and same identity. 

# Example 1: This program shows one identity
# Input : id("geek")
# Output : 139793848214784

# Example 2: This program shows various identities
# str1 = "geek"
# print(id(str1))
# Output : 140252505691448

# str2 = "geek"
# print(id(str2))
# Output : 140252505691448

# print(id(str1) == id(str2))
# Output : True

# list1 = ["aakash", "priya", "abdul"]
# print(id(list1[0]))
# Output: 140252505691840
# print(id(list1[2]))
# Output: 140252505739928

#print(id(list1[0])==id(list1[2]))
# Output : True

# to check if variables are identical or not, use 'is' or '==' or '!=' to compare thier unique id 
# 'is' operator compares the identity of two objects
# '==' operator compares the values of two objects

# Exercise script
first_var = 1000
a = id(first_var)
print(f'first_var = {first_var}, address is {a}')

second_var = first_var
b = id(second_var)
print(f'second_var = {second_var}, address is {b}')

third_var = 999
c = id(third_var)
print(f'third_var = {third_var}, address is {c}')

fourth_var = third_var + 1
d = id(fourth_var)
print(f'fourth_var = {fourth_var}, address is {d}')

print(f'{first_var} is {second_var} =', bool(first_var is second_var))
print(f'{first_var} is {third_var} =', bool(first_var is third_var))
print(f'{first_var} is {fourth_var} =', bool(first_var is fourth_var))