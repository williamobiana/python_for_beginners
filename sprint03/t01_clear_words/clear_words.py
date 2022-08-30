# What does the Python map() function do?
# What parameters does the function map() take?
# How to use lambda expressions with map() ?

#https://www.geeksforgeeks.org/python-map-function/
# Python’s map() is a built-in function 
# that allows you to process and transform all the items in an iterable 
# without using an explicit 'for loop', 

#The map function is used to do a certain function to a certain iterable 
# without using 'for loop',

#It takes a function and an iterable
#def square_func(n):
#    return n * n
#
#numbers = [1, 2, 3, 4]
#
## We use map() and arguments parameters (defined function, iterable list)
#result = map(square_func, numbers)
#print(list(result))

# or using lambda
#numbers = [1, 2, 3, 4]
#result = map(lambda n : n * n, numbers)
#print(list(result))

import re
def clear_words(text):
    s = [word for word in text.split(' ') if word]
    result = map(lambda w : (re.sub('[?!.:;,-]', '', w)), s)
    return list(result)

#s = re.split('\s+', text)
#s = text.split(' ')
# i initially used the split variable above, but encountered some error when multple space was used
#https://bobbyhadz.com/blog/python-split-string-ignore-empty-strings

##### used a list comprehension #######
# s = [word for word in text.split(' ') if word]

###### or use a for loop #######
# s = []
# for word in text.split(' '):
#     if word:   #if word is present
#        s.append(word)  

#### function to remove puntuation marks ####
# def strip_marks(text):
#     punctuation = '[?!.:;,-]'
#     strip_word = re.sub(punctuation, '', text)
#     print(strip_word)
# 
#### write map with lambda variation of strip marks ####
# result = map(lambda w : (re.sub(punctuation, '', w)), text)
# print(list(result))












