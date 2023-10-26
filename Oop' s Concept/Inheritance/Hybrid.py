# 5. HYBRID INHERITANCE : eg: one base class -- child class then that 3 class inherit in another class called parent class

class A:
    def fun1(self):
        print("class A")
class B(A):
    def fun2(self):
        print("class B")
class C(A):
    def fun3(self):
        print("class C")
class D(B,C):
    def fun4(self):
        print("class D")

ob = D()
ob.fun1()
ob.fun2()
ob.fun3()
ob.fun4()