#access specifier module
'''
encapsulation: 
        the process of protecting data by making the variable private and controlling thier access through setter and getter methods
        or 
        binding together the data and the methods that operate on the data
        and keeping them safe from outside interference and misuse

steps to achieve encapsulation
1)class should be public and non abstract
2)should have a private variable
3)should have a setter (to modify) - takes usually 1 parameter,validation logic inside it,not supposed to return any value
4)getter method(to fetch) - has no parameters,supposed to return the value,access private data

syntax:
class class_name:
    def __init__(self,var):
        self.__private_var=var
    
    #setter methods
    def set_var(self,new_val):
        #validation logic
        self.__private_var=new_val
    
    #getter methods
    def get_var(self):
        return self.__private_var

obj=Test(10)
obj.set_var(20)
print(obj.get_var())

encapsulation using @property decorator

2 decorators:
1)@property - is a decorator,allows method to behave like "getter"
            - instead of calling it normally like a method we can access it like a normal attribute
            ex: print(instanceref.variable)

2)@<property>.setter - allows you to assign a value like a variable,but indirectly it calls a method
                    ex: instanceref.variable=newValue

ex:
class ClassName:
    def __init__(self):
        self.__var=initialValue

    @property                  #getter should be written first
    def var(self):
        return self.__var

    @var.setter                #then comes setter
    def var(self,new_val):
        self.__var=new_val

obj=ClassName()
obj.var=100
print(obj.var)


advantages using property decorator:
1)it gives attribute access with mehtod control
2)looks like attribute but works like method"
3)when requirements change,the code does not break

'''
