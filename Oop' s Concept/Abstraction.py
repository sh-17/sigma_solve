"""
===> What is Abstraction ?
        - Abstraction is used to hide the internal functionality of the function from the users.
          The users only interact with the basic implementation of the function, but inner working
          is hidden. User is familiar with that "what function does" but they don't know "how it does."
"""

""" 

    Example : Like we are Watching Video On Youtube then how we will do searching for watching any specific videos ?  
              by using keyboard..how we are able to type that alphabets , how it will been shown our screen.. we will 
              get the result on that specific video so how this all things are happening.. someone will upload that 
              videos they also saved the data on there servers on any protocols and fetching that data and shown us on 
              the screen 
              
              means that we just searching the videos ane we get the details but that all things are comming
              from where that we don't know... which called inner functionalities... we don't know internal 
              working that we are getting the data's on our phone we just see the results  
                
            - ABSTRACT CLASS HAVE ONLY DECLARATION NO DEFINATION  IN PYTHON THERE IS NO METHOD WE HAVE TO CREATE METHOD USING DECORATOR
                it can have many more abstract methods
            - There is an ABC module to use abstraction method ..... using this we can make abstract class and method

"""
# Creating an Abstract Class
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, n):
        self.no_of_tyres = n
    @abstractmethod  # after using this we cannot create object of thi vehicle class
    def start(self):
        pass

    # Creating an concrete method : which normal methods
    def display(self):
        print("Hi I am calling from vehicle class")


# Inheriting this all class from vehicle class if we are creating this class in another file then we nned to import
# vehicle class like this : from  *file name* import vehicle

class Bike(Vehicle):
    # defining an own constructor
    def __init__(self,n,color):# self.no_of_tyres = 2(we can also use this)
        super().__init__(n)
        self.color=color

    def start(self):  # we have just declare this method we are not implementing this methods
        print("Start With kick")


class Scooty(Vehicle):
    def __init__(self,n):
        super().__init__(n)

    def start(self):
        print("self start")


class car(Vehicle):
    def __init__(self,n,x): # x is guesing as gears of car
        super().__init__(n)
        self.no_of_gears = 6

    def start(self):
        print("start with key")


# creating an object (if file is different then there is need to import (from main import *))

bike=Bike(2,"BLACK")
bike.start()
scooty=Scooty(2)
scooty.start()
