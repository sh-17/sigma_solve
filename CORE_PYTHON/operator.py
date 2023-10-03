# Realtional & Comaparision Operations 

a = 5
b = 6
print(a<b)

a = 5
b = 6
print()
print(a<=b)

a = 5
b = 6
print()
print(a>=b)

#Comparison Operator
a=10
b=20

if(a > b):
    print("a is greater !")
elif(a < b):
    print("b is greater !")
else:
    print("a and b is equal !")
"""
Types of comparison operator :-
1) Equal to (==)
2) Not equal to (!=)
3) Greater than (>)
4) Less than (<)
5) Greater than or equal to (>=)
6) Less than or equal to (<=)
"""

# Logical Operator

a = 2
b = 3
c = 9
print()
print(a<b and c )

a = 2
b = 3
c = 89
d = 1
print()
print(a<b or c or d )

a = 9
b = 5
print()
print(not(a>b))

a = True
b = False

if a and b:
    print("Both are True")
else:
    print("Either a or b is False")
"""
1) and :- 
Returns True if both operands are True, and False otherwise.
2) or :-
Returns True if either operand is True, and False otherwise.
3) not :-
Returns True if the operand is False, and False otherwise.
"""

# Bitwise Operator

a = 10
b = 15
print()
print(a&b)


#Identity Operator
a = 10
b = 10

if a is b:
    print("a and b are the same object")
else:
    print("a and b are not the same object")
"""
1) is :- 
Returns True if the two operands are the same object, 
and False otherwise.
2) is not :-
Returns True if the two operands are not the same object, 
and False otherwise.
"""

#Membership Operator
a = [5,10,15,30,5,45]
b = 10

if a in b:
    print("number in List")
else:
    print("not in List")
"""
1) in :- 
Returns True if the left operand is a member of
the right operand, and False otherwise.
2) not in :-
Returns True if the two operands are not 
the same object, and False otherwise.
"""