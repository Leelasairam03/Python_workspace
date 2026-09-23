'''
Constructor/initialiser-it is a block of code/special dunder method used to declare and initialize instance variables of an instance
SYNTAX: def __init__(self):

-it is written within the class and its name should be __init__(self)
-self refers to the current instance which is being created
-constructor is automatically invoked when an object of the class is created
-constructor can have n number of paramenters, n-1 arguments are passed

types of constructors:
    1.default constructor - constructor without any parameters
                -it is not visible to the user
                -present in super class object
                -when user doesn't provide custom constructor,default constructor will be used.

    2.custom constructor/user defined   
        -parameterised constructor - constructor with parameters
             -defined by the programmer,used when external values are passed to the constructor
             -n parameters, n-1 arguments are passed
        
        -non-parameterised constructor - constructor without parameters
             -defined by the programmer,used when no external values are passed to the constructor
             -n parameters, n arguments are passed

'''



class Employee:
    def __init__(self,name,eid,salary):      #execute once everytime a new instance is created
        self.name=name
        self.eid=eid
        self.salary=salary

e1=Employee('sairam',1,50000)
e2=Employee('balram',2,40000)
e3=Employee('palaksh',3,30000)

class Pen:
    def __init__(self,a,b,c):
        self.cost=a
        self.height=b
        self.quantity=c

p1=Pen(10,5,6)
p2=Pen(20,4,8)
p3=Pen(30,6,10)

class State:
    country='India'
    currency='INR'
    prime_minister='narendra modi'


    def __init__(self,name,capital,language):
        self.name=name
        self.capital=capital
        self.language=language

s1=State('karnataka','Bengaluru','kannada')








        