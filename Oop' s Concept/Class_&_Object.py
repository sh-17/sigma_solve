"""
What is Class & Object ?

    - Inside Class we can create multiple Functions, variable , can define variable
    - Class is blueprint of object using class we create objects
    - By using class we can call the object
    - we def methods inside the class only

"""

class Func:
    a = 10
    b = 10
    def sum(self):
        print(30+20)
func = Func() # created an object
func1 = Func()
print(func.a) # calling a func
print(func1.b)
func.sum(); # calling Function
