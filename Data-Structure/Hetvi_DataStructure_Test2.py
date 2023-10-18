# # Write a Python program to subtract N days from the current date. [HETVI]
# # Sample Date :
# # N = 5
# # current Date : 2015-06-22
# # 5 days before Current Date : 2015-06-17

from datetime import datetime,timedelta
Current_time = datetime.now()
print("Current date:", Current_time.date()) # current_time_date is used to extract and print only the date
new_date = (Current_time + timedelta(days=-5, hours=5)).date() # this will print date and add 5 days and subtracting 5 hours
print("date:",new_date) # printing the new_date
# print(datetime.now() + timedelta(days=5, hours=-5))

""" Exception handling """
from datetime import datetime,timedelta
try :
    Current_time = datetime.now()
    print("Current date:", Current_time.date()) # current_time_date is used to extract and print only the date
    new_date = (Current_time + timedelta(days=-5, hours=5)).date() # this will print date and add 5 days and subtracting 5 hours
    print("date:",new_date) # printing the new_date
except Exception as e:
    print("error",str(e))
# print(datetime.now() + timedelta(days=5, hours=-5))

""" Using Exception Handling & imput value from user"""

from datetime import datetime,timedelta
try:
    curr_time = datetime.now()
    print("curr date: ",curr_time.date()) # print current date

    days = int(input("enter days : "))
    # hours = int(input("enter hrs : "))

    new_date = (curr_time - timedelta(days=days)).date() # subtracting the days
    print("new_date: ",new_date)

except ValueError :
    print("invalid input") # if num is not an int then it will print this message
except Exception as e:
    print("error :",str(e))

# # Write a Python Program To get a list, sorted in increasing order by the last element in each
# # tuple from a give list of non empty tuples
# # Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

mylist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]  # taking value as tuple inside the list
empty_list = []
for i in mylist:
    empty_list.append((i[0], i[1]))
    empty_list.sort()
print('sorting value from last in Tuple : ', empty_list)

"""
    Using ItemGetter we can sort Values in Tuple
    What is ItemGetter Function : Function from operator module which allows you to specify
    which element in a tuple you want to sort by
"""
from operator import itemgetter
def sort_tuples(tuples):
    # Sort the tuples by the second item using the itemgetter function
    return sorted(tuples, key=itemgetter(1))
# Test the function
tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_tuples(tuples))

""" # Using Function """

def sort_element(tuples_list):  # sort the value from last
    # sorting function that returns the last element of each tuple
    def last_element(tuple):  # getting the value from last
        return tuple[-1]

    # Sort the list of tuples using the custom sorting function
    sorted_list = sorted(tuples_list, key=last_element)
    return sorted_list
list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Calling the function to sort list
result = sort_element(list)

# Print the sorted result
print("using function sorting the value from last : ",result)

from operator import itemgetter


def sort_tuples(tuples):
    # Sort the tuples by the second item using the itemgetter function
    return sorted(tuples, key=itemgetter(1))

""" 
itemgetter(1) which means we want sort the tuples based on 
2nd element from index1 of each tuple

It's sorted in ascending order by the second element of each tuple, which explains why
(2, 1) comes first and (2, 5) is last in the sorted list.

"""

tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_tuples(tuples))

# Using List Comprehension
tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_tuples = [t for t in sorted(tuples, key=lambda x: x[-1])]
print("list comprehension : ", sorted_tuples)

""" 
lambda function is used as key argument for the sorted function.. 'x[-1] is used to access the last element of tuple
sort the tuple in ascending order

"""
