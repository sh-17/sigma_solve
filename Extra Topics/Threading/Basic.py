# threads are python objects of threading thread() class
import threading

# current thread
print(threading.current_thread().name)  # output : <_MainThread(MainThread, started 19744)>
print(threading.current_thread().is_alive())  # it will return boolean value if thread is started or not
print(threading.current_thread().ident)  # to check identity
# name is attribute of this class and object is current_thread()

""" TWO WAYS OF CREATING THREADS : 1. USING THREAD CLASS PRESENT IN THREADING MODULE ,
                                        
                                   2. BY EXTENDING THREAD CLASS - USING INHERIT BY CREATING CLASS CLASS 

"""
# IMPORT THREAD CLASS FROM THREADING MODULE
from threading import Thread, current_thread


# CREATE FUNCTION CONTAINING CODE TO BE EXECUTED PARALLEL
def display():
    print("t1 thread details: ",current_thread())
    # def display(n,msg):
    for i in range(4):
        # for i in range(n)
        print("Hey! How are you?")


# CREATE AN OBJECT OF THREAD CLASS
# t1 = Thread(target=display,args=(2,"hello")) # using tuple we can pass single argument using ( , ) args=(5,)
t1 = Thread(target=display)
# START CREATED THREAD USING START() METHOD.
t1.start()
#  there is no direct wait to return any msg
""" When we create new thread it goes the req to the operator system inside that it will allocate memory -- using 
python interpreter """