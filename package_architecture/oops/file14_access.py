#access specifiers/modifiers
'''
Access specifier is used to define the scope of a variable or method.
it applies only inside classes because classes are about encapsulation
python does not have strict access specifiers like java/c++ but it follows a convention

3 types:
Public      :accessible from anywhere
Private     :accessible only within the class
Protected   :accessible within the class and subclasses


1)public
any var or method declared normally inside a class is public by default
No special prefix is used

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student('sai ram',21)
print(s1.name)
print(s1.age)

2)protected
we use a single underscore prefix to denote a protected variable or method

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def _protected_method(self):
        print("protected method")

3)private
use double underscore prefix to denote a private variable or method


'''
