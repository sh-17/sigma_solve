#  2. MULTILEVEL INHERITANCE : In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to
#                            a relationship representing a child and a grandfather.

class A:
    def fun1(self):
        print("class A")
class B(A):
    def fun2(self):
        print("class B")
class C(B):
    def fun3(self):
        print("class C")
ob = C()
ob.fun1()
ob.fun2()
ob.fun3()