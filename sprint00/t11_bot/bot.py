# create a bot

#strings
str1 = input('Enter your first string: ')
str2 = input('Enter your second string: ')
if str1 == '':
    print('One of the strings is empty.')
elif str2 == '':
    print('One of the strings is empty.')
elif str1 and str2 == '':
    print('One of the strings is empty.')
else:
    command = input('Enter your command: ')
    #operation
    if command == 'find':
        if str2 in str1:
            find = True
        else:
            find = False
        print(find)
    elif command == 'concat':
        concat = str1 + ' ' + str2
        print(f'Your string is: {concat}')
    elif command == 'beatbox':
        btbx1 = input('Enter your first beatbox number: ')
        b1 = int(btbx1)
        btbx2 = input('Enter your second beatbox number: ')
        b2 = int(btbx2)
        print((str1*b1) + (str2*b2))
    else:
        print('usage: command find | concat | beatbox')
    