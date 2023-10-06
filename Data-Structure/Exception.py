# EXCEPTION HANDLING : RUNTIME ERROR WHICH CAN BE HANDLED BY THE PROGRAMMER.. ALL EXCEPTION ARE REPRESENTED AS CLASSES IN PYTHON

"""
    - The try block lets you test a block of code for errors.
    - The except block lets you handle the error.
    - The else block lets you execute code when there is no error.
    - The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

# Python error and exception handling :

"""
        - Errors are the problems in a program due to which the program
          will stop executing.
        - On the other hand, exceptions are raised when some internal events occur
          which changes the normal flow of the program.

        => Two types :
                - Syntax errors
                - Logical errors(exceptions)

            => Syntax error :
                - When the proper syntax of the language is not followed
                 then a syntax error is thrown.

                 if (10<20)
                 SyntaxError: invalid syntax

                - It returns a syntax error message because after the is statement
                  a colon : is missing, we can fix this by writing the correct syntax.

            => Logical error :
                - When in the runtime an error that occurs after passing
                  the syntax test is called exception or logical type.
                    e.g.
                        a = 100/0
                        Traceback (most recent call last):
                            a = 100/0
                        ZeroDivisionError: division by zero
                
                - Note:Exception is the base class for all exceptions in python.
                
# Exceptions :

# """
#         - Exceptions are raised when the program is syntactically correct, but
#           the code resulted in an error.
#         - This error does not stop the exception of the program, however, it
#           changes the normal flow of the program.
# """

# Try and except statement-catching exception :

"""
        - Statements that can raise exception are keep inside the try clause and 
          the statements which handle that exception are written inside except clause.   
                    try :
                            print("second element = %d" %(a[1]))

                            throws an error since there are only 3
                            element in array.

                            print("Fourth element = %d" %(a[3]))
                     except :
                            print("An error occurred")

                     >> Second element = 2
                        An error occurred

        - In the above example, the statement that can cause the error are
          placed inside the try statement(second print statement in our case).
          The second print statement tries to access the fourth element of the 
          list which is not there and this throws an exception. This exception
          is then caught by the except statement.    """


"""ZeroDivisionError : If we try to perform division by 0
2. OverflowError : If the result of an operation is too big to be presented
3. IndexError : If we try to access an index of a sequence that is invalid
4. AttributeError : If we try to call an attribute (function object), its type is unsupported.
5. EOFError : If a function in python reaches the end of the file without reading any data at all.
6. KeyError : If we try to access a key in a dictionary that is invalid or does not even exist
7. IOError : If we give a wrong file name or incorrect location.
"""


