

# all() is a function to return True if all of the items  is True, if not all True, then it will return False.
# https://www.programiz.com/python-programming/methods/built-in/all

# functools returns other functions
# from functools import reduce

# https://www.pythontutorial.net/python-basics/python-reduce-list/
#The reduce() function accepts a function and a sequence and
#returns a single value calculated as follows:

#1) Initially, the function is called with the first two items from the sequence 
#and the result is returned.
#2) The function is then called again with the result obtained in step 1 
#and the next value in the sequence. This process keeps repeating 
#until there are no items in the sequence.

# my_list = [ 1, 2, 8, 50, 90 ]  ==> 1 + 2 = 3 / 3 + 8 = 11 / 11 + 50 = 61 / 61 + 90 = 151

from functools import reduce
def multiplier(lst):
    try:
        if not isinstance(lst, list):
            raise ValueError('The given data is invalid.')
        elif isinstance(lst, list) and all(isinstance(i,(int,float)) for i in lst) == False:
            raise ValueError('The given data is invalid.')
        else:
            result = reduce(lambda a,b: a*b, lst)
            return result
    except ValueError as z:
        print(z)

# ref: 
# https://datascienceparichay.com/article/python-check-list-contains-only-numbers/
#  




