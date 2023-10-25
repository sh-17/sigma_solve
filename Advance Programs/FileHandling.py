"""The key function for working with files in Python is the open() function.

Opening Files in Python
The open() Python method is the primary file handling function. The basic syntax is:

file_object = open('file_name', 'mode')

The open() function takes two elementary parameters for file handling:

The file_name includes the file extension and assumes the file is in the current working directory.
If the file location is elsewhere, provide the absolute or relative path.

2. The mode is an optional parameter that defines the file opening method.

'r'	Reads from a file and returns an error if the file does not exist (default).
'w'	Writes to a file and creates the file if it does not exist or overwrites an existing file.
'x'	Exclusive creation that fails if the file already exists.
'a'	Appends to a file and creates the file if it does not exist or overwrites an existing file.
'b'	Binary mode. Use this mode for non-textual files, such as images.
't'	Text mode. Use only for textual files (default).
'+'	Activates read and write methods.

The mode must have exactly one create(x)/read(r)/write(w)/append(a) method, at most one +.
Omitting the mode defaults to 'rt' for reading text files.

Behavior	Modes
Read	r, r+, w+, a+, x+
Write	r+, w, w+, a, a+, x+
Create	w, w+, a, a+, x, x+
Pointer Position Start	r, r+, w, w+, x, x+
Pointer Position End	a, a+
Truncate (clear contents)	w, w+
Must Exist	r, r+
Must Not Exist	x, x+
Read Mode
The read mode in Python opens an existing file for reading, positioning the pointer at the file's start.

Note: If the file does not exist, Python throws an error.

--> To read a text file in Python, load the file by using the open() function:

f = open("<file name>")

--> The mode defaults to read text ('rt'). Therefore, the following method is equivalent to the default:

f = open("<file name>", "rt")

--> To read files in binary mode, use:

f = open("<file name>", "rb")

--> Add + to open a file in read and write mode:

f = open("<file name>", "r+")  # Textual read and write

f = open("<file name>", "rt+") # Same as above

f = open("<file name>", "rb+") # Binary read and write

--> In all cases, the function returns a file object and the characteristics depend on the chosen mode.

--> Note: Refer to our article How to Read From stdin in Python to learn more about using stdin to read files.

--> Write Mode
        - Write mode creates a file for writing content and places the pointer at the start. If the file exists, write truncates (clears) any existing information.

--> Warning: Write mode deletes existing content immediately. Check if a file exists before overwriting information by accident.

--> To open a file for writing information, use:

f = open("<file name>", "w")

--> The default mode is text, so the following line is equivalent to the default:

f = open("<file name>", "wt")

--> To write in binary mode, open the file with:

f = open("<file name>", "wb")

--> Add + to allow reading the file:

f = open("<file name>", "w+")  # Textual write and read

f = open("<file name>", "wt+") # Same as above

f = open("<file name>", "wb+") # Binary write and read

--> The open() function returns a file object whose details depend on the chosen modes.

--> Append Mode
        - Append mode adds information to an existing file, placing the pointer at the end. If a file does not exist, append mode creates the file.

--> Note: The key difference between write and append modes is that append does not clear a file's contents.

f = open("<file name>", "a")  # Text append

f = open("<file name>", "at") # Same as above

f = open("<file name>", "ab") # Binary append

--> Add the + sign to include the read functionality.

Note: Learn how to append a string in Python.

--> Create Mode
        - Create mode (also known as exclusive create) creates a file only if it doesn't exist, positioning the pointer at the start of the file.

--> Note: If the file exists, Python throws an error. Use this mode to avoid overwriting existing files.

f = open("<file name>", "x")  # Text create

f = open("<file name>", "xt") # Same as above

f = open("<file name>", "xb") # Binary create

--> Add the + sign to the mode include reading functionality to any of the above lines.

--> Reading Files in Python
        - After importing a file into an object, Python offers numerous methods to read the contents.

--> Use the read() method on the file object and print the result. For example:

f = open("file.txt")
print(f.read(),end="")

--> Note: The print() function automatically adds a new empty line. To change this behavior, add the end="" parameter to print() to remove the empty line.

--> python read from file : The code prints the text file's contents. Read Parts of the File
--> Provide a number to the read() function to read only the specified number of characters:

f = open("file.txt")
print(f.read(5))

--> python read characters : The output prints the first five characters in the file.

--> Alternatively, use the readline() method to print only the first line of the file:

f = open("file.txt")
print(f.readline())

--> python read line
--> Add an integer to the readline() function to print the specified number of characters without exceeding the first line.

--> Read Lines
--> To read lines and iterate through a file's contents, use a for loop:

f = open("file.txt")
for line in f:
    print(line, end="")

--> python read file for loop : Alternatively, use the readlines() method on the file object:

f = open("file.txt")
print(f.readlines())

--> python read lines : The function returns the list of lines from the file stream.

--> Add an integer to the readlines() function to control the number of lines. For example:

f = open("file.txt")
print(f.readlines(15))

--> python read lines characters : The integer represents the character number, and the function returns the line where the
character ends along with the previous lines.

--> Close Files
        - A file remains open until invoking the close() function. use to avoid unpredictable file behavior and corrupted files.

--> To close a file, run the close() method on the file object:

f.close()

--> An alternative way to ensure a file closes is to use the with statement. For example:

with open("<file name>"):
    file_contents = f.read()
    # Additional code here

--> The with statement automatically closes the file.

-->  Deleting Files in Python
Removing files in Python requires establishing communication with the operating system.
Import the os library and delete a file

import os
os.remove("file.txt")



Python File Methods
Python offers various other functions when working with file objects.


close()	Flushes and closes the file object.
detach()	Separates buffer from text stream and returns the buffer.
fileno()	Returns the file's descriptor if available.
flush()	Flushes the write buffer. Not available for read-only objects.
isatty()	Checks if a file stream is interactive.
read(<int>)	Read <int> number of characters at most.
readable()	Checks if an object is readable.
readline(<int>)	Reads from the object until a newline or end of the file.
readlines(<int>)	Returns a list of lines from the file object, where <int> is the approximate character number.
seek(<offset>, <position>)	Changes the pointer position to <offset> relative to the <position>.
seekable()	Checks if the file object supports random access.
tell()	Prints the current stream position.
truncate(<byte>)	Resizes the file stream to <bytes> (or current position if unstated) and returns the size.
write(<string>)	Writes <string> to the file object and returns the written number of characters.
writable()	Checks whether the file object allows writing.
writelines(<list>)	Writes a <list> of lines to the stream without a line separator."""