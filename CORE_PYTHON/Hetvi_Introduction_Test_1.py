# # left star
n = int(input("Enter Number:"))
for i in range(n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

"""
*
**
***
****
*****

"""

# # reverse string using slicing method
n = input("enter name :")
rev = n[::-1]
print()
print('Reverse String:', rev)
#
# """ Output : Reverse String : ereH ivteH yeH  """

n = "Hey I'm An Artist"
rev = n[::-1]
print()
print('Reverse String:', rev)

""" Output : Reverse String : tsirtrA nA m'I !yeH """

# using string join() function with reverse iterate method
a = ['a','b','c']
print(','.join(reversed(a)))

# using for loop reverse string

a = "hetvi"
b = len(a)
for i in range(b-1,-1,-1):
    print(a[i], end="")
    print()

    """
    -5-4-3-2-1 
    0 1 2 3 4 
    h e t v i """

