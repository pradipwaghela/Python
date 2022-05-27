"""
Class 
class class_name(arg):
    statment 1
             2
             .
             .
             .
             n
self :- Object of clas
myobject.method(arg1, arg2),
this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – 
this is all the special self is about.
__init__(self):
    pass
Construcutor in python
"""



class Person():
    def __init__(self,nam,nm):
        self.nam=nam
        self.num=nm
    def greet(self):
        print(f"Welcome {nam} We know {num} is your number")

    def greet1(self):
        print(f"Welcome {nam} We know {num} is your number")



nam=input("Enter Your name:- ")
num=input("Enter Your number:- ")
P1=Person(nam,num)
P1.greet()
P1.greet1()
 #Person.greet(P1)