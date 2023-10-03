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

# nested if-else

num = int(input("enter number :"))

if num > 0 and num < 10:
    if num < 5 :
        print("less than 5")
    else:
        print("greater than 5")
elif num >= 10:
    print("greater than or equal 10")
    if num >= 15:
        print("greater than 15")
    else:
        print("less than 15")
else:
    print("ent num again: ")
