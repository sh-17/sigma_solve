"""
==> Super Method : (all types of methods and variables )We Can access parent class properties using super keyword

    - this function returns temporary object ehich contains reference to parent class
"""

class Computer(object):
    # def __init__(self,ram,storage): using parameterized
    def __init__(self):
        self.ram = '8gb'
        self.storage = '512gb'
        print("computer class cinstructor called")

class Mobile(Computer):
    # def __init__(self,ram,storage):
    def __init__(self):
        # super().__init__('ram','storage') return an object any parent class
        super().__init__() # return an object any parent class
        self.model = 'iphone'
        print("mobile class constructor called")
# Apple = Mobile('8gb','512gb') uisng parameterise .. we can also call func from here
Apple = Mobile()
print(Apple.__dict__)

""" inside this computer is parent class and mobile is child class 
    by using super class inside the child  class it can access propertion of parent class

"""