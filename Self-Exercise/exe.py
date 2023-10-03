# 1. Add logic to print two lines. The first line should contain the result of
# integer division,  a//b . The second line should contain the result of float division, a/b

a = 3
b = 5
print("Int: ",a//b)
print("Float: ",a/b) #--> O/P : 0 , 0.6

# 2. Print the Sqaure of each num in separate line

a = 5   # O/P : 0,1,4,9,16
for i in range (a):
    print(i*i)

# 3. check condition even odd
n = int(input('enter num: '))
if n % 2 == 1 or n in range(5, 21):
    print("Weird")
else:
    print("Not Weird")

# leap year
def leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 100 !=0 and year % 4 == 0:
        leap = True

    return leap

year = int(input('enter year: '))
print(leap(year))
#

num = int(input('enter num:'))
for i in range(1, num+1):
    print(i,end="")