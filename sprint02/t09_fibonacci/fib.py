# Create a script that contains two functions:
#   - fib() takes a parameter 'n' and returns the number in the Fibonacci Sequence under that index
#   - fib_generator() is a generator function. It takes a parameter 
#     (upper limit for the index) and returns the Fibonacci number under the current index. 
#     The function calls the function fib()

# def fib(n):
#     if n < 0:
#         print('incorrect input')
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# 
# This function above uses a recurrsion to call on itself:
# reference: https://www.youtube.com/watch?v=ngCos392W4w
# reference: sprint01 notes function.txt
# 
# def fib_generator(num):
#     a = 0
#     b = 1
#     for i in range(num):
#         yield a
#         a, b = b, a + b # Adds values together then swaps them
# 
# this function above uses the first numbers of the fib sequence as reference



# Testing using yeild(generator) and the 2 functions
def fib(n):
    return n if n == 1 or n == 0 else fib(n-1) + fib(n-2)

def fib_generator(num):
    a = fib(0)
    b = fib(1)
    for _ in range(num):
        yield a
        a, b = b, a + b
