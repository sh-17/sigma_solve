"""
1. Public : members are accessible from outside the class, By default, all members of a class are public,
            which means they can be accessed from anywhere.

2. Private : members cannot be accessed (or viewed) from outside the class

3. Protected :  members cannot be accessed from outside the class, however, they can be accessed in inherited classes.
                (we can call protected variables inside the inherited class )

"""
# public class
class A:
    def xyz(self):
        print("Hi")

class B:
    def abc(self):
        print("hello")
        ob1=A()
        ob1.xyz()
ob = A()
ob.xyz()

ap = B()
ap.abc()

# Protected Members

class A:
    def _xyz(self):
        print("hey")

class B:
    def abc(self):
        print()
        print("how r you")
        ob1=A()
        ob1._xyz()


# ob = A()
# ob.xyz()

ap = B()
ap.abc()

"""
if we call the object outside the class it will show an error becuase protect members 
cannot be count outside of the class

Traceback (most recent call last):
  File "D:\sigma_solve\Oop' s Concept\Access_Modifiers.py", line 39, in <module>
    ob.xyz()
AttributeError: 'A' object has no attribute 'xyz'. Did you mean: '_xyz'?"""

# Private Class : which we can call object inside that private function only

class A:
    def __xyz(self):
        print("hey")
    def lmn(self):
        print("bye")
        a = A()
        a.__xyz()

ob = A()
ob.lmn()