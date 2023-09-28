# represent the type of data into a variable or memory
# built-in data type : none type, numeric type, sequence, sets, mappings
# user-define : array, class, module

""" NUMERIC DATA TYPE """

# float :  val = 5.1e5 -- e means exponentiation which represent the power of 10 (5.1*10 raise 5)
# complex : a + bj or a + bJ (a and b may contain int or float number )
# a = real num , b = imaginary num , j or J = square root of -1
# bool : True/False true contains  1 and false contain 0

""" SEQUENCE DATA TYPE """

# **** STRING ****
str = " hey i m an artist! "
print(str)

# **** LIST ****
list = [234,'abc',True]   #----> grp of elemnts can also modify elemnts
print(list[0])
list[1] = 5123
print(list)

# **** TUPLE **** 

tuple = ('1,2,3','hello')
tuple[0]
print(tuple)
# tuple[1] = 20 #--> its gives error becuse  value cant be change 
print(tuple)

# **** RANGE TYPE ****

# RG = range(5) #--> rangw cant change value
rg = range (10,20,2) # 2 means it will give gap between 10 to 20
print(rg[2])
# print(RG)     (op : 10,12,14,16,18,20)

# **** SET ****
set = {10,20,30,'hello',40}
print(set) # -> unchangable

# **** MAPPING TYPE **** 

var = {'hetvi':100,'kashvi':200,'honey':300}
print('hetvi' in var)# --> check if key is present in dictonary
del var['hetvi']    ## delete key from dictionary
print(var)