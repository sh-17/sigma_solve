""" Basic Example :

# taking two variable having same object name
nm = "hetvi" # first it will allocate memory for hetvi
nm = "sheth" # after that this line will execute so one tag (nm) cannot point same object & it will automatically break
the "hetvi (nm) tag" like this way python removes memory using garbage collector
print(nm)

"""

import gc

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} is being deleted")

# Create two Person objects
person1 = Person("Hetvi")
person2 = Person("Sheth")

# Create a circular reference
person1.friend = person2
person2.friend = person1

# Remove references to the objects
del person1
del person2

# Manually trigger garbage collection (not typically necessary)
gc.collect()

# You'll see the "__del__" method being called as the objects are deleted

"""
In this example we create two Person objects named “ hetvi” & “sheth”. then we create a circular reference by 
making each person reference the other as their friend. When we remove references to both objects using del, 
they are no longer accessible. At this point, the garbage collector can identify and collect these objects, 
and the __del__ method is called, indicating that the objects are being deleted. The circular reference does not 
prevent the garbage collector from working correctly in this case.
 
"""