
# DIFF BETWEEN LIST AND GENERATOR COMPREHENSION : GENERATORS DOESNT ALLOCATE MEMORY FOR THE WHOLE LIST INSTEAD THEY
# generate each value one by one which is why they are memory efficient

""" 1). LIST COMPREHENSION """
# Syntax: [ expression for item in iterable ] -----> [l for l in range(1,11)]

"""
 ---> List comprehenion means it will create new list from an iterable object which statisfy thw given condition   
 ---> we can use this if conditional statment with list comprehension
            - [ expression for item in iterable if conditional ] 
            - [ expression if conditional else statment for item in iterable ] 
 
            - expression : the operation which we want to perform on each element
            - item : each item represent in iterable
            - iterable : the data which we want to iterate
            - condition : used for include and exclude items from the new list
"""
# Diff of using comprehension and without using comprehension

l = [1,5,4,3,6,9,45,63,89,15,30]
div_by_3 = []
for item in l:
    if item%3 == 0:
        div_by_3.append(item)
print("without using comprehension : ",div_by_3)
print("using comprehension: ",[item for  item in l if item%3==0])


# Example 1: Generating an Even list WITHOUT using List comprehensions
l = [i for i in range(1,12) if i%2==0 ]
print(l)

# Example 2: Generating Even list using List comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Example 3: Square Number using comprehension

list_using_comp = [var ** 2 for var in range(1, 10)]

print("Output List using list comprehension:",
      list_using_comp)

""" 2) DICTIONARY COMPREHENSION """
""" output_dict = {key:value for (key, value) in iterable if (key, value 
    satisfy this condition)} """

d = { i:f"item{i}"for i in range(1,10) }
print(d)

# Example 1: Generating odd number with their cube values without using dictionary comprehension


input_list = [1, 2, 3, 4, 5, 6, 7]

output_dict = {}

for var in input_list:
    if var % 2 != 0:
        output_dict[var] = var ** 3

print("Output Dictionary using for loop:", output_dict)

# Example 2 : using comprehension

input_list = [1, 2, 3, 4, 5, 6, 7]

dict_using_comp = {var: var ** 3 for var in input_list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:", dict_using_comp)

"""     
        It initializes an list containing numbers from 1 to 7. It then constructs a new
        dictionary using dictionary comprehension. For each odd number var in the 
        list, it calculates the cube of the number and assigns the result as the value to
        the key var in the dictionary.
"""

""" 3) SET COMPREHENSION """

sqr = {x**2 for x in [1,2,3,4,4,5,5,5]}
print("Square: ",sqr)

# Example 1 : Checking Even number Without using set comprehension

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

output_set = set()

for var in input_list:
    if var % 2 == 0:
        output_set.add(var)

print("Output Set using for loop:", output_set)



#USING COMPREHENSION

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:",
      set_using_comp)

""" GENERATOR COMPREHENSION : A Python generator function allows you to declare a function that behaves like an iterator, providing a faster and easier way to create iterators. They can be used on an abstract container of data to turn it 
    into an iterable object like lists, dictionaries and strings
"""

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_gen = (var for var in input_list if var % 2 == 0)

print("Output values using generator comprehensions:", end=' ')

for var in output_gen:
    print(var,end=' ')