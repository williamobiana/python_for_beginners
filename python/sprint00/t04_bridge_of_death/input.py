# To get input from a user, you use the "input()" function 
# example:
# day = input('Time of day: ')
# print(day)

# "f-strings" or "f" are used to format a string to make string interpolation simpler
# interpolation means substituting 1 or more place-holders {} with thier assigned value
# example_1:
# val = 'python'
# print(f'{val} is awesome when writing {val} scripts')

# example_2:
# name = 'William'
# age = 29
# print(f'Hello my name is {name} and i am {age} years old')

# "\n" means newline

# Exercise Script
print('BRIDGEKEEPER: Stop.')
print('Who would cross the Bridge of Death must answer me these questions three.')

print('BRIDGEKEEPER: ')
name = input('What is your name?\n ')

print('BRIDGEKEEPER: ')
quest = input('What is your quest?\n ')

print('BRIDGEKEEPER: ')
color = input('What is your favourite color?\n ')

print('================')

print('Traveler info:')
print(f'Your name is {name}')
print(f'Your quest is {quest}')
print(f'Your favorite color is {color}')

print('================')

print('BRIDGEKEEPER: Right. Off you go.')