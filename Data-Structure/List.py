"""
LIST : each element or value which is inside list is called item,list comes under sequence datatype

        - list are define by having values
        - list are orderable & mutable so we can update value and have definite count
        - list need not to be homogenous : contains only single type of data
        - list can contain different kind of elements i.e : bool,str,int, or any type
        - list is mutable and we can modify items
        - list allows duplicate data & can have two items with same value
        - The list() python is a built-in function that works as a constructor. Lists are data structures
          in Python that are defined as dynamic arrays. These store similar types of data types such as integers,
          strings, objects, etc


"""
""" - Lists has more builtin function than that of tuple.
      We can use dir([object]) inbuilt function
      to get all the associated functions for list and tuple.

    - list() constructor returns a list. if iterable is passed as a parameter, it will create
      a list consisting of iterable's item, convert any iterable into list
"""

# The list can be created using list constructor or square brackets []....

# USING CONSTRUCTOR :
""" the constructor of a class has its class name,  Create a list by
passing the comma-separated values inside the list() """

list = list(('1','2','3'))
print(list)

# USING SQUARE BRACES [] :

list = [1,2,3]
print(list)

# USING HETEROGENEOUS :

"""Heterogeneous: The list can contain different kinds of elements 
   i.e; they can contain elements of string, integer, 
   boolean, or any type. """

list = [1.0,'hetvi',56]
print(list)

# EMPTY LIST USING LIST :
#
# mylist = list()
# print(mylist)

""" O/P : [] """

# EMPTY LIST USING [] :

mylist = []
print(list)
""" O/P : [] """

# lENGTH
list = [1, 2, 3]
print(len(list))

""" Note : whenever we try to access an item with an index more than list
           length it wil show an error 'index error'

--> the index values are always an integer.
    If we give any other type, then it will showType Error. """

""" POSITIVE INDEX """

list = [10,20,'hlmxk',6,'gjs']
print(list[2])

# Accessing element from the nested list :

l1 = [1, 2, 3, 4, ["hey", "How R You", (1, 2, 3, {"key": "value", "key2": "val"})]]
print("nested :",l1[4][2][3])

""" NEGATIVE INDEX """

list = [10,20,'hlmxk',6,'gjs']
print(list[-2])

""" SLICING """

my_list = [5, 8, 'Artist', 7.50, 'Hetvi']

# slicing first four items
print(my_list[:4])
# Output [5, 8, 'Tom', 7.5]

# it will print every second element and it will skip count 2
print(my_list[::2])
# Output [5, 'Tom', 'Emma']

# reversing the list
print(my_list[::-1])

# Iterating a list
list = [1,2,'hello',3,8]
for item in list:
    print("iterate :",item)

# APPEND : accept only one parameter and it will add calue at  the end of list

list = [1,2,3,'hello',35]
list.append('hetvi')
print("append : ",list)

# INSERT : add item at specified position in list, insert method accept two parameters position and object

list = [1,2,3,4,5,6]
list.insert(2,25)
print("Insert: ",list)

# EXTEND : it will accept list of elements and add them at the end of list we can also add another list by using this method

# mylist = list([1,2,3,'hey',4,5,6])
# mylist.extend([2,25])
# print("extend : ",mylist)

#REMOVE :removes only 1 item at a time, to remove range of element iterator is used (only removes the item which is mentioned

l = [1,2,5,6]
l.remove(6)
print(l)

# iterate :
for i in range(1,2):
    l.remove(i)

# POP :it also remove and return elements from list but by default it remove only last element from list & also pass argument by giving an index
list = [1,2,3,4,5,6]
list.pop()
print("pop :",list)

# CLEAR : remove all items from list

mylist = [1,2,3,5,2]
mylist.clear()
print("clear",mylist)

# INDEX : function to find item in list

mylist = [1,2,3,5,2]
print("find element index wise: ",mylist.index(2))

my_list1 = [1, 2, 3]

# COPY :

new_list = my_list1.copy()
print(new_list) #NEW LIST
# Output [1, 2, 3]

# making changes in the original list
my_list1.append(4)
# print both copies
print(my_list1)
# result [1, 2, 3, 4]
print(new_list)
# O/P [1, 2, 3]


"""
    1. append() : Add an element to the end of the list
    2. clear() : Removes all items from the list
    3. copy() : Returns a copy of the list
    4. count() : Returns the count of the number of items passed as
                 an argument
    5. extend() : Add all elements of a list to another list
    6. index() : Returns the index of the first matched item
    7. insert() : Insert an item at the defined index
    8. pop() : Removes and returns an element at the given index
    9. remove() : Removes an item from the list
    10. reverse() : Reverse the order of items in the list
    11. sort() : Sort items in a list in ascending order
"""

