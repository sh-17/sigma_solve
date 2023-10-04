# # left star
# # n = int(input("Enter Number:"))
# for i in range(0,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#
# # output :
# """
# *
# **
# ***
# ****
# *****
#
# """
#
# # reverse string
# n = input("enter name :")
# rev = n[::-1]
# print()
# print('Reverse String:', rev)
#
# """ Output : Reverse String : ereH ivteH yeH  """
#
#
# n = "Hey I'm An Artist"
# rev = n[::-1]
# print()
# print('Reverse String:', rev)
#
# """ Output : Reverse String : tsirtrA nA m'I !yeH """

# using string method
a = ['a','b','c']
print(','.join(reversed(a)))

# using for loop reverse string

a = "hetvi"
b = len(a)
for i in range(b -1, -1, -1):
    print(a[i], end="")

