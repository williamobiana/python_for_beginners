# A guide to newer python string format techniques
# https://realpython.com/python-formatted-output/

# convert string to operator
# https://stackoverflow.com/questions/1740726/turn-string-into-operator



def validator(operation):
    value = operation.split(' ') #convert to list
    #variable for num1
    if value[0] != '':
        num1 = float(value[0])       
    else:
        return False
    #variable for num2
    if value[2] != '':
        num2 = float(value[2])
    else:
        return False
    #variable for operator
    if value[1] == '<' or value[1] == '>': 
        opr = value[1]
    elif value[1] == '==':
        opr = value[1]
    elif value[1] == '<=' or value[1] == '>=':
        opr = value[1]
    else:
        return False
    
    exp = (f'{num1} {opr} {num2}') 
    compute = eval(exp)    #eval = evaluate
    if compute is True:
        return True
    elif compute is False:
        if value[0] == value[2] and value[1] == '>':
            opr = value[1].replace('>', '==')
            exp = (f'{num1} {opr} {num2}') 
            return exp
        elif value[0] == value[2] and value[1] == '<':
            opr = value[1].replace('<', '==')
            exp = (f'{num1} {opr} {num2}') 
            return exp
        elif value[0] < value[2] and value[1] == '==':
            opr = value[1].replace('==', '<=')
            exp = (f'{num1} {opr} {num2}') 
            return exp
        elif value[0] > value[2] and value[1] == '==':
            opr = value[1].replace('==', '>=')
            exp = (f'{num1} {opr} {num2}') 
            return exp
        elif value[1] == '<':
            opr = value[1].replace('<', '>')
            exp = (f'{num1} {opr} {num2}') 
            return exp
        elif value[1] == '>':
            opr = value[1].replace('>', '<')
            exp = (f'{num1} {opr} {num2}') 
            return exp
        elif value[1] == '<=':
            opr = value[1].replace('<=', '>=')
            exp = (f'{num1} {opr} {num2}') 
            return exp
        elif value[1] == '>=':
            opr = value[1].replace('>=', '<=')
            exp = (f'{num1} {opr} {num2}') 
            return exp
        