# A set is an unordered collection of items
# A set itself is mutable, but ...
# Every set element is unique (no duplicates) and must be immutable (cannot be changed)
# It can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc

# Note: sets dont allow duplication, this is a huge advantage when performing set operations

# A set is created by placing all the items (elements) inside curly braces {}, 
# ... separated by comma, or by using the built-in set() function.
# It can have any number of items and they may be of different types 
# ... (integer, float, tuple, string etc.)
# But no mutable elements like (lists, sets or dictionaries) as its elements, else traceback.
# example:
# my_set = {1.0, "Hello", (1, 2, 3)}
# my_set = set([(1, 2, 3), "Hello", 1.0])

# Creating an empty set
# Empty curly braces {} will make an empty dictionary
# Empty set() will make an empty set
# example
# a = set()

# Modifying a set
# Sets are mutable, since they are unordered, indexing is pointless
# We can add a single element using the add() method
# We can add multiple elements using the update() method
# The update() method can take tuples, lists, strings or other sets as its argument
# example
# my_set = {1, 3}
# my_set.add(2)
# my_set.update([2, 3, 4])
# my_set.update([4, 5], {1, 6, 8})

# Note: although lists are not allowed in set, the update() method can use the list element

# Removing elements from a set
# A particular item can be removed from a set using the methods discard() and remove()
# discard() function leaves a set unchanged if the element is not present in the set
# remove() function will raise an error in such a condition (if element is not present in the set)
# example
# my_set = {1, 3, 4, 5, 6}
# my_set.discard(4)
# my_set.remove(6)
# my_set.discard(2)    #nothing will happen, eventhough 2 was not in the set
# my_set.remove(2)     #error, because 2 was not in the set

# pop() method remove and return an item  
# clear() method remove all the items from a set 

# SET OPERATIONS
# Union (|) or union()
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A | B) or A.union(B) or B.union(A)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (&) or intersection()
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A & B) or A.intersection(B) or B.intersection(A)
# Output: {4, 5}

# Difference (-) or difference() # set of element in one variable
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A - B) or A.difference(B)
# Output: {1, 2, 3}
#
# print(B - A) or B.difference(A)
# Output: {8, 6, 7}

# Symmetric Difference (^) or symmetric_difference() # set of element in both variables (except intersection)
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A ^ B) or A.symmetric_difference(B) or B.symmetric_difference(A)
# Output: {1, 2, 3, 6, 7, 8}

# other set methods
# https://www.programiz.com/python-programming/set



# define witch hunt that looks for witches using set of names.
# 2 list of sets as argurments
# operation returns a set of names of witches
def witch_hunt(suspect_set, innocent_set):
    if len(suspect_set) > 2:
        if suspect_set != [] and innocent_set != []:
            # by default if the suspect names are in innocent name, they are removed by symmetric diffrence
            ss1 = suspect_set[0] ^ innocent_set[0] ^ innocent_set[1]
            ss2 = suspect_set[1] ^ innocent_set[0] ^ innocent_set[1]
            ss3 = suspect_set[2] ^ innocent_set[0] ^ innocent_set[1]
            is1 = innocent_set[0]
            is2 = innocent_set[1]
            # set operation to filter names
            inter_ss = ss1 & ss2 & ss3
            diff_is = is1 - is2
            hunt = inter_ss - diff_is
            return hunt
        elif suspect_set != [] and innocent_set == []:
            ss1 = suspect_set[0]
            ss2 = suspect_set[1]
            ss3 = suspect_set[2]
            is1 = set()
            is2 = set()
            inter_ss = ss1 & ss2 & ss3
            diff_is = is1 - is2
            hunt = inter_ss - diff_is
            return hunt        
        elif suspect_set == [] and innocent_set != []:
            ss1 = set()
            ss2 = set()
            ss3 = set()
            is1 = innocent_set[0]
            is2 = innocent_set[1]                
            inter_ss = ss1 & ss2 & ss3
            diff_is = is1 - is2
            hunt = inter_ss - diff_is
            return hunt
        else:
            ss1 = set()
            ss2 = set()
            ss3 = set()
            is1 = set()
            is2 = set()
            inter_ss = ss1 & ss2 & ss3
            diff_is = is1 - is2
            hunt = inter_ss - diff_is
            return hunt
    else:
        if suspect_set != [] and innocent_set != []:
            ss1 = suspect_set[0]
            ss2 = suspect_set[1]
            is1 = innocent_set[0]
            is2 = innocent_set[1]
            inter_ss = ss1 & ss2
            diff_is = is1 - is2
            hunt = inter_ss - diff_is
            return hunt
        elif suspect_set != [] and innocent_set == []:
            ss1 = suspect_set[0]
            ss2 = suspect_set[1]
            is1 = set()
            is2 = set()
            inter_ss = ss1 & ss2
            diff_is = is1 - is2
            hunt = inter_ss - diff_is
            return hunt        
        elif suspect_set == [] and innocent_set != []:
            ss1 = set()
            ss2 = set()
            is1 = innocent_set[0]
            is2 = innocent_set[1]                
            inter_ss = ss1 & ss2
            diff_is = is1 - is2
            hunt = inter_ss - diff_is
            return hunt
        else:
            ss1 = set()
            ss2 = set()
            is1 = set()
            is2 = set()
            inter_ss = ss1 & ss2
            diff_is = is1 - is2
            hunt = inter_ss - diff_is
            return hunt                

