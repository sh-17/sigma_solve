# TUPLE  : COLLECTION OF ITEMS WE CAN STORE ANYTHING LIKE STR,FLOAT.INT, separated by commas, use parenthesis()

"""
     - Tuple is sequence type of data
     - Tuple are ordered, unchangeable, and allow duplicate values.
     - Tuple is similar to a list in e.g : Indexing, Nested objects and Repetition BUT
     - tuple is immutable & lists are mutable.Once tuple is created we cant change the value.
"""

# Access tuple :

n = 1, 2, 387, 4656, 'hey'
print(n)
print(n[2])

""" O/P : 387 """

# Postive indexing :

n = (1,2,5,-86,-5,36)
print(n[1])
""" O/P : 2 """


# Negative indexing :
n = (1,2,5,-86,-5,36)
print(n[-3])

""" O/P : -87 """
# UPDATE () :

# It will Convert tuple to list after making changes it will convert that list into tuple again.
n = (1,2,5,-86,-5,36)
tuple_list = list(n)
print(tuple_list)

tuple_list.insert(2, "hello")
list_tuple = tuple(tuple_list)
print(list_tuple)
""" O/P : [1,2,5,-86,-5,36] """

# Count() :
"""It will Return the number of elements with the specified value inside the tuple."""

n = (1,2,5,-86,-5,36)
print(n.count(5))
""" O/P : 1 """

# index() :Search the tuple for specified value and return the position of where it was found

n = (1,2,5,-86,-5,36)
print(n.index(4))

# Delete() : You can delete tuple completely.
n = (1,2,5,-86,-5,36)
del n
print(n)
