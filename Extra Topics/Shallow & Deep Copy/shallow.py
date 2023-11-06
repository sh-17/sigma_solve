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
