# How to define a class in Python?
# What are classes used for?
# What can a class contain?
# What is an instance of a class? How is an instance different from a class?
# How to create an instance of a class?
# What does the method __init__() do?
# How is __init__() called?


class Guard:
    #initialize the class
    def __init__(self, **kwargs):
        
        #check how many parameters are present
        #if more than 1 parameter
        if len(kwargs) > 1:
            self.name = kwargs['name']
            self.salary = kwargs['salary']
        
        #if 1 parameter
        elif len(kwargs) == 1:
            #if that parameter is name
            if 'name' in kwargs:
                self.name = kwargs['name']
                self.salary = 0
            #if that parameter is salary
            elif 'salary' in kwargs:
                self.salary = kwargs['salary']
                self.name = None
        
        #if anything else 
        else:
            self.name = None
            self.salary = 0

    #define the greet method
    def greet(self):
        return (f'Hello, my name is {self.name}!')

    #define the receive_bribe method
    def receive_bribe(self, num):
        if num > self.salary:
            return(f'You may pass.')
        else:
            return('I am not letting you pass.')


