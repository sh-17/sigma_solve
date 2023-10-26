"""
4. HIERARCHICAL INHERITANCE : When a class can be derived from more than one base class this type of inheritance is
called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the
derived class. AL INHERITANCE : opposite of multiple inh.... when one class is inherit inside multiple class call
hirechical

- When more than one derived class are created from a single base this type of inheritance is called hierarchical
inheritance. In this program, we have a parent (base) class and two child (derived) classes.
"""
class A:
    def fun1(self):
        print("class A")
class B(A):
    def fun2(self):
        print("class B")
class C(A):
    def fun3(self):
        print("class C")
ob = C()
ob.fun1()
ob.fun3()