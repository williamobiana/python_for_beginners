#python conditions are logic used in "if statements" and loops
#comparison/relational operators are the math operators (==, >, <, >=, <=, !=)
#writing an if statement
#  x = 2
#  if x < 2:
#      print('less')
# elif (else if) can be used depending on the logic and its optional in an "if statement"
# else ends the "if statement"
#  x = 2
#  if x < 2:
#      print('less')
#  else:
#      print('more')

#Example of how to get the INPUT statement for strings and use (if) statement in Python
#Message = input("Enter Your Message: ") 
#if Message=="Hello": 
#	print("Hi!") 
#else: 
#	print("Bye") 


question = input('There are 3 signs in front of you. Which one would you like to read? ')
right = 'The right sign says: "DEAD PEOPLE ONLY"'
left = 'The left sign says: "BEWARE!"'
middle = 'The middle sign says: "CERTAIN DEATH"'
output = (f'There is no {question} sign')

if question == "right":
    print(right)
elif question == "left":
    print(left)
elif question == "middle":
    print(middle)
else:
    print(output)
