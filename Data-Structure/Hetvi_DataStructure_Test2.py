# Write a Python program to subtract N days from the current date. [HETVI]
# Sample Date :
# N = 5
# current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17

import datetime

N = int(input("Enter number of days:"))  # user will input num of days
current_date = (datetime.datetime.now())  # Current Date
subtracted_days = current_date - datetime.timedelta(days=N)  # Subtracting the Days
print("The date", N, "days before was ", str(subtracted_days))

# using Exception Handling

import datetime

try:
    N = int(input("Enter number of days: "))  # user will input num of days
except ValueError as error:  # if its not an int then it will show the print message
    print("enter a valid int")
else:
    current_date = datetime.datetime.now()  # Current Date
    subtracted_days = current_date - datetime.timedelta(days=N)  # Subtracting the Days
    print("The date", N, "days before was ", (subtracted_days))

# Write a Python Program To get a list, sorted in increasing order by the last element in each
# tuple from a give list of non empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

mylist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]  # taking value as tuple inside the list
empty_list = []
for i in mylist:
    empty_list.append((i[0], i[-1]))
    empty_list.sort()

print('sorting value from last in Tuple : ', empty_list)


# Using Function

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
