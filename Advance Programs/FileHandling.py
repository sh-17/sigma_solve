"""
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

"""
# E.G - 1 : The open() function returns a file object, which has a read() method for reading the content of the file
f = open('myfile.txt','r')
print(f.read())

# E.G - 2 : If the file is located in a different location, we will have to specify the file path
f = open("D:\sigma_solve\Advance Programs\myfile.txt", "r")
print(f.read())

# E.G : 3 :  By default the read() method returns the whole text, but we can also specify how many characters you want to return:
f = open("myfile.txt", "r")
print(f.read(5)) # it will print first 5 letter

# E.G - 4 : By calling readline(), you can read the lines

f = open("myfile.txt","r")
print(f.readline())

# E.G - 5 : By looping through the lines of the file, we can read the whole file, line by line
f = open("myfile.txt","r")
for a in f:
    print(a)

# E.G - 6 :
"""Note: You should always close your files, in some cases, due to buffering, 
changes made to a file may not show until you close the file.
"""
f = open("myfile.txt", "r")
print(f.readline())
f.close()


""" 

To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

"""

f = open("myfile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("myfile2.txt", "r")
print(f.read())

# Note: the "w" method will overwrite the entire file.

"""

To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

"""

# f = open("demo.txt", "x")

# Create a new file if it does not exist:

# f = open("demo.txt", "w")

""" To delete a file, you must import the OS module, and run its os.remove() function """

import os
os.remove("demo.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
# Check if file exists, then delete it

import os
if os.path.exists("demo.txt"):
  os.remove("demo.txt")
else:
  print("The file does not exist")

# To delete an entire folder, use the os.rmdir() method:
#
# import os
# os.rmdir("myfolder")

""" NOTE : WE CAN ONLY REMOVE EMPTY FOLDERS """