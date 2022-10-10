# What relationships may exist between classes in OOP?
# What is aggregation in OOP?
# What is composition in OOP?
# What is the difference between aggregation and composition?
# What is the magic __str__() method used for?
# What is the difference between __str__() and __repr__() ?
# How to redirect the log output to a file?


# What is the __str__ method in Python?
# https://www.digitalocean.com/community/tutorials/python-str-repr-functions

# Aggregation vs Composition in Object Oriented Programming
# https://www.geeksforgeeks.org/python-oops-aggregation-and-composition/

# Redirect the log output to a file?
#import logging

#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

#logging.debug('detailed information')
#logging.info('confirmation that things are working')
#logging.warning('something unexpected has happend, but things are working')
#logging.error('some problem has occured and program cannot run')

# to define the format for the output.
#logging.basicConfig(filename='example.log', format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

#check out the logging_attributes for format
#https://docs.python.org/3/library/logging.html#logrecord-attributes


# import logging
# logging.basicConfig(filename='example.log', level=logging.INFO)
# 
# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
# 
#         logging.info(f'Created Employee: {self.fullname} - {self.email}')
#     
#     @property #this indicates that it is a method
#     def email(self):
#         return f'{self.first}.{self.last}@email.com'
# 
#     @property #this indicates that it is a method
#     def fullname(self):
#         return f'{self.first} {self.last}'
# 
#     def __str__(self):
#         return f'{self.first}, {self.last}'
# 
#     def __repr__(self):
#         return f'{self.first}, {self.last})'
# 
# emp_1 = Employee('adam', 'smith')
# emp_2 = Employee('erling', 'haaland')
# emp_3 = Employee('jane', 'foster')
# 
#
#
#
#
#import logging
#
#logging.basicConfig(level='INFO', filename='shipments.log')
#
#class Cargo:
#    #initialize the class
#    def __init__(self, destination, weight):
#        self.destination = destination
#        self.weight = weight
#        logging.info(f'[Cargo] initialized: Cargo(destination={self.destination}, weight={self.weight}')
#    def __str__(self):
#        return f'Cargo to {self.destination} with weight {self.weight}'
#    def __repr__(self):
#        return f'Cargo(destination={self.destination}, weight={self.weight})'
#
#class Container:
#    #initialize the class.
#    def __init__(self, weight_limit, cargo=None):
#        #create the properties
#        self.weight_limit = weight_limit
#        #self.cargo = cargo becomes modifed based on conditions of the module below 
#        if cargo and cargo.weight <= self.weight_limit:
#            self.set_cargo(cargo)
#        else:
#            self.cargo = None
#        logging.info(f'[Container] initialized: Container(weight_limit={self.weight_limit}, cargo={self.cargo}')
#    def set_cargo(self, cargo_class): #we use cargo_class to aviod conflict id we used Cargo()
#        if cargo_class.weight <= self.weight_limit:
#            self.cargo = cargo_class
#            logging.info(f'[Container] Cargo set: Cargo to {self.cargo.destination} with weight {self.cargo.weight}')
#    def __str__(self):
#        return f'Container up to {self.weight_limit} with {self.cargo}'
#    def __repr__(self):
#        return f'Container(weight_limit = {self.weight_limit}, cargo = destination={self.cargo.destination}, weight={self.cargo.weight})'

#class Ship:
#    def __init__(self, route, containers):
#        #route properties(list of strings)
#        self.route = route
#        #(list instances of the container class)
#        self.containers = containers
#        self.add_containers(containers)
#        logging.info(f"[Ship] initialized: {repr(self)}")
#    def add_containers(self, cont_instances):
#        for cont in cont_instances:
#            if cont.cargo and cont.cargo.destination in self.route:
#                self.containers.append(cont)
#                logging.info(f'[Ship] Added Container: {cont}')
#    def __str__(self):
#        text = f'Ship to {self.route} with containers:'
#        for cont in self.containers:
#            text += '\n' + str(cont)
#        return text
#    def __repr__(self):
#        return f'route={self.route},containers={repr(self.containers)}'
#
#
#



import logging

logger = logging.getLogger()

if not logger.hasHandlers():
    handler = logging.FileHandler('shipments.log', mode='w')
    formatter = logging.Formatter('%(levelname)s %(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


class Cargo:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight
        logger.info(f"[Cargo] initialized: {self.__repr__()}")

    def __str__(self):
        return f"Cargo to {self.destination} with weight {self.weight}"

    def __repr__(self):
        return f"Cargo(destination={self.destination}, weight={self.weight})"


class Container:
    def __init__(self, weight_limit, cargo=None):
        self.weight_limit = weight_limit
        if cargo and cargo.weight <= self.weight_limit:
            self.set_cargo(cargo)
        else:
            self.cargo = None
        logger.info(f"[Container] initialized: {self.__repr__()}")

    def set_cargo(self, other):
        if other.weight <= self.weight_limit:
            self.cargo = other
            logger.info(f"[Container] Cargo set: {self.cargo}")

    def __str__(self):
        return f"Container up to {self.weight_limit} with {self.cargo}"

    def __repr__(self):
        return f"Container(weight_limit={self.weight_limit}, cargo={repr(self.cargo)})"


class Ship:
    def __init__(self, route, containers):
        self.route = route
        self.containers = []
        self.add_containers(containers)
        logger.info(f"[Ship] initialized: {repr(self)}")

    def add_containers(self, conts):
        for c in conts:
            if c.cargo and c.cargo.destination in self.route:
                self.containers.append(c)
                logger.info(f"[Ship] Added Container: {c}")

    def __str__(self):
        tmp = f"Ship to {self.route} with containers:"
        for c in self.containers:
            tmp += '\n' + str(c)
        return tmp

    def __repr__(self):
        return f"Ship(route={self.route}, containers={repr(self.containers)})"

