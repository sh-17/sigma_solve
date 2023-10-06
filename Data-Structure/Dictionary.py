# DICTIONARY : STORES MULTIPLE ITEMS IN SINGLE VARIABLE

"""
    - Separated by commas and enclosed by{}
    - Values can access by using keys
    - Dictionary are in ordered collection
    - Values in a dictionary can be of any data type and not allow
      duplicate, keys can't be repeated because it is immutuable.
    - Dictionary keys are case-sensitive, the same name but different cases
      of key will be treated distinctly.
    - When you just need a sequence of elements that you can access with indexing, choose a list.
    - If you need to quickly access an element mapped to a specific unique key, choose a dictionary.

"""

# Accessing Single Value :

MyInfo = {
    'Name': 'Sheth Hetvi',
    'Profession': 'Certified Artist',
    'Skills1': 'Artist',
    'Skills2': 'Singer',
    'Passion': 'Developer',
}

print("Name :", MyInfo['Name'])
print("Profession : ", MyInfo.get('Profession'))
print("MyInfo : ", MyInfo.keys())
print("MyInfo : ", MyInfo.values())
print("Info_Key_Value : ", MyInfo.items())  # it will gives key and value

# clear (): using clear we cant see the value which is removed, items from dictionary can be deleted at once by using

MyInfo.clear()
print('clear:', MyInfo)
# using for loop
for key in MyInfo.keys():
    print(f"My {key} is: {MyInfo[key]}")

for key, value in MyInfo.items():
    print(f"My key and value {key} are: {value}")

""" Dictionary Methods """
Workshop = {
    "Name": " Hetvi ",
    "Date": "17/05/23"
}
# Update (): if item is already exits in dic else it will create a ney key and value vlaue pair
MyInfo.update(Workshop)
print(Workshop)

# setdefault() : Return the value of the  key. if the key does not exist: insert the key, with the specified value.

a = Workshop.setdefault("City", "Ahemdabad")
print("Workshop", a)

# copy() :return a copy of the dictionary

a = Workshop.copy()
print("copy", a)

# pop(): deletes the value from existing dict.. and return remaining value

Workshop.pop('Name')
print(Workshop)

# fromkeys() : Return a dictionary with the specified keys and value.

x = ('key1', 'key2', 'key3')
y = 0
dict3 = MyInfo.fromkeys(x, y)
print(dict3)

# Updating existing key's value :

MyInfo["name"] = "Sheth Hetvi"
print(MyInfo)

# Adding nested key to dictionary :

Workshop = {
    "name": " Anjli ",
    "city": "Ahemdabad",
    "Date": 17 / 5 / 2023,
}
Workshop["Contact"] = {"Owner": 9856217895}

print(Workshop)

# In order to access the value of any key in the nested dictionary, use indexing[] syntax.

print(Workshop["Contact"]["Owner"])

# Removing elements from dictionary :

# Using del keyword :
del Workshop["city"]
print(Workshop)

# Note : The del Dict will delete the entire dictionary and hence printing it after deletion will raise an error.

#defaultdict(): to handle the missing keys
from collections import defaultdict

default = defaultdict(list)
print("missing key: ",default["missing_key"])
