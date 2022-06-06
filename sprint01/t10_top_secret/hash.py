# Hashing is a mathematical formula used to encrypt and verify data. 
# ... A hashed message cannot be altered without changing the hash, 
# ... which can then be used to verify that the message has not been altered.

# In programming, the hash method is used to return "integer values" ...
# ... that are used to compare dictionary keys using a dictionary look up feature

# Hashing is the process of using an algorithm to map data of any size to a fixed length.
# ... This is called a hash value.

# A hash table is an unordered collection of key-value pairs, where each key is unique.

# An object is hashable if it has a "hash value" which never changes during its lifetime.
# ... A hashable object needs a __hash__ method.
# ... in cases of comparisons, a hashable object needs an __eq__ method.

# The hash() function returns the "hash value" of the object if it has one. 
# ... Hash values are integers.

# example
# https://zetcode.com/python/hashing/

# From the example..
# 1. Even though the user details are the same, the comparison yields differet objects
# 2. We implement a custom __eq__ method. it would result in TypeError: unhashable type: 'User'.
# 3. We implement the __eq__ and the __hash__ methods...
# ... The implementation of the __hash__ function returns a hash value...
# ... computed with the hash function from a tuple of attributes.

# Hashing Strings with Python
# https://www.pythoncentral.io/hashing-strings-with-python/

# The hashlib module, is a module popular hashing algorithms. 
# common hash functions are: md5, sha1

# Hashing function only takes a sequence of bytes as a parameter
# To hash a string, encode the string in a sequence of bytes. (convert to bytes)


def md5_hash(msg):
    import hashlib
    hash_object = hashlib.md5(msg.encode())
    print('Original String:', msg)
    print('md5 hash generated is ')
    print(hash_object.hexdigest())

def sha1_hash(msg):
    import hashlib
    hash_object = hashlib.sha1(msg.encode())
    hex_dig = hash_object.hexdigest()
    print('Original String:', msg)
    print('sha1 hash generated is ')
    print(hex_dig)