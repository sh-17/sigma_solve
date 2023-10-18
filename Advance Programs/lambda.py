"""
  Lambda Function : Function Which Defines Without having any name it also called as anonymous function

            -   this function can be used when we need function for short period of time..
            -   it can be used as the arguments on higher orderd functions
                (which means use the function use another function as arguments in that case we use
                lambda function as high-orderd function )

            -   Built - In - Functions : Map, Filter, Reduce....
"""
x = lambda a,b,c : a+b+c
print(x(5,6,2))

#Using Lambda list comprehension:

tables = [lambda x=x: x*10 for x in range(1,11)]
for table in tables:
    print (table())

# Using Upper():

str = 'hey! I m An Artist'
upper = lambda string:string.upper()
print(upper(str))

# Using Lambda Function

def my_func (n):
    return lambda a : a*n
mytray = my_func(6)
print(mytray(10))

# Python Lambda with Multiple Statments

""" Lambda Functions do not allow multiple statments, we can create two lambda functions and then
call the other lambda function as a parameter to the first function """

l = [[1,2],[5,2,6],[8,6,7,8]]

sortlist = lambda x: (sorted(i) for i in x) # sorting the each sublist For each sublist i in x, it sorts the elements in ascending order using the sorted function.
second_largest = lambda x, f: [y[len(y)-2] for y in f(x)]
res = second_largest(l, sortlist)
print(res)

# using lambda function with Filter()

""" filter function filter the elements of iterable depending on a function that tests each element
    in sequence to be true or not """

a = [10,20,30,40,50]
def highest_rank(n):
     if n>=60:
         return True
# result = list(filter(lambda n : (n>60),a))
result = list(filter(highest_rank,a)) # by using list it will show output in list
for i in result:
    print(i)

# Using Lambda Function with Map() : Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.). It is used when you want to apply a single transformation function to all the iterable elements.
# The iterable and function are passed as arguments to the map in Python.

""" What is the use of mapping function?
    function executes a specific function on each element of the iterable 
    and change the elements """

a = [10,20,30,40,50]
# def inc(n):
#     return n+2
result = map(lambda  n : n+2 , a) # inside this inc function it will execute each element from a variable.
print(result)
for i in result:
    print(i)



a = [10,20,30,40,50]
b = [1,2,3,4,5]
result = map(lambda n,m: n+m, a, b) # n parameter define as a and m defines as b
print(result)
for i in result:
    print(i)

# Reduce : function ud=sed to reduce a sequence of elements to a single
# value by processing elements according to a function supllied it will
# return single value

# --> for using this funcion we need to import functools module
""" Syntax : from functools import reduce
                reduce(function_name, sequence """
from functools import  *
a = [10,20,30,40,50]
result = reduce(lambda n,m: n+m,a)
print(type(result))
print(result)