# Arithmetic are used with numeric values to perform common mathematic operations:
# ['+', '-', '*', '/', '%', '**', '//']

# the diffrence between a division "/" and a floor division "//"
# division represnt its output in float(decimal) numbers
# floor division rounds down to the nearest whole number

# the modulus "%" can determine if a number is even or odd by dividing by 2
# 10 % 2 = 0 (10 is even)
# 9 % 2 = 1 (9 is odd)

# Execerise Script
a = input('Enter the first number: ')
b = input('Enter the second number: ')
a = int(a)
b = int(b)

c = (a + b)
print(f'{a} + {b} = {c}')

c = (a - b)
print(f'{a} - {b} = {c}')

c = (a * b)
print(f'{a} * {b} = {c}')

c = (a / b)
print(f'{a} / {b} = {c}')

c = (a % b)
print(f'{a} % {b} = {c}')

c = (a ** b)
print(f'{a} ** {b} = {c}')

c = (a // b)
print(f'{a} // {b} = {c}')