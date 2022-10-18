# What is inheritance?
# What is the difference between inheritance and composition?
# What does it mean to have an 'is a' relation (in programming)?
# What are the benefits of using inheritance?
# What class do all classes in Python inherit by default?
# What is multiple inheritance?
# How to call the __init__() method of the immediate parent class without specifying the name of the parent class?

# Classes - Inheritance
# Python super()

# What is the difference between inheritance and composition?
# https://www.geeksforgeeks.org/python-oops-aggregation-and-composition/

# Inheritance: take all of the properties of another class
# Composition: relies on propertites of another class

# What class do all classes in Python inherit by default?
# Object Class

# What is multiple inheritance?
# have propertites from multiple classes

# How to call the __init__() method of the immediate parent class without specifying the name of the parent class?
# use the super class function super()

# https://www.youtube.com/watch?v=RSl87lqOXDE

# class Employee:
#     raise_amt = 1.04
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last +'@email.com'
#         self.pay = pay
#     def fullname(self):
#         print(f'{self.first} {self.last}')
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
# dev = Employee('william', 'obiana', 50000)
# print(dev.email)
# 
# 
# class Developer(Employee):
#     raise_amt = 1.10
#     def __init__(self, first, last, pay, prog_lang):
#         #Employee.__init__(self, first, last, pay)
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang
# dev = Developer('william', 'obiana', 50000)
# print(dev.email)
# dev.apply_raise()
# print(dev.pay)
# print(dev.prog_lang)
# 
# 
# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         #Employee.__init__(self, first, last, pay)
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#     def print_emps(self):
#         for emp in self.employees:
#             print(emp.fullname())
# mgr = Manager('sue', 'smith', 90000, [dev])
# print(mgr.email)
# mgr.print_emps()
# mgr.remove_emp(dev)
# mgr.print_emps()
# mgr.add_emp(dev)
# mgr.print_emps()
# 
# print(isinstance(mgr, Manager)) #True
# print(isinstance(mgr, Employee)) #True
# print(isinstance(mgr, Developer)) #False
# 
# print(issubclass(Developer, Employee)) #True
# print(issubclass(Manager, Employee)) #True
# print(issubclass(Manager, Developer)) #False
# 
# 


# colors to prettify output, don't edit
clr = ['\033[38;5;208m',  # Phone
       '\033[38;5;112m',  # Computer
       '\033[38;5;87m',   # Smartphone
       '\033[38;5;160m',  # IPhone
       '\033[0m']

class Phone(object): # you may edit within the parentheses
    def __init__(self, number):
        print(f'{clr[0]}[Phone init ({self.__class__.__name__})]{clr[4]}')
        self.number = number

    def make_call(self, number):
        print(f'{clr[0]}[Phone make call ({self.__class__.__name__})]{clr[4]}')
        print(f'Call from {self.number} to {number}')


class Computer(object): # you may edit within the parentheses
    def __init__(self, operating_system, cpu, ram_size, input_devices):
        print(f'{clr[1]}[Computer init ({self.__class__.__name__})]{clr[4]}')
        self.operating_system = operating_system
        self.cpu = cpu
        self.ram_size = ram_size
        self.input_devices = input_devices


class Smartphone(Computer, Phone): # you may edit within the parentheses
    def __init__(self, operating_system, cpu, ram_size, number, battery):
        print(f'{clr[2]}[Smartphone init ({self.__class__.__name__})]{clr[4]}')
        input_devices = ['touch screen']
        Computer.__init__(self, operating_system, cpu, ram_size, input_devices)
        Phone.__init__(self, number)
        self.battery = battery


class IPhone(Smartphone): # you may edit within the parentheses
    def __init__(self, cpu, ram_size, number, battery):
        print(f'{clr[3]}[IPhone init ({self.__class__.__name__})]{clr[4]}')
        operating_system = 'iOS'
        super(IPhone, self).__init__(operating_system, cpu, ram_size, number, battery)
        

