# """
# 1. __init__(self, ...): This method is called when an object is
#     created from a class and is used to initialize its attributes.
# """
#
#
# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#
# obj = MyClass(42)  # Calls __init__ to initialize 'value' attribute.
#
#
# # 2.__str__(self): Defines the string representation of an object for display using str() and print.
# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return f"MyClass instance with value: {self.value}"
#
#
# obj = MyClass(42)
# print(obj)  # Calls __str__ to display the string representation.
#
#
# # 3. __add__(self, other): Customizes the behavior of the + operator for instances of the class.
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#
# point1 = Point(1, 2)
# point2 = Point(3, 4)
# result = point1 + point2  # Calls __add__ to create a new Point object.
#
#
# # 4. __eq__(self, other): Defines the equality comparison behavior using ==.
#
# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     def __eq__(self, other):
#         return self.value == other.value
#
#
# obj1 = MyClass(42)
# obj2 = MyClass(42)
# result = obj1 == obj2  # Calls __eq__ to check if objects are equal.
#
#
# # 5. __len__(self): Customizes the behavior of len() for instances of the class.
#
# class MyList:
#     def __init__(self, data):
#         self.data = data
#
#     def __len__(self):
#         return len(self.data)
#
#
# my_list = MyList([1, 2, 3, 4, 5])
# length = len(my_list)  # Calls __len__ to get the length of the list.
#
#
# # 6. __getitem__(self, key): Customizes object indexing using square brackets ([]).
#
# class MyDict:
#     def __init__(self, data):
#         self.data = data
#
#     def __getitem__(self, key):
#         return self.data[key]
#
#
# my_dict = MyDict({'a': 1, 'b': 2})
# value = my_dict['a']  # Calls __getitem__ to retrieve the value.
#
# """
# ===> __ne__(self, other): Defines the behavior for the inequality comparison using !=.
#
# ===> __lt__(self, other): Defines the behavior for the less-than comparison using <.
#
# ===> __le__(self, other): Defines the behavior for the less-than or equal comparison using <=.
#
# ===> __gt__(self, other): Defines the behavior for the greater-than comparison using >.
#
# ===> __ge__(self, other): Defines the behavior for the greater-than or equal comparison using >=.
#
# ===> __contains__(self, item): Customizes the behavior for the in operator.
#
# ===> __iter__(self): Used to define an iterator for an object, enabling it to be looped over with for loops.
#
# ===> __next__(self): Used in conjunction with __iter__ to specify the next value in an iterable sequence.
#
# ===> __del__(self): Defines custom behavior when an object is deleted.
#
# ===> __enter__(self), __exit__(self, exc_type, exc_value, traceback): Used for context management, typically with the with statement.
#
# ===> __call__(self, ...): Allows you to treat an instance of a class as a function by defining the behavior of calling the object.
#
# ===> __getattr__(self, name): Customizes attribute access when an attribute is not found in an object.
#
# ===> __setattr__(self, name, value): Customizes attribute assignment behavior.
#
# ===> __delattr__(self, name): Customizes attribute deletion behavior.
#
# ===> __getitem__(self, key): Used for indexing behavior within an object.
#
# ===> __setitem__(self, key, value): Customizes behavior when setting values via indexing.
#
# ===> __delitem__(self, key): Defines behavior for deleting items via indexing.
#
# """

class hello:
    def __init__(self, m, n):  # this needs m and n
        self.g = m
        self.h = n

    def hi(self, x, y):
        a = x + self.g
        b = x + self.h  # use self to access other class members
        return a, b


m = 100
n = 200
obj = hello(m, n)  # pass m and n to the constructor
c = obj.hi(10, 11)
print(c)


# using polymorphism adding sum of numbers
class add:
    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s

s = add()

# sum of 1 integer
print(s.sum(1))

# sum of 2 integers
print(s.sum(3, 5))

# sum of 3 integers
print(s.sum(1, 2, 3))

"""
The add class is defined.

Inside the add class, there is a method named sum that takes three arguments, a, b, and c, with default values of None.

A variable s is initialized to 0. This variable will store the sum of the provided integers.

The sum method checks if a, b, and c are not None. If all three arguments are provided, 
it calculates the sum of a, b, and c and assigns it to the variable s.

If a and b are provided (but not c), it calculates the sum of a and b and assigns it to s.

If only a is provided (and both b and c are None), it assigns a to s.

Finally, the s variable, which contains the calculated sum, is returned from the sum method.

An instance of the add class is created with s = add().

The sum method of the s instance is called with different numbers of arguments to demonstrate its functionality:

print(s.sum(1)): This calculates the sum of one integer (1) and prints it. Since only one argument is provided, 
the method returns the value of that argument (1). 

print(s.sum(3, 5)): This calculates the sum of two integers (3 and 5) and prints it. The method returns the sum of 3 and 5, which is 8.

print(s.sum(1, 2, 3)): This calculates the sum of three integers (1, 2, and 3) and prints it. The method returns the sum of these three numbers, which is 6.

"""