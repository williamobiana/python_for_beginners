# How to write in a file in Python?
# What happens if you use the write() method with 'w' mode to write to a file that is not empty?
# What is a context manager?
# How does the with statement work?
# Why is the with statement particularly useful for working with files?
# How to check if an open file has been closed?

# https://www.programiz.com/python-programming/file-operation

# with open("test.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")

# This program will create a new file named test.txt in the current directory if it does not exist. 
# If it does exist, it is overwritten.

# context managers automatic setup and teardown of resources (using with statement)
# example:
# with open("test.txt") as f:  # using 'with' closes the file after use
#     data = f.read()
#
# Context managers can be written using classes or functions
# Context manager are more efficient than try-except-finally
#
# to check if an open file has been closed
# print(f.close())
# Output: True (file is closed)
#         False (file is still open)
#
#

########### TASK #############
# Create a script that contains a function write_file(). This function:
#     • takes two arguments:
#         – filename as a string
#             If the given filename does not end with .txt, prints two consecutive messages:
#             'Please enter the filename in the format "filename.txt".'
#             'Failed to write to file "[filename]".'
#         – message to be added
#             (Assume that the function will receive only strings for both arguments. There is
#             no need to handle other cases.)
#             The default value of the message argument must be set to 'None'.
#     • creates a file with the given name (if it doesn't exist yet) and opens it for writing
#     • writes the given message to the file and closes the file
#     • opens the file again to check if it is not empty
#         – if the file is empty or its contents are not equal to the provided message,
#           prints the message: 'Something went wrong...'
#         – otherwise, prints two consecutive messages:
#           * 'Your message has been written to file "[filename]".'
#           * 'File "[filename]" now contains the following text:
#             [message]'

import os
def write_file(filename, message='None'):
    suffix = filename.endswith('.txt')
    if suffix == True:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(message)
        with open(filename, 'r', encoding='utf-8') as f:
            # check if the file is empty (os.stat("file").st_size == 0)
            if os.stat(filename).st_size == 0 or message not in f.read(): 
                print('Something went wrong')
            else:
                print(f'Your message has been written to file "{filename}".')
                print(f'File "{filename}" now contains the following text:\n{message}') 
    else:
        print('Please enter the filename in the format "filename.txt".')
        print(f'Failed to write to file "{filename}".')

