# Using bytes
# s = 'abc'
# 
# # string to bytes using bytes()
# b = bytes(s, encoding='utf-8')
# print(type(b))							# <class 'bytes'>
# print(b)								# b'abc'
# 
# # bytes to string using decode()
# s = b.decode()
# print('Original String =', s)			# Original String = abc
# s = 'xyz'		
#---------------------------------------------------------------
# Using encode
# To encode
# data = ""  			#string
# data = "".encode()	#bytes
# print(data)
# output: data = b"" 			#bytes

# To decode
# data = b"" 			#bytes
# data = b"".decode() #string
# print(data)
# output: data = str(b"")  	#string

# For Loops
# for bytes in encoded_a:
#     print(bytes, end = ' ')
#---------------------------------------------------------------


# def convert_to_bytes(arg1, arg2, arg3):

#string
# https://www.geeksforgeeks.org/python-convert-string-to-bytes/
# x = 'bbb'
# data_type = type(x).__name__
# b = bytes(x, encoding='utf-8')
# 
# print(f'-- The {data_type} value is "{x}"\n\
# bytes: "{b}"')

#interger
# https://www.geeksforgeeks.org/how-to-convert-int-to-bytes-in-python/
# x = 1
# data_type = type(x).__name__
# b = (x).to_bytes(1, byteorder="little") 
# 
# print(f'-- The {data_type} value is "{x}"\n\
# bytes: "{b}"')

#boolean
# https://www.programiz.com/python-programming/methods/built-in/bytearray
# x = False
# data_type = type(x).__name__
# b = bytes(x)   #bytes is for immutable objects
# 
# print(f'-- The {data_type} value is "{x}"\n\
# bytes: "{b}"')

# from bytes import convert_to_bytes

def convert_to_bytes(arg1, arg2, arg3):
    # interger
    x1 = int(arg1)
    data_type1 = type(x1).__name__
    b1 = bytes(x1) 
    
    # boolean
    if arg2 == 'False':
        arg2 = False
    elif arg2 == 'True':
        arg2 = True
    else:
        arg2 = False
    x2 = bool(arg2)
    data_type2 = type(x2).__name__
    b2 = bytes(x2)   #bytes is for immutable objects
    
    # string
    data_type3 = type(arg3).__name__
    b3 = bytes(arg3, encoding='utf-8')
    
    # output
    print(f'-- The {data_type1} value is "{arg1}"\n\
    bytes: "{b1}"')

    print(f'-- The {data_type2} value is "{arg2}"\n\
    bytes: "{b2}"')
    
    print(f'-- The {data_type3} value is "{arg3}"\n\
    bytes: "{b3}"')    