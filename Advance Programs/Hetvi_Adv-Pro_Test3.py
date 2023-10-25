"""
    Que 2 : Write a Python program to count the same pair in two given lists. Use map() function.
    [Take input from file] [store output in that file]
    Original lists:  [HETVI]
                                    [1, 2, 3, 4, 5, 6, 7, 8]
                                    [2, 2, 3, 1, 2, 6, 7, 9]

    Number of same pair of the said two given lists:
    4
"""

from collections import Counter
# this function takes two lists as param.. it will count the no.s of pair in the two list with same elements
def count_pairs(list1, list2):
    return sum(map(lambda x, y: 1 if x == y else 0, list1, list2))  # i used map and sum func.. to count same pairs ..

try:
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [2, 2, 3, 1, 2, 6, 7, 9]

    same_pair = count_pairs(list1, list2)

    print(f"Number of same pairs: {same_pair}")

except Exception as e:
    print(f"number of pair:{e}\n")



from collections import Counter
# this function takes two lists as param.. it will count the no.s of pair in the two list with same elements
def count_pairs(list1, list2):
    return sum(map(lambda x, y: 1 if x == y else 0, list1, list2))  # i used map and sum func.. to count same pairs ..


try:
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [2, 2, 3, 1, 2, 6, 7, 9]

    with open("input.txt", "r") as file:
        lines = file.readline()

    same_pair = count_pairs(list1, list2)

    print(f"Number of same pairs: {same_pair}")

    with open("input.txt", "a") as file:
        file.write(f"number of pair:{same_pair}\n")

except Exception as e:
    print(f"number of pair:{e}\n")


# Que : 1 Write a Python program that implements a decorator to handle exceptions raised by a
#       function and provide a default response. [HETVI]

def div_decor(func):
    def inner(a, b):
        try:
            number = func(a, b)
            return number  # Return the result of the division
        except ZeroDivisionError as e:  # taking this exception to check wether the condition is true or not
            print('Zero Division Error', e)

    return inner


@div_decor
def divide(a, b):
    return a / b  # Return the result of the division


print()
print(divide(10, 0))
