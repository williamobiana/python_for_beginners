# What is a finite state machine?
# How does the method __call__() affect a class?
# Python Generators & Co-routines(cooperative-functions)

# Python Co-routines
# https://www.youtube.com/watch?v=tqay-vzqSN0
# https://arpitbhayani.me/blogs/fsm

# __call__() in python class
# https://www.geeksforgeeks.org/__call__-in-python/
# The __call__ method enables the instances to behave like functions and can be called like a function
# class Example:
#     def __init__(self):
#         print("Instance Created")
#     def __call__(self):
#         print("Instance is called via special method")
# e = Example()
# # __call__ method will be called
# e()

# FSM is a way of controlling & organizing logic 
# finite = limited number, state = how it is at the moment, machine
# a program can have 1 active state at a time.

# While building FSMs, 
# how we decide to model and implement states and transition functions

# States could be modeled as Co-routines:
#   it will run an infinite loop within which they accept an input, 
#   decides the transition  
#   updates the current state of the FSM
# Transition function could be as simple as a bunch of if and elif statements 

import sys
import logging
import time

# colours in python
# https://pkg.go.dev/github.com/whitedevops/colors
clr = ['\033[1;32m',
       '\033[1;31m',
       '\033[1;33m',
       '\033[m']

logger = logging.getLogger()

if not logger.hasHandlers():
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s %(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

# define the traffic light state
class TrafficLightState:
    def __init__(self):
        self.green = None
        self.yellow = None
        self.red = None
        self.state = self.yellow

    def get_new_color(self):
        prev_char = ''
        while True:
            char = yield
            if char == 'y' and prev_char == 'r':
                self.state = self.green
            if char == 'y' and prev_char == 'g':
                self.state = self.red
            if char == 'g' or char == 'r':
                pass
            prev_char = char

# define the color states
class GreenState(TrafficLightState):
    def __init__(self):
        super(GreenState, self).__init__()
        self.color = f'{clr[0]}Green{clr[3]}'
        self.c = 'g'
        logger.info("GreenState created")


class RedState(TrafficLightState):
    def __init__(self):
        super(RedState, self).__init__()
        self.color = f'{clr[1]}Red{clr[3]}'
        self.c = 'r'
        logger.info("RedState created")


class YellowState(TrafficLightState):
    def __init__(self):
        super(YellowState, self).__init__()
        self.color = f'{clr[2]}Yellow{clr[3]}'
        self.c = 'y'
        logger.info("YellowState created")


# define the machine state
class TrafficLightStateMachine(TrafficLightState):
    def __init__(self):
        super(TrafficLightStateMachine, self).__init__()
        self.green = GreenState()
        self.red = RedState()
        self.yellow = YellowState()
        self.state = self.green
        self.get = self.get_new_color()
        self.get.send(None)
        logger.info("TrafficLight state machine created")

    def __call__(self):
        while True:
            yield self.state.color
            self.get.send(self.state.c)
            time.sleep(0.2)

