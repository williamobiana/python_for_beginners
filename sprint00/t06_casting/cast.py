# Casting is useful in programming by converting 1 data-type to another, and ensure a function... 
# ...handles the variables correctly.
# Implicit conversions is where the python interpreter converts 1 data-type to another automatically...
# ...example: converting converting interger calculations to float.
# Explicit conversions is when you tell it to do so.

# Exercise script
a = 3
b = 10
c = -14.8
d = True

print('Avalaible varaibles:')
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(f'd = {d}')

print()

print('Result:')
result = f'{a} + {b}'
print(result,'=', float(a+b))

result = f'{c} - {b}'
print(result, '=', int(c-b))

result = f'{c} + {b}'
print(result, '=', str(c) + str(b))

result = f'{a} - {a}'
print(result, '=', bool(a-a)) 
