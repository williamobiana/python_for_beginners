
# EOFError: when one of the built-in functions input() or raw_input() hits an end-of-file condition (EOF) 
#           without reading any data.

# ValueError is raised when a user gives an invalid value to a function but is of a valid argument
# TypeError is raised when a value is not of the expected type
# other error types: https://docs.python.org/3/library/exceptions.html

# Keyerror is formatted diffrently because it works with dictionaries


def raise_error(key, message):
    if key == 'value':
        raise ValueError(message)
    if key == 'key':
        raise KeyError(message)
    if key == 'index':
        raise IndexError(message)
    if key == 'memory':
        raise MemoryError(message)
    if key == 'name':
        raise NameError(message)
    if key == 'eof':
        raise EOFError(message)
    else:
        message = 'No error with such key.'
        raise ValueError(message)
    
    
    
    
    



