"""
---> CREATES A NEW OBJECT WHICH STORE THE REFERENCE OF THE ORIGINAL ELEMENTS
---> WE CAN USE SHALLOW COPY IN FOUR DIFFERENT WAYS

    1. BUILT-IN-FUNCTION : list(), set(), dict()
    2. SLICING OPERATORS
    3. LIST COMPREHENSION
    4. COPY FUNCTION FROM COPY MODULE

"""

"""
---> A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to 
the objects found in the original.

"""

""" using list """
list1 = [1,2,3,4]
list2 = list(list1)
print(list2)
list2.append('a')
print(list2)

""" using slicing """
original_list = [1, 2, 3]
shallow_copy = original_list[:]
print(original_list)


"""
--> Using Dictionary : 
You can create a shallow copy of a dictionary using the dictionary's copy() method or the built-in dict() constructor.
Using copy() method
"""
original_dict = {'a': 1, 'b': 2}
shallow_copy = original_dict.copy()
print(shallow_copy)

""" Dict() """
original_dict = {'a': 1, 'b': 2}
shallow_copy = dict(original_dict)
print(shallow_copy)

""" ---> Using Set Method """

original_set = {1, 2, 3}
shallow_copy = original_set.copy()
print(shallow_copy)

""" Set Constructor """
original_set = {1, 2, 3}
shallow_copy = set(original_set)
print(shallow_copy)

""" using copy function """

import copy
original_object= {1, 2, 3}
shallow_copy = copy.copy(original_object)
print(shallow_copy)

"""
1) Assignment Operator (=) :-
    -> The = operator is used for variable assignment. It is used to bind a variable to a value or object.
    -> When we use = operator, we are creating a reference to the same object in memory.
    -> This means that if you modify the object through one variable,
        the change will be reflected in all variables that reference the same object.
"""
import copy

print("\n--- Using (=) ---")
x = [5, 10, 15, 20, 25]
y = x  # Assigning variable "x" as a variable "y"
y[2] = 100
print(f"List x = {x}")
print(f"List y = {y}")


"""
2) copy.copy() :- (Shallow copy)
    -> The copy function is used to create a shallow copy of an object.
    -> A shallow copy of an object creates a new object that is a copy of the original object with a new reference.
    -> But it doesn't create copies of the objects contained within the original object.
    -> Instead, it references the same objects that are inside the original object.
    -> Shallow copies are useful when you want to duplicate the top-level structure of a complex object.
"""
print("\n--- Using (copy) ---")
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = copy.copy(a)
b[1][2] = 100
print(f"Original = {a}")  # [[1, 2, 3], [4, 5, 100], [7, 8, 9]]
print(f"Copy = {b}")  # [[1, 2, 3], [4, 5, 100], [7, 8, 9]]



