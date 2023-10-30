""" Encapsulation means the methods that work on data withing a single unit """


# implementation details are hide

# we restrict data access outside the class in encapsulation.... encapsulation can be achieved by declaring the data
# members and methods of class as private

# public data
class Finance:
    def __init__(self):
        self.revenue = 10000
        self.num_of_Sales = 445


f1 = Finance()
print(f1.__dict__)


class HR:
    def __init__(self):
        self.num_of_emp = 56
        f1.revenue = 1


h1 = HR()
print(f1.__dict__)


# private data : it will call the function but it will not call the attibutes inside the function
class Students:
    __name = "Hetvi"

    def __init__(self):
        print(self.__name)
        # self.__displayinfo()

    def __displayinfo(self):
         print("Welcome")


obj = Students()
obj._Students__displayinfo() # using name mangling if we want to access private data in
# another way we can access through class name and private attribute name


"""
Getter Methods:

Getter methods are used to retrieve the values of an object's attributes. getter methods are use to access private data 

Setter methods are used to modify the values. They encapsulate the modification of an 
attribute, allowing you to add validation or custom logic when setting a new value. Setter methods provide a way to 
control and enforce constraints on the attribute's value, ensuring that it remains within valid boundaries. 


"""


class Circle:
    def __init__(self, radius):
        self._radius = radius  # A protected attribute with an underscore prefix.

    # Getter method to retrieve the radius.
    def get_radius(self):
        return self._radius

    # Setter method to set the radius with validation.
    def set_radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            print("Invalid radius value. Radius must be greater than 0.")


# Create a Circle object and demonstrate encapsulation.
circle = Circle(5)

# Access the radius using the getter method.
print("Radius:", circle.get_radius())

# Attempt to set an invalid radius using the setter method.
circle.set_radius(23)


