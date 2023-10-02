# scope : which means concate two fun 
def fun1(n):
    print(n,"hello")
fun1("world")

# l var & g var

# jyre local var ni ander value nai hoi tyre gbl sathe + thse 
l = 10 # global scope
def func(n):
    l = 5 #local
    a = 23 #local
    print(l, a)
func("hii")
print(l)

# global keyword --> allow kre user ne modify karva mate outside var... je current scope ma hoi ene  
# when we want to read nd write any global var value insdie the function
l = 10 # global scope
def func(n):
    #l = 5 #local
    a = 23 #local
    global l 
    l = l + 20
    print(l, a)
    print(n,"hii")
func("this is me")

# nested :
def hey():
    a = 5
    def hello():
        global a
        a = 6
    print("before hello()",a)
    hello()
    print("after "
          "hello()",a)
hey()
