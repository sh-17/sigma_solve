# SET

"""
    - unordered collection
    - store multiple item in single variable
    - unchangeable
    - doesn't allow duplicate items
    - doesn't repeat same entries
"""
# empty set

set = set()
print(type(set))

# Access Set

n = {"hey",45,8}
for i in n:
    print(i,end="")

""" o/p : 8,45,hey """

# union ()

s1 = {1,2,5,6}
s2 = {5,8,9}
print(s1.union(s2))
s1.update(s2) # it will update the two unquie num which are specified inside the l2
print(s1,s2)

# instersection update : it will update the value which is mentioned in both variables

myskills = {'resin','canvas','mandala','painting','singing'}
myskills2 = {'singing','artist','crafty','developer','dot mandala'}
myskills.intersection_update(myskills2)
print("intersection_update",myskills)

# isdisjoint() : checks if item is is given in set are present in another set or not

# if items are not present then it will returns se False, and  if items are present then return True .

myskills = {'resin','canvas','mandala','painting','singing'}
myskills2 = {'singing','artist','crafty','developer','dot mandala'}
print("isdisjoint",myskills.isdisjoint(myskills2))

# issuperset(): it will show similar item in particular list removes extra item

myskills = {'resin','canvas','mandala','painting','singing'}
myskills2 = {'singing','artist','crafty','developer','dot mandala'}
print("issuperset: ",myskills.issuperset(myskills2))
myskills3 = {'canvas','mandala','potrait'}
print("issuperset : ",myskills.issuperset(myskills3))

# issubset():return value true if values are same inside the original and r set
myskills = {'resin','canvas','mandala','painting','singing'}
myskills2 = {'singing','artist','crafty','developer','dot mandala'}
print("issubset: ",myskills.issubset(myskills2))
myskills3 = {'canvas','mandala','potrait'}
print("issubset : ",myskills.issubset(myskills3))

# symmetric_difference(): it will not present those two item which are similar in myskills
myskills = {'resin','canvas','mandala','painting','singing'}
myskills2 = {'singing','artist','crafty','developer','mandala'}
myskills3 = myskills.symmetric_difference(myskills2)
print("symmetric_difference :",myskills3)

# symmetric_difference_update():  method update into existing set from another set
myskills = {'resin','canvas','mandala','painting','singing'}
myskills2 = {'singing','artist','crafty','developer','mandala'}
myskills.symmetric_difference_update(myskills2)
print("symmetric_difference_update: ",myskills3)

# difference : return new set
# only prints that items which are present in original set not in both sets
# shows output for only first original set

myskills = {'resin','canvas','mandala','painting','singing'}
myskills2 = {'singing','artist','crafty','developer','mandala'}
myskills3 = myskills.difference(myskills2)
print("difference:",myskills3)

# differnce_update () : updates into existing set from another set

myskills = {'resin','canvas','mandala','painting','singing'}
myskills2 = {'singing','artist','crafty','developer','mandala'}
myskills.difference_update(myskills2)
print("difference_update: ",myskills)

#add : add single item to set
myskills = {'resin','canvas','mandala','painting','singing'}
myskills.add('potrait')
print("adding single item: ",myskills)

#update : more than one item
myskills = {'resin','canvas','mandala','painting','singing'}
myintro = {'hey i m an artist'}
myskills.update(myintro)
print("updated item: ",myskills)

# remove() : if we try to del item which is not present ot will raise an error whereas discard will not raise an error

# myskills = {'resin','canvas','mandala','painting','singing'}
# myskills.remove('potrait')
# print("remove item: ",myskills)


myskills = {'resin','canvas','mandala','painting','singing'}
myskills.discard('potrait')
print("discard item: ",myskills)

# pop () : random remove any element from set and it will also show the item which is remove from set

myskills = {'resin','canvas','mandala','painting','singing'}
item = myskills.pop()
print(myskills)
print(item)

# del() : del is not method its a keyword which del the set entirely , it will not the deleted set

myskills = {'resin','canvas','mandala','painting','singing'}
myskills2 = {'singing','artist','crafty','developer','mandala'}
del myskills
print("del: ",myskills2)

# clear(): if we don't want to del the entire set, we just want to delete all items whithin that set

myskills = {'resin','canvas','mandala','painting','singing'}
myskills.clear()
print("clear - it will show as empty set:",myskills)