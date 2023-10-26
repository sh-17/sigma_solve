# 3. MULTIPLE INHERITANCE : when any two child class inherit in one parent class
#
#     - When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features
#       of the base classes are inherited into the derived class.

class A:
    def fun1(self):
        print("class A")
class B:
    def fun2(self):
        print("class B")
class C(A,B):
    def fun3(self):
        print("class C")
ob = C()
ob.fun1()
ob.fun2()
ob.fun3()