# iteration - repetition of steps until a condition is met.

# a loop is a sequence of instructions that is continually repeated until a certain 
# ...condition is reached.

# an exit condition is a statement that must be met to terminate a loop

# An Infinite Loop is a continuous repetitive conditional loop 
# that gets executed until an external factor interferes to stop it.

# A counter() varaible is an integer variable with an initial value of zero
# print(Counter(['A','A','B','B','C','C']))

# using and updating count in a "while" loop
# count = 0
# while (count < 9):
#    print('The count is:', count)
#    count = count + 1 #updating the counter variable
# 
# print("Good bye!")

# while loops are well suited, when i dont know how many iterations i will need.
# the syntax is...
# while [this condition is true]
#     [do this]
# example:
# password = input('Enter your password: ')
# while password != 'unic0rn1990':
#     print('The password is incorrect. Try again')
#     password = input('Enter your password: ')
# print('The password is correct')

# This code keeps asking the user to enter the password while the password is incorrect.
# Once the password is correct, the loop stops iterating

        
def add_to_bookshelf(book_to_add, bookshelf):
    i = 0   #index
    while i < len(bookshelf):
        if bookshelf[i] == '---':
            bookshelf[i] = book_to_add
            return True
        i += 1   #iterate
    else:
        return False

# Note: this execrise took 2 days to understand.
# because its a "while" loop we need to count the index and iterate it
# ....to loop for the duration of the number of strings in the list
# .... or else it will loop forever.



# This is an incorrect way of doing it...    
# def add_to_bookshelf(book_to_add, bookshelf):
#     while bookshelf != []:
#         if '---' in bookshelf:
#             bookshelf.remove('---')
#             bookshelf.append(book_to_add)
#             return True
#         else:
#             return False
#     else:
#         return False
#     





    
