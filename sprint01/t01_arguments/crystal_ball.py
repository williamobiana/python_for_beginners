# Arguments:
# information can be passed into functions as argurments
# arguments are specified after the function name, inside the parentheses ().
# example:
# def my_function(fname):
# fname is the argument 

# you can add as many argurments as you want, just seperate them with a comma ,.
#
#   
# Number of Arguments:
# By default, a function must be called with the correct number of arguments
# if your function expects 2 arguments, you have to call the function with 2 arguments
# else you get a traceback error (missing 1 required positional argument)
# example:
# def my_function(fname, lname):
#     print(fname + " " + lname)
# my_function('Emil', 'Obi')

# logical operators "and" and "or" are used to combine conditional statements



def crystal_ball(courage, intelligence):
    if courage > 50 and intelligence > 50:
        print('I see great success in your future')
    elif courage >= 100 or intelligence <= 10:
        print('Your life is in danger')
    else:
        print('Your future is a mystery')