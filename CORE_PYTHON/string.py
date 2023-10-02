# captitalize() : first string capitle

str = "hey i m artist"
print(str.capitalize()) 

# casefold () all letters small

str = "hey i m aRtist"
print(str.casefold()) 

# center () it will add # on left n right side 

str = "hey i m artist"
print(str.center(20,'#')) 

# count() : returns the value of repeated word inside the str 

str = "hey ,hey i m artist"
print(str.count("hey")) 

# find() it will find text

str = "hey i m artist"
print(str.find("i")) 

#endwith () it will show ending word

str = "hey i m artist"
print(str.endswith("artist")) 

#expandtabs() makes space

str = "h\te\ty\ti\tm\t artist"
print(str.expandtabs()) 

#index()

str = "hey i m artist"
print(str.index("i"))
print(str.index("i", 2, 6)) 

#isalnum3 () : returns true if all the charecters are alphanumeric

str = "hello96hetvi"
print(str.isalnum())

# isalpha() : return true is str has only alphabets 

str = "hello96hetvi"
print(str.isalpha())

# isdecimal() : return true if there is only num
str = "35"
print(str.isdecimal())

# slicing o/p : llo

a = "hello, hetvi"
print(a[2:5]) 

# from start o/p : hello
a = "hello, hetvi"
print(a[:5])

# after first 3 word
a = "hello, hetvi"
print(a[3:]) 

# negative index o/p : het 'o':-5, 'v':-2 
a = "hello, hetvi"
print(a[-5:-2]) 

# Concatentation :  ( NOTE : we can not combine strings & numbers)means combine 2 strings you can use the + operator

#add space : 
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#But using format() method we can combine strings & numbers

age = 22
txt = "My name is hetvi, and I am {}"
print(txt.format(age))