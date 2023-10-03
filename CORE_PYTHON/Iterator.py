# NOTE : MEANING OF ITERATOR Repetitive execution of the same block of code over and over Even strings are iterable
# objects, and can return an iterator iter method is used to get an iterator ..
# iterable aek object che ae iterator ne generate kari ske

# sequence ma show thay
mystr = "hetvi"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# looping through iterator : We can also use a for loop to iterate through an iterable object

mytuple = ("hello", "world")
for x in mytuple:
    print(x)
    print()

# using while loop
num = [1,2,5,6,8,56]
myint = iter(num)

while True:
    try:
        mynum = next(myint)
        print("using while loop : ",mynum)
    except StopIteration:
        break

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to our object.

# all classes have a function called __init__(), which allows you to do initialize when the object is created.

# The __iter__() method, you can do operations (initializing etc.), but always return the iterator object itself.

# The __next__() method allows you to do operations, and return the next item in the sequence.

# Creating an iterator that returns numbers, starting with 1, and each sequence

# to create iterator we need iter and next function
class num:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 2  # (

        # + the value twice from num )
        return x


myclass = num()
myiter = iter(myclass)
print()
print("add value :",next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print()


# turn the value of PI
# import math
# num = float(input("enter num : "))
# x = math.pi
# print(x)


class num:
    def __init__(self):  # declare variable because value will start from 1
        self.a = 1

    def __iter__(self):  # iter is our object
        return self

    def __next__(self):  # method to call num
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = num()
for i in myclass:
    print(i)
