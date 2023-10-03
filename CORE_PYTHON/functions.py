# You can add as many arguments as you want, just separate them with a comma.

""" If we do not include any return statement in function, it automatically returns None.
So, in Python function always returns a value.

- A function can take an unlimited number of arguments.

- A Python function can return multiple values

"""


# function with one argument Example :
def my_fun(fname):  #fname is argument,
    print(fname +"ART")
my_fun("Resin ")
my_fun("Canvas ")
my_fun("Mandala ")
# This function expects 2 arguments, and gets 2 arguments:

def my_fun(fname,lname):  #fname is argument,
    print(fname +" "+lname)
my_fun("I Love to do","Art")

# Arbitary Arguments *args : if the num of arguments is unknown add a * before the parameter name

def my_fun(*Art):
    print("The best art is " +Art[1])
my_fun("MandalaArt","ResinArt")

# Keyword Arguments : we can also send the arguments with the key and value

def my_func(art1,art2,art3):
    print("Best Art is " + art3 )
my_func(art1 = "Resin",art2 = "madala", art3 = "fluid")

# Arbitary Keyword Arguments **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add
# two asterisk: (**)before the parameter name in the function definition.

def my_func(**Art):
    print("best art is " + Art["art2"])
my_func (art1="resin ",art2 ="mandala",art3= "canvas" ,art4="fluid")


# Default Parameter Value : If we call the function without argument, it uses the default value:

def my_func(Art = "Resin Art"):
  print("I am best in " + Art)

my_func("Mandala Art")
my_func("Fluid Art")
my_func()
my_func("Canvas Painting")

# Passing list as argument :  if you send a List as an argument, it will still be a List when it reaches the function

def my_func(Art):
    for x in Art:
        print(x)
Artist = ["Resin","Mandala","Fluid"]

my_func(Artist)

# Return Value : it will multiply and return thr value

def my_func(x):
    return 5 * x    #in this it will multiply by 5
print(my_func(6))

# Pass Statment : function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
    pass
# Having an empty function it will raise an error without the pass statement

# Recursive Function : A process in which function calls itself

def recursion(k): # use k as vairable as data which minus the value (-1) everytime when we recurse
    if(k>0):
        result = k + recursion(k-1)
        print(result)
    else:
        return  0
    return result
print("\nRecursion Example Results")
recursion(5)

# **Example 2**
def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = 5
print(f"fact of {num} is {factorial(num)}")

#** Example 3**

def fibbonacci(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonacci(n - 1)+fibbonacci(n - 2)
num = 10
print("fibonacci")
for i in range (num):
    print(fibbonacci(i),end="")

"""

-> Main 2 Types of Function :-
    1)Built-in Function
        Example - max(), min(), print(), len(), input()        
    2)User Define Function

-> Two Types of user define function :-
    i)Default Function (No Argument)
        Example - def class(): , def Test(): 
    ii)Parameterised Function (Single or Multiple Argument)
        Example - def class(a): , def Test(x,y,z):

"""