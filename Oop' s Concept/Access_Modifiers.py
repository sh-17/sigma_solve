"""
Public :
Private :
Protected :

"""

class Employee:
    no_f_leaves = 10
    var = 10

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def printdetails(self):
        return f"The Name is (self.name). Salary is(self.salary)"

    @classmethod
    def change_no_of_leaves(cls,newleaves):
        cls.no_f_leaves = newleaves
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("this is good"+string)
emp = Employee("")