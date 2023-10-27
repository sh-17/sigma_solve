"""
    Dunder methods" and "magic methods" both refer to the same set of special methods in Python, and
    they have names enclosed in double underscores (e.g., __init__, __str__, __add__). These methods define how
    objects of a class should behave in response to various built-in operations and functions
"""

# 1. __init__ (Dunder Method): Initializes object attributes when an instance of the class is created.

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)  # Creates an object and initializes its 'value' attribute.

# 2. __str__ (Dunder Method): Defines a human-readable string representation of the object. It's used by the str() function and print

class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value: {self.value}"

obj = MyClass(42)
print(obj)  # Calls obj.__str__() to display the string representation

# 3. __add__ (Dunder Method): Defines the behavior of the + operator when applied to objects of the class.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1 + point2  # Calls point1.__add__(point2) to create a new Point object.
