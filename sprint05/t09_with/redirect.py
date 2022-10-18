# context managers which facilitate the proper handling of resources
# It is helpful for the automatic setup and teardown of resources.

# examples of content managers for diffrent features
# https://www.geeksforgeeks.org/context-manager-in-python/

# creating context manager that support 'with' statement work effectively
# https://www.geeksforgeeks.org/with-statement-in-python/


import sys

class Redirect:
    def __init__(self, filepath, direct):
        self.filepath = filepath
        self.dir = direct
        self.o = sys.stdout
        self.e = sys.stderr

    def __enter__(self):
        self.file = open(self.filepath, 'w')
        if self.dir == 'o':
            sys.stdout = self.file
        if self.dir == 'e':
            sys.stderr = self.file
        if self.dir == 'oe':
            sys.stdout = self.file
            sys.stderr = self.file
        return self.file

    # define the exit with parameters to manage exceptions since the script has more than 1 parameter
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_value:
            print(f'exit exception text: {exc_value}')
            return True
        sys.stdout = self.o
        sys.stderr = self.e
        self.file.close()


