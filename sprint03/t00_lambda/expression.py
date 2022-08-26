# What is a lambda function in Python?
# What is another name for lambda functions and why?
# What are the main features and limitations of lambda functions?
# What is the keyword used to create a lambda function?
# What does the following expression do lambda a, b: a + b ? What will be the result if
# you pass in the values (2, 2) ?


# Lambda use declarative programming.
# declarative programming: 
# is a method that involves stating what the task or desired outcome is.
# and the logic will be perform my the program for you.

# A lambda function is a small anonymous function(function with no name) 
# that can take any number of arguments, but can only have one expression.

# Another name for Lambda function is Lambda calculus (also written as λ-calculus) 
# it is a formal system in mathematical logic for expressing computation 
# based on function abstraction and application using variable binding and substitution

# feature:
# it has no name when defining it, and it is contained in one line of code.
# limitations: 
# it can take any number of arguments; however it can contain only one statement.

# example:
# def add(a, b):
#     return a + b
# add() takes 2 argument a, b and returns it with an add operation upon invocation.
#
#  if you use a Python lambda construction, you get the following:
# lambda a, b: a + b
#
#     The keyword: lambda
#     A bound variable: a, b
#     A body: a + b
#
# example:
# if we pass a value a = 2, b = 2
#
# #####function#####
# def add(a, b):
#     return a + b
#
# #####driver code#####
# a=2
# b=2
# add(a, b)
# output:
# 4
#
# #####lambda##### 
# (lambda a, b: a + b)(2,2)
#     The keyword: lambda
#     A bound variable: a, b
#     A body: a + b
#     The value: 2, 2 (a = 2, b = 2)
# lambda 2, 2: 2 + 2
# output:
# 4
#
# 

#####task######

# function
# def reminder(n, a, b):
#     if n % a == 0 and n % b == 0:
#         print('True')
#     else:
#         print('False')

# lambda equivalent
n = int(input('n: '))
a = int(input('a: '))
b = int(input('b: '))

result = (lambda n, a, b: (n % a == 0 and n % b == 0))(n, a, b)

print(result)

