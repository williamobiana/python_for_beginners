# Exercise Script (create a calculator script, using knowledge from previous modules)

print('==== Simple calculator ====')
print('Lets add some numbers')

first_value = input('Input your frist value: ')
a = float(first_value)

operator = input('Input your operator: ')

second_value = input('Input your second value: ')
b = float(second_value)

output = "usage: the operator must be '*' or '+' or '-' or '/'"

if operator == '+':
    compute = float(a + b)
    print(f'{a} + {b} = {compute}')
elif operator == '-':
    compute = float(a - b)
    print(f'{a} - {b} = {compute}')
elif operator == '*':
    compute = float(a * b)
    print(f'{a} * {b} = {compute}')
elif operator == '/':
    compute = float(a / b)
    print(f'{a} / {b} = {compute}')
else:
    print(output)

print('==== Simple calculator ====')