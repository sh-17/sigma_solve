# def check_status(a, b,flag):
#     if ((a >= 0 and b < 0 ) and flag is False):
#         return True
#     if ((a < 0 and  b >= 0) and flag is False):
#         return True
#     if ((a < 0 and b < 0) and flag is True):
#         return False
#
# def friends(a, b):
#     if a == True and b == True:
#         return True
#     if a == False and b == False:
#         return True
#     return False
#
# n = int(input('enter num: '))
# def pos (n) :
#     n -= 1
#     while n >= 0:
#         print(n,end="")
#         n-=1
# def neg (n):
#     while n <= 0:
#         print(n,end="")
#         n += 1
#
# # Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).
# n = int(input("enter :"))
#
# def int(x):
#     start = 1
#     jump = 1
#     while jump <= x:
#         print(jump,end=" ")
#         start += 1
#         jump = start**2
# int(n)
#
# # use of slicing and function create a str should contains lowercase without using method
#
# str = (input("enter str :"))
# def cat_hat(str):
#     cat = 0
#     hat = 0
#     for i in range(0, len(str) - 2, 1):
#         if str[i: i + 3] == "cat":
#             cat += 1
#         if str[i: i + 3] == "hat":
#             hat += 1
#     if cat == hat:
#         return True
#     return False
# print(str)
#
#
# """list = ("hetvi")
# reverse_list = []
#
# for i in list:
#     reverse_list.insert(0,i)
# for i in reverse_list:
#     print(i,end="")"""
#
# def swapPosition(list, num1, num2):
#     list[num1], list[num2] = list[num2], list[num1]
#     return list
# List = [1, 5, 6, 56, 54, 965]
# num1, num2 = 1, 7
# print(swapPosition(List, num1, num2))
#
#
# # """ using pop """
# def swapPositon(list,num1,num2):
#     firt = list.pop(num1)
#     second = list.pop(num2-1)
#
#     list.insert(num1,second)
#     list.insert(num2,firt)
#     return list
# List = [1,2,3,6,5,4]
# num1 , num2 = 1,5
# print(swapPositon(List,num1,num2))
#
# # cube form triangle
# n = int(input("enter : "))
# n = 5
# def triangle(n):
#     for i in range(0, n + 1):
#         for j in range(1, i + 1):
#             print("*", end="")
#         for j in range(1, n):
#             print("*", end=" ")
#         print()
# triangle(n)
#
# # Triangle
#
# rows = int(input("Enter number of rows: "))
#
# k = 0
#
# for i in range(1, rows + 1):
#     for space in range(1, (rows - i) + 1):
#         print(end="  ")
#
#     while k != (2 * i - 1):
#         print("*", end="")
#         k += 1
#
#     k = 0
#     print()
#
# # program to calculate the sum of numbers
# # until the user enters zero
# total = 0
# n = int(input("enter num : "))
# while n != 0:
#     total += n # we can also write like total = total + n
#     n = int(input("enter num:"))
# print('total: ',total)

# n = 5
# for i in range(0,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

a = 5
for i in range(0,a+1):
#     for j in range(0,i+1):
#         print("*", end="")
    for j in range(0,a-i):
        print("*",end="")
    print()



