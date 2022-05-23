"""
Class 
class class_name(arg):
    statment 1
             2
             .
             .
             .
             n
myobject.method(arg1, arg2),
this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – 
this is all the special self is about.
"""

class Person():
    nam=input("Enter your name:- ")
    nm=int(input("Enter your number:- "))

    def greet(self):
        print(f"Welcome {self.nam} We know {self.nm} is your number")


P1=Person()
P1.greet()  #Person.greet(P1)