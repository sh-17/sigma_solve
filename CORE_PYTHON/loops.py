# for loop iterate through letters

for i in "heyimartist":
    print(i)

# range()
for i in range(5):
    print(i)

# list

a = ['resin','lippan','canvas']
for i in a:
    print(i)
    print()

# zip() bbne list ne combine kari ne aek format ma o/p apse

a1 = ['resin','canvas','mandala']
b2 = [1,2,3]

for a,b in zip(a1,b2):
    print(a,b)

# sort asc
numbers = [1,4,50,80,12]

for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if(numbers[i] > numbers[j]):
            temp = numbers[i]
            numbers[i] = numbers[j];
            numbers[j] = temp

print(numbers)

# reverse
for i in range(10,0,-1):
    print(i)

"""********* WHILE-LOOP (loop keeps repeating until condition return false )********"""

# ADDING NUM

myList = []
i = 0

while len(myList) < 4:
    myList.append(i)
    i += 1

print(myList)

# PRINT NUM IN SERIRES

n = 10

while n <= 100:
    print(n ,end = ",")
    n = n+10

# POP()

fruitsList = ["Mango","Apple","Orange","Guava"]

while fruitsList:
    print(fruitsList.pop())

print(fruitsList)

# COVERT DECIMAL TO BINARY

num = int(input("Enter a number: "))
b = 0
p = 1
n = num

while n>0:
    rem = n%2
    b += rem * p
    p = p*10
    n = n//2

print("Binary value: ",b)

#REVERSE NUMBER

n = int(input("Enter a number: "))
rev = 0

while n != 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

print("Reversed number:", rev)