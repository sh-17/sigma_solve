"""
Polymorphism : The word polymorphism means having many forms. In programming, polymorphism means the same function name
               (but different signatures) being used for different types. The key difference is
               the data types and number of arguments used in function.

two methods : 1. Overloading(Operator, Function) : function can be called with different number of arguments

              2. Overriding :  Multiple function with same name and same number of parameters
"""


# Method Overloading : Python dosent support this method but using using different methods we can overload methods
# without argument we can pass ,or we pass one value or two vaule argument will call,
# if we don't pass any value then also it will be call and this is the main purpose of overloading method

class method_overloading:
    def method(self, x=None, y=None):
        if x == None and y == None:
            print("helo this is python polymorphism")  # First method
        elif x != None and y == None:
            f = 1
            for i in range(1, x + 1):  # second method
                f = f * i
            print("Factorial is : ", f)
        else:
            print("Addition is: ", x + y)  # third method


ob = method_overloading()
ob.method()
ob.method(5)
ob.method(15, 65)  # one method calls in different ways

"""
--> Method Overriding : When same name and same parameters (when two funcs...)comes together in same crieteria then it will decide which one call
    - local function override to the previuos function and call itself

    - if there are same func.. name then it will only call that func which we had call inside object first
"""

class A():
    def Hello(self):
        print("Hi")
class B(A):
    def Hello(self):
        print()
        print("Hey")
    def xyz(self):
        print("bye")
obj = A()
obj.Hello()

"""
---> Operator Overloading : using special methods we can overload the operators

"""

class Employee:
    leaves = 8

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
    def printdetails(self):
        return f"the name is{self.name}, Salary is {self.salary} and role is{self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.leaves=newleaves
    def __add__(self, other):
        return self.name + other.name
    def __repr__(self):
        return f"Eployee({self.name},{self.salary},{self.role})"
emp1 = Employee("hetvi ",5000,"developer")
# emp2 = Employee("Kashvi",500,"Cleaner")
print(emp1)


