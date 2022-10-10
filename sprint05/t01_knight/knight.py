# What are the different ways of working with **kwargs in class initialization?
# How to set an attribute of an object using a method?
# How to check whether an object has a certain attribute using a method?

#ways of working with **kwargs in class initialization
#https://stackoverflow.com/questions/60418497/how-do-i-use-kwargs-in-python-3-class-init-function

#Python setattr()
#https://www.programiz.com/python-programming/methods/built-in/setattr
# class Food():
#     breakfast = "Pancakes"
#     Lunch = "Sandwich"
# 
# #Parts of setattr
# #self: what class or object
# #name: the variable you are affecting
# #value: what the variable's value will be
# 
# setattr(Food,"breakfast","Toast")
# print(Food.breakfast)
# output: Toast

#Python hasattr()
#https://www.programiz.com/python-programming/methods/built-in/hasattr
#hasattr(object, name)

#10 Examples to Master *args and **kwargs in Python
#https://towardsdatascience.com/10-examples-to-master-args-and-kwargs-in-python-6f1e8cc30749


class Knight:
    #initialize the class
    def __init__(self, **kwargs):
        #set attribute to recieve data from dictionary
        for key, value in kwargs.items():
            setattr(self, key, value)

    def greet(self):
        #check if name and title is in the dictionary
        if hasattr(self,'name') and hasattr(self,'title'):
            print(f"Hello, I'm Sir {self.name} the {self.title}!")
        else:
            print("Hello")
