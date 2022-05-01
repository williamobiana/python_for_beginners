# to unbind an object (variable, function, class, etc.)
# use the keyword "del", or use slicing [:] at the end of the object, or change the value so it nolonger holds reference

# in the interpreter, run the command help('keywords') to get a list of keywords
# to get more information on a particular keyword, run the command with the keyword you need. eg: help('del')

my_number = 1
print(my_number)
del(my_number)
print(my_number)