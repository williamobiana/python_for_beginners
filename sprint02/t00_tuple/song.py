# What is a tuple in Python?
# Tuples are used to store multiple items in a single variable in order and unchangeable

# How is a tuple different from a list?
# Lists are mutable and (values can be cahanged)
# Tuples are immutable (values cannot be changed)

# What is the advantage of using a tuple over a list?
# Tuples are faster than lists
# Safe from any accidental modification
# Used for immutable data values
# Can be used as dictionary keys

# How to create a tuple with just one element?
# To create a tuple with only one item, you have add a comma after the item...
# ... else python will consider it a string
# exammple:
# x = ("apple",)
# print(type(x))
# output:
# <class 'tuple'>

# Concatenating and Multiplying Tuples
# https://www.digitalocean.com/community/tutorials/understanding-tuples-in-python-3
#
### Concatenating
# coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
# kelp = ('wakame', 'alaria', 'deep-sea tangle', 'macrocystis')
#
# coral_kelp = (coral + kelp)
# print(coral_kelp)
#
# Output:
# ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral', 'wakame', 'alaria', 'deep-sea tangle', 'macrocystis')

### Multiplyiing
# multiplied_coral = coral * 2
# multiplied_kelp = kelp * 3
#
# print(multiplied_coral)
# print(multiplied_kelp)
#
# Output
# ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral', 'blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
# ('wakame', 'alaria', 'deep-sea tangle', 'macrocystis', 'wakame', 'alaria', 'deep-sea tangle', 'macrocystis', 'wakame', 'alaria', 'deep-sea tangle', 'macrocystis')




# Define the song() function with arguments 'verse' & 'tuple'
def song(verse, chorus):
    # verse variable is 2 tuples of strings in a tuple 
    # verse = (('a', 'b'), ('c', 'd'))

    # chorus is a tuple of strings
    # chorus = ('x', 'y')

    # if verse has condition of more than 2 tuples
    if len(verse) > 2:
        res = (verse[0] + chorus + verse[1] + chorus + verse[2] + chorus * 2)
    # if verse has condition of empty
    elif len(verse) == 0:
        res = (chorus)
    # if verse has no conditions
    else:
        res = (verse[0] + chorus + verse[1] + chorus * 2)
    return res
    