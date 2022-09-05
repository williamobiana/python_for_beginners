# How to work with files in Python?
# What modes can you choose when opening a file with open() ?
# Why is it important to close an opened file?
# What methods does Python have for reading files?
# What error will Python throw if you try to access a file that does not exist? 
# What about a file that has no read permissions?

# https://www.programiz.com/python-programming/file-operation

# A file operation in python takes place in the following order:
#     Open a file
#     Read or write (perform operation)
#     Close the file


########## Opening files ###########
# open(), this function returns a file object, also called a handle.
# example:
# f = open("test.txt")    # open file in current directory
# f = open("C:/Python38/README.txt")  # specifying full path

# We can specify the mode while opening a file. 
# In mode, we specify whether we want to read r, write w or append a to the file. 
# We can also specify if we want to open the file in text mode or binary mode.

# The default is reading in text mode. In this mode, we get strings when reading from the file.
# On the other hand, binary mode returns bytes, 
# ...this is the mode to be used when dealing with non-text files like images or executable files.

# Modes and description
# r = Opens a file for reading. (default)			
# w = Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.		
# x = Opens a file for exclusive creation. If the file already exists, the operation fails. 			
# a = Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist. 			
# t = Opens in text mode. (default) 			
# b = Opens in binary mode.			
# + = Opens a file for updating (reading and writing)

# example:
# f = open("test.txt")      # equivalent to 'r' or 'rt'
# f = open("test.txt",'w')  # write in text mode
# f = open("img.bmp",'r+b') # read and write in binary mode

# when working with files in text mode, 
# it is highly recommended to specify the encoding type to accomodate diffrent OperatingSystem users
# example:
# f = open("test.txt", mode='r', encoding='utf-8')


############# Closing files ##############
# Closing a file will free up the resources that were tied with the file. 
# It is done using the close() method
# example:
# f = open("test.txt", encoding = 'utf-8')
# f.close()

# Note:
# If an exception occurs when we are performing some operation with the file, 
# the code exits without closing the file
# A safer way is to use a try...finally block
# try:
#    f = open("test.txt", encoding = 'utf-8')
# finally:
#    f.close()
# This way, we are guaranteeing that the file is properly closed

#### Closing a file using 'with' statement ######
# The best way to close a file is by using the 'with' statement
# This ensures that the file is closed when the block inside the 'with' statement is exited.
# example:
# with open("test.txt", encoding = 'utf-8') as f:


######## Writing to Files ###########
# In order to write into a file, 
# we need to open it in write w, append a or exclusive creation x mode
# We need to be careful with the w mode, as it will overwrite into the file if it already exists.

# Writing a string or sequence of bytes (for binary files) is done using the write() method.
# example:
# with open("test.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")  #\n for newline
#    f.write("This file\n\n")
#    f.write("contains three lines\n")
# This program will create a new file named test.txt in the current directory if it does not exist. 
# If it does exist, it is overwritten.

######### Reading Files ############
# To read a file in Python, we must open the file in reading r mode
# There are various methods available for this purpose. 
# We can use the read(size) method to read in the size number of data
# If the size parameter is not specified, it reads and returns up to the end of the file.
# example:
# >>> f = open("test.txt",'r',encoding = 'utf-8')
# >>> f.read(4)    # read the first 4 data
# 'This'
# 
# >>> f.read(4)    # read the next 4 data
# ' is '
# 
# >>> f.read()     # read in the rest till end of file
# 'my first file\nThis file\ncontains three lines\n'
# 
# >>> f.read()  # further reading returns empty sting
# ''

# We can change our current file cursor (position) using the seek() method. 
# Similarly, the tell() method returns our current position (in number of bytes).
# example:
# >>> f.tell()    # get the current file position
# 56
# 
# >>> f.seek(0)   # bring file cursor to initial position
# 0
# 
# >>> print(f.read())  # read the entire file
# This is my first file
# This file
# contains three lines

# We can read a file line-by-line using a for loop
# example:
# >>> for line in f:
# ...     print(line, end = '')
# ...
# This is my first file
# This file
# contains three lines

# Alternatively, we can use the readline() method to read individual lines of a file
# >>> f.readline()
# 'This is my first file\n'
# 
# >>> f.readline()
# 'This file\n'
# 
# >>> f.readline()
# 'contains three lines\n'
# 
# >>> f.readline()
# ''

# Lastly, the readlines() method returns a list of remaining lines of the entire file
# >>> f.readlines()
# ['This is my first file\n', 'This file\n', 'contains three lines\n']


######## File methods ###########
# https://www.programiz.com/python-programming/file-operation


######### Errors ##########
# error if you try to access a file that does not exist?
# output: [Errno 2] No such file or directory

# error if a file has no read permissions?
# output: [Errno 13] Permission denied



############## TASK ###############
# Create a script that contains a function read_file() that:
#   takes one argument: filename as a string
#   (You are not required to handle cases when the argument is not of type str)
#   if the file is present in the current directory (and the user has read permissions for it):
#       - opens the file
#       - reads the file and saves its contents in a variable
#       - prints the file contents in the following format:
#            'File "[filename]" has the following message:
#            [file contents]'
#       closes the file
#   if there is no such file in the current directory (or the user has no read permissions ...
#   ... for the requested file):
#       - prints the message: 'Failed to read file "[filename]".'

def read_file(filename):
    try:
        f = open(filename,'r',encoding = 'utf-8')
        data = f.read().rstrip()  #rstrip is to strip txt from file. 
        print(f'File {filename} has the following message:\n{data}')
        f.close() 

        ### alternative ###
        # with open('data.txt', 'r') as file:
        # data = file.read().rstrip()
        # print(f'File {filename} has the following message:\n{data}')

    except FileNotFoundError:   
        print(f'Failed to read file {filename}.')
    except PermissionError:
        print(f'Failed to read file {filename}.')






