a = 80
if a % 2 == 0:
    print("even number")
else:
    print("odd number")
print(a)


# elif
num = int(input("enter number :"))
if num % 2 == 0:
    print("even number")
elif num % 2 !=0:
    print("odd number")
else:
    print(num)

# prime number

num = int(input("enter number :"))

if num > 0:
    for i in range(2,num):
        if num % 2 == 0: # num bija num
            print('prime number')
            break
        else:
            print('not prime number')
            break

# another method

a = int(input("ent num:"))
b = int(input("ent num:"))
print('greater')if a > b else print('equal') if a == b else print('smaller')
