"""
====>  Decorators means to create or to add some thing more attractive or presentable

===> Decorators are very powerful and useful tool in Python since it allows
     programmers to modify the behavior of function or class.

===> we can apply decorator function on method

1) What is Decorators ?
   --> Any callable python object that is used to modify a function or a class
       (it will def a function , inside that it will add some functionalities and show the result )

2) Type of decorator : 1) Function Decorator 2) Class Decorator

3) steps
            - need to take a function as parameter
            - add functionality to the function
            - function need to return another function

"""

"""BASIC EXAMPLE : Function using function as parameters"""


def func1():
    print('hi i m func1')


def func2(func):
    print('hi i m func2 now i will call func1')


func2(func1)

""" EXAMPLE 1 :  FUNCTION WITHOUT PARAMTER INSIDE THIS FUNCTION WHICH IS DECORATED IT DOSENT CONTAIN ANY PARAMETERS"""


# Print a string in uppercase
def decor_upper(func):  # to decorate the function we need to pass that function to decorator function
    def inner():
        str1 = func()
        return str1.upper()

    return inner  # calling the inner function which will return the refrence of function


""" INSIDE THIS FUNCTION WHICH IS DECORATED IT DOSENT CONTAIN ANY PARAMETERS"""


@decor_upper  # this called decorators which means we are decorating this print_str function
def print_str():
    return "good morning"


print("Example 1: ", print_str())  # it will show decorated function
# a = decor_upper(print_str)# calling this upper function
# print(a())


""" EXAMPLE 2 : FUNCTION WITH PARAMTER FUNCTION WHICH IS DECORATED AND ALSO CONTAIN ANY PARAMETERS"""


def div_decor(func):
    def inner(x, y):  # taking twi parameters
        if y == 0:  # if value becomes zero it will print below line and if it is true then it will comeout the func
            return "give proper input"
        return func(x, y)

    return inner


@div_decor
def div(a, b):
    return a / b


print("Example 2: ", div(4, 0))  # it will show an zero division error because zero cant divide

""" EXAMPLE : 3 CREATING MULTIPLE DECORATORS """


def upper_decor(func):
    def inner():
        str1 = func()
        return str1.upper()

    return inner


def split_decor(func):
    def wrapper():
        str2 = func()
        return str2.split()

    return wrapper


@split_decor
@upper_decor
def ordinary():
    return "good morning"


print("Example 3: ", ordinary())

""" EXAMPLE 4: How Multiple Decorator function works """


def upper_decor(func):
    def inner():
        return "first " + func() + " first"

    return inner


def split_decor(func):
    def wrapper():
        return "second " + func() + " second"

    return wrapper


@upper_decor
@split_decor
def ordinary():
    return "good morning"


print("Example 4: ", ordinary())

""" EXAMPLE 5 : If a Decorator contains a parameter then how to use it """


def outer(expr):
    def upper_d(func):
        def inner():
            return func() + expr

        return inner

    return upper_d


@outer(" hetvi")  # taking an expression
def ordinary():
    return "good morning"


print("Example 5: ", ordinary())

""" if i use the param... in the decor.. function """

""" 
    *args:
    *args is used to send a non-keyworded variable length argument list to the function. 

    The syntax is , the symbol * followed by a name.by convention, it is often used with the word args.

    Using the *, the variable that we associate with the * becomes an iterable meaning you can  iterate over it.
"""

""" EXAMPLE 6: GENERAL FUNCTIONS  """


def div_Decorator(func):
    def inner(
            *args):  # can use multiple aruguments using *args (using args because if one function there is 2 value and in another func.. there is 3  )
        list1 = []
        list1 = args[1:]  # it will give list of parameters ( *args : function to take variable length argument )
        for i in list1:
            if i == 0:
                return "give proper input!!!"
            return func(*args)

    return inner


@div_Decorator
def divide(a, b):
    return a / b


@div_Decorator
def add(a, b, c):
    return a + b + c


print("Example 6: ", divide(2, 6))
print("Example 6: ", add(9, 7, 6))

""" EXAMPLE 7: CLASS DECORATORS """
import functools


def decorator(func):
    @functools.wraps(func)  # it will copy the lost data from the undecorated function
    def inner():
        str1 = func()
        return str1.upper()

    return inner


@decorator
def greet():
    return "good morning"


print("Example 7: ", greet.__name__)  # it will print func.. name


# Using Decorator methods
def check_name(method):
    def inner(name_ref):
        if name_ref.name == 'hetvi':
            print("Hey! my name is also same")
        else:
            method(name_ref)

    return inner


class printing:
    def __init__(self, name):  # self refers to the instance of class to the object itself
        self.name = name

    @check_name
    def print_name(self):
        print("entered user name is : ", self.name)


p = printing("kriya")
p.print_name()


# call method

class printing:
    def __init__(self, name):  # self refers to the instance of class to the object itself
        self.name = name

    def __call__(self):  # call is special method which will execute when we call object in function form
        print("entered user name is : ", self.name)


p = printing("kriya")
p()


# class Decorator method

class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        str1 = self.func()
        return str1.upper()


@Decorator
def greet():
    return "good morning"


print(greet())

"""E.G. : 2"""

class Check_div:
    def __init__(self,func):
        self.func = func # here checking wether the second parameter is zero or not
    def __call__(self, *args, **kwargs):
        if args[1] == 0:
            print("you cant devide change the input!!")
        else:
            self.func(*args,**kwargs)
@Check_div
def div(a,b):
    return a/b
print(div(10/2))

"""EXAMPLE :"""

def decor(func):
    def inner():
        return func().upper()

    return inner


def decor2(func):
    def inner():
        return func().split()

    return inner

@decor
@decor2
def decor3():
    name = input("ent name: ")
    s_name = input("ent s name: ")
    # f_name = input("ent f name: ")
    f_name = name + " " + s_name
    return f_name


# decor3 = decor2(decor(decor3))
print(decor3())

"""
output: 
ent name: hetvi
ent s name: sheth
['HETVI', 'SHETH']

"""