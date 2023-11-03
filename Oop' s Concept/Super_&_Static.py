"""
==> Super Method : (all types of methods and variables )We Can access parent class properties using super keyword

    - this function returns temporary object which contains reference to parent class
"""

class Computer(object):
    # def __init__(self,ram,storage): using parameterized
    def __init__(self):
        self.ram = '8gb'
        self.storage = '512gb'
        print("computer class constructor called")


class Mobile(Computer):
    # def __init__(self,ram,storage):
    def __init__(self):
        # super().__init__('ram','storage') return an object any parent class
        super().__init__()  # return an object any parent class
        self.model = 'iphone'
        print("mobile class constructor called")


# Apple = Mobile('8gb','512gb') using parameters .. we can also call func from here
Apple = Mobile()
print(Apple.__dict__)

""" 
inside this computer is parent class and mobile is child class 
by using super class inside the child  class it can access proportion of parent class
"""

""" Static Methods : Static Methods are which performs operations on external data , 
    data which not associates with class & object 
    
    - No need to pass object or class refrence, created using decorator @staticmethod
 """

#  ----> Example 1 inside static we dont need to use self
class Bank:
    bank_name = 'Axis'
    rate_of_interest=12.25 #class variable
    @staticmethod
    def simple_interest(prin,n):
        si = (prin*n*Bank.rate_of_interest)/100
float(input("enter principle value:"))
float(input("enter num of years:"))

Bank.simple_interest(20000,3)

# static methods are independent
# we can call them with object or class itself
# we don't need to pass self argument in class method
