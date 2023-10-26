# 1. SINGLE INHERITANCE :  Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.
"""---> Main Class : Super, Base, Parent class
---> Down Class : Sub, Derieved, Child class"""

class A:
    def fun1(self):
        print("class A")
class B(A):
    def fun2(self):
        print("class B")
class C:
    def fun3(self):
        print("class C")
ob = B()
ob.fun1()
ob.fun2()