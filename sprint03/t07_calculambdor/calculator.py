
operators = {'add': (lambda a,b:a+b), 
             'sub': (lambda a,b:a-b), 
             'mul': (lambda a,b:a*b), 
             'div': (lambda a,b:a/b), 
             'pow': (lambda a,b:a**b)}

def calculator(opr, a, b):
    try:
        if not isinstance(a,(float,int)) or not isinstance(b,(float,int)):
            raise ValueError('Invalid numbers. Second and third arguments must be numerical.')
        elif opr not in operators:
            raise ValueError('Invalid operation. Available operations: add, sub, mul, div, pow.')
        else:
            return operators[opr](a,b)
    except ValueError as z:
        print(z)
