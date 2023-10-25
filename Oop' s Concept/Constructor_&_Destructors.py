"""""""""
==> What is Method ?

    - Methods are same as function we can also call method through object

==> What is Constructor ?

    - Constructor is also type of method but we don't need to call constructor
    - When we create a class constructor automatically calls the object
    - Constructors are generally used for instantiating an object.
    - Constructors are special methods used to initialize objects whereas
      methods are used to execute certain statements.
    - In Python the __init__() method is called the constructor and
      is always called when an object is created.

--> Type of Constructor :

    - Default Constructor - Doesn't accept any arguments, it defines only one arg.. which is reference to the instance
                            being constructed
    - Parameterized Constructor - takes first as argu.. as reference to the being instance being
                                  contructed known as self and the rest of argu.. provided by the programmer

"""""""""

""" E.G-1 : Using Default Constructor """

class Artist:
    # Defualt Constructor
    def __init__(self):
        self.art = "Artist"

    # a method for print data members
    def print_artist(self):
        print(self.art)

# creating object of class
obj = Artist()
obj.print_artist()


""" E.G-2 : Using Parameterized Constructor"""

class addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self,f,s):
        self.first = f
        self.second = s
    def display(self):
        print("First Number = " + str(self.first))
        print("Second Number = " + str(self.second))
        print("Total = " + str(self.answer))
    def calculate(self):
        self.answer = self.first + self.second
        # self.answer = self.first * self.second



# creating object of the class
# this will invoke parameterized constructor
obj1 = addition(10,30)

# creating second object of same class
obj2 = addition(10,30)

obj1.calculate()
obj2.calculate()
# display result of obj1
obj1.display()
# display result of obj2
obj2.display()



"""


===> Advantages of using constructors in Python:
1. Initialization of objects: Constructors are used to initialize the objects of a class. They allow you to set default 
                              values for attributes or properties, and also allow you to initialize the object with custom data.
2. Easy to implement: Constructors are easy to implement in Python, and can be defined using the __init__() method.
3. Better readability: Constructors improve the readability of the code by making it clear what values are being 
                       initialized and how they are being initialized.
                       
4. Encapsulation: Constructors can be used to enforce encapsulation, by ensuring that the object’s attributes are 
                  initialized correctly and in a controlled manner.

===> Disadvantages of using constructors in Python:

1. Overloading not supported: Unlike other object-oriented languages, Python does not support method overloading. 
                              This means that you cannot have multiple constructors with different parameters in a single class.
                              
2. Limited functionality: Constructors in Python are limited in their functionality compared to constructors in other 
                          programming languages. For example, Python does not have constructors with access modifiers
                          like public, private or protected.
                          
3. Constructors may be unnecessary: In some cases, constructors may not be necessary, as the default values of attributes 
                                    may be sufficient. In these cases, using a constructor may add unnecessary complexity
                                    to the code.

"""


""" 

====> Destructor : Destructors are called when an object gets destroyed. In Python, destructors are not needed as 
                   much as in C++ because Python has a garbage collector that handles memory management automatically.
                   
    -  The __del__() method is a known as a destructor method in Python. It is called when all references to the object 
       have been deleted i.e when an object is garbage collected. 
                        
    Example: def __del__(self):
    # body of destructor
    
Note : A reference to objects is also deleted when the object goes out of reference or when the program ends. 

"""
# E.G : 1
# By using del keyword we deleted the all references of object ‘obj’,
# therefore destructor invoked automatically.

class Employee:

    # Initializing
    def __init__(self):
        print()
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Employee()
del obj

# --> Note : Destructor was called after the program ended
