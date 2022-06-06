# to return a value, use the return statement
# In Python, every function returns something. If there are no return statements, then it returns None.
# https://www.geeksforgeeks.org/python-return-statement/


# Python allows function arguments to have default values. 
# If the function is called without the argument, the argument gets its default value.
# https://www.programiz.com/python-programming/function-argument
# https://www.geeksforgeeks.org/default-arguments-in-python/

# Python allows function arguments to have default values. If the function is called without the argument, 
# the argument gets its default value.


def buy_milk(money = 0):
    product = '[milk]'
    price = 25
    if money >= price:
        quantity = int(money / price)
        return product * quantity

def buy_bread(money = 0):
    product = '[bread]'
    price = 19
    if money >= price:
        quantity = int(money / price)
        return (product * quantity)[0:21]


