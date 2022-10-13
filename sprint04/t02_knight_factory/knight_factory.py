# How is a module different from a package in Python? What is the benefit of using a package?
# What is the role of __init__.py in a package?
# What standard module is used to work with logging?
# What is the role of a Handler object in logging? How to print a log to the error or output stream?
# How can a Formatter object help? What are LogRecord attributes and what are they used for?


# Create a Python package with __init__.py
# Modules and Packages
# logging — Logging facility for Python


#https://www.geeksforgeeks.org/what-is-the-difference-between-pythons-module-package-and-library/
#Modules contain functions
#Package contains modules

#https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
#__init__.py is a constructor to initialize a package and group modules that can be called with import

#https://docs.python.org/3/library/logging.html
#https://blog.sentry.io/2022/07/19/logging-in-python-a-developers-guide/
#handler
#how to use a formatter object, #logrecords attributes (name, level, msg etc)


#how to print a log to err or output
#By passing sys.stdout or sys.stderr to the logging.StreamHandler() function


import generator

for i in range(5):
    generator.logging.info('[Name chosen.]')
    generator.logging.info('[Title chosen.]')
    generator.logging.info(f'Sir {generator.names.names()} the {generator.titles.titles()}')










