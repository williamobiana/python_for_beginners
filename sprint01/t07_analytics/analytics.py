# A character is anything you can type on the keyboard in one keystroke, 
# ... like a letter, a number, or a backslash.
# 
# Sometimes abbreviated as char, 
# ... a character is a single visual object used to represent text, numbers, or symbols
# https://realpython.com/python-strings/

# to analyse a string for its characteristics, you can use string methods
# str.islower()
# str.isalpha() ....etc
# https://overiq.com/python-101/strings-methods-in-python/

def print_str_analytics(str):
    printable_char = len(str)
    alnum = 0
    alpha = 0
    deci = 0
    lcase = 0
    ucase = 0
    wspace = 0
    for i in str:
        if i.isalnum():
            alnum = alnum + 1
        if i.isalpha():
            alpha = alpha + 1
        if i.isdecimal():
            deci = deci + 1
        if i.islower():
            lcase = lcase + 1
        if i.isupper():
            ucase = ucase + 1
        if i.isspace():
            wspace = wspace + 1
    print('|==================================================|\n'
          '|               String analytics                   |\n'
          '|==================================================|\n'
          f'| {str}                                            \n'
          '|==================================================|')
    print(f'| Number of printable characters is: {printable_char}')
    print(f'| Number of alphanumeric characters is: {alnum}')
    print(f'| Number of alphabetic characters is: {alpha}')  
    print(f'| Number of decimal characters is: {deci}')  
    print(f'| Number of lowercase characters is: {lcase}')
    print(f'| Number of uppercase characters is: {ucase}')
    print(f'| Number of whitespace characters is: {wspace}')
    print('|==================================================|')



    



    
        