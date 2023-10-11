# # EXCEPTION HANDLING : RUNTIME ERROR WHICH CAN BE HANDLED BY THE PROGRAMMER.. ALL EXCEPTION ARE REPRESENTED AS CLASSES IN PYTHON
#
#
# # Exception Handling : whenever we executing our programs we may cross with of the some errors and this errors are called exception handling
# """ 1.  Index Error :  when our code is trying to access an index that is invalid """
#
# list = [1, 2, 3, 4, 5]
# list[4]
# """ Traceback ( most recent call last):
# Index Error : list index out of range list[4] """
#
# list = [1, 2, 3, 4, 5]  # correct syntax
# print("correct syntax of Index Error : ", list[0])
#
# """2. Name Error : it will occur name value because we have to give proper variable name
# """
# # lsst
# """ Traceback (most recent call last):
#      lsst
# NameError: name 'lsst' is not defined. Did you mean: 'list'?"""
#
# """ 3. TYPE ERROR : whenever we write int inside the string form it will shows an error """
#
# """ 3 + '5' """
#
# # by using try and except block we can handle the python errors
#
# """4. VALUE ERROR : NOT DEFINED FOR NEGATIVE VALUES """
#
# # By using try & except :
#
# import math
#
# num = int(input("enter num: "))
# try:
#     result = math.factorial(num)
#     print(result)
# except:
#     print("cannot compute factorial of negative number")
#
# """ - Whenever we write (EG:-5) then it will shows an error because negative values are not calculate by factorial...
#     - After using try & except block it will show that line which we have print instead of showing an traceback error ....
#     - whenever user input the num it will saved in variable.....
#       then try block will try to execute it will find the result using math.factorial
#     - so if the input is valid it will execute and except block will be skipped
#     - and if input is not valid it will print cannot compute factorial of negative number
# """
# # by using raise
#
# try:
#     num = int(input("enter num : "))
#     if num <= 0:
#         raise ValueError("not positive num")
# except ValueError as error:
#     print(error)
#
# # result = math.factorial(num)
# # print(result)
#
#
# # By using try & finally : Finally clause will execute in any situation wether the exeception is occur or not
#
# import math
# num = int(input("enter num : "))
# try:
#     result = math.factorial(num)
#     print(result)
# finally:
#     print("goodbye")
#
# """ - as per the above statement if we write negative num it will taceback value error
# but using finally clause it will show traceback error and also it will prints goodbye statment
#
# - finally clause is use to free the extrenal resources
#
# """
#
# """
#     - The else block lets you execute code when there is no error.
#     - The finally block lets you execute code, regardless of the result of the try- and except blocks.
# """
#
# # Python error and exception handling :
#
# """
#         - Errors are the problems in a program due to which the program
#           will stop executing.
#         - On the other hand, exceptions are raised when some internal events occur
#           which changes the normal flow of the program.
#
#         => Two types :
#                 - Syntax errors
#                 - Logical errors(exceptions)
#
#             => Syntax error :
#                 - When the proper syntax of the language is not followed
#                  then a syntax error is thrown.
#
#                  if (10<20)
#                  SyntaxError: invalid syntax
#
#                 - It returns a syntax error message because after the is statement
#                   a colon : is missing, we can fix this by writing the correct syntax.
#
#             => Logical error :
#                 - When in the runtime an error that occurs after passing
#                   the syntax test is called exception or logical type.
#                     e.g.
#                         a = 100/0
#                         Traceback (most recent call last):
#                             a = 100/0
#                         ZeroDivisionError: division by zero
#
#                 - Note:Exception is the base class for all exceptions in python.
#
# # Exceptions :
#
# # """
# #         - Exceptions are raised when the program is syntactically correct, but
# #           the code resulted in an error.
# #         - This error does not stop the exception of the program, however, it
# #           changes the normal flow of the program.
# # """
#
# # Try and except statement-catching exception :
#
# """
#         - Statements that can raise exception are keep inside the try clause and
#           the statements which handle that exception are written inside except clause.
#                     try :
#                             print("second element = %d" %(a[1]))
#
#                             throws an error since there are only 3
#                             element in array.
#
#                             print("Fourth element = %d" %(a[3]))
#                      except :
#                             print("An error occurred")
#
#                      >> Second element = 2
#                         An error occurred
#
#         - the statement that can cause the error are placed inside the try statement(second print statement in our case).
#           The second print statement tries to access the fourth element of the
#           list which is not there and this throws an exception. This exception
#           is then caught by the except statement.    """
#
# # 1. SyntaxError : This error occurs when you have a syntax mistake in your code.
# # print("Hey I m an Artist"
#
# """
# - Explanation :  Python expects code to follow specific rules.
#       A SyntaxError means you didn't follow these rules.
#       Check for missing parentheses, colons, or quotation marks.
# """
# # 2. Indentation Error :
# def my_function():
# print("Indentation error")
#
# """
# - Python uses indentation to determine code blocks.
#   block have the same indentation.
#
# print("Indentation error")
#     ^
# IndentationError: expected an indented block after function"""
#
# # 3. Name Error : This error occurs when you try to use a variable or function that hasn't been defined.
#
# print(undefined_variable)
#
# """ Explanation : Python can't find the name you're trying to use.
#     Check for types or make sure you've defined the variable or function.
# """
#
# # 4. Type Error :  This error happens when you use an operation on a data type that it doesn't support.
#
# result = "5" + 3
#
# """ Explanation : Python expects data types to be compatible for certain operations.
#     In this case, you can't add a string and an integer directly."""
#
# # 5. IndexError: This error occurs when we try to access an index that doesn't exist in a list or other sequence.
# If we try to access an index of a sequence that is invalid my_list = [1, 2, 3] print(my_list[5]) my_list[2]
#
# """ Explanation : You're trying to access an index that is out of the range of the list.
#     Remember that Python lists are zero-indexed."""
#
# # 6. KeyError : If we try to access a key in a dictionary that is invalid or does not even exist, This error
# happens when you try to access a dictionary key that doesn't exist.
#
# my_dict = {"name": "Alice"}
# print(my_dict["age"])
#
# """ Explanation : The key you're trying to access doesn't exist in the dictionary.
#     It will shows an error because the age dict is not stored inside the variable ."""
#
# # 7. FileNotFoundError:  This error occurs when you try to open or manipulate a file that doesn't exist.
#
# with open("nonexistent.txt", "r") as file:
#     content = file.read()
#
# """ Explanation :  Make sure the file path is correct and the file exists in the specified location."""
#
# # 8. ValueError: happens when you pass an argument of the correct data type but with an inappropriate value to a function.
#
# age = int("twenty")
#
# """" Explanation : The int() function expects a valid integer string. Ensure your input is of the correct format."""
#
# # 9. ZeroDivisionError : If we try to perform division by 0
#
# result = 10 / 0

# """Explanation : Division by zero is undefined in mathematics , dividing by zero it will prevent this error."""

# # 10. AttributeError: when you try to access an attribute or method of an object that doesn't exist.
# #     If we try to call an attribute (function object), its type is unsupported.
# text = "Hello, world"
# text.split(",")

# """ Explanation : Check if the attribute or method you're trying to use is available for the object
#     you're working with."""

# # 11. IOError : If we give a wrong file name or incorrect location.
# # 12. EOFError : If a function in python reaches the end of the file without reading any data at all.
# # 13. OverflowError : If the result of an operation is too big to be presented

