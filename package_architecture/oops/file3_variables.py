#dunder variable module
'''
variables in object oriented: 

1)class variables
2)instance variables

class variables: declared inside class but outside of all methods
                 shared among all instances of the class
                 if any value is common for all instances it should be made as class variable
                 stored in class dictionary
                 syntax: 
                        variable_name= value
                              or
                        ClassName.variable_name = value   #outside the class it can be defined like this.

                 acccessing class variables:
                        ClassName.variable_name   #outside the class
    
                 modifying class variables:
                        ClassName.variable_name = newvalue  #modifies class variable for all instances
                        

instance variables: declared using instance references(object references)
                    unique to each instance of the class
                    stored inside instance dictionary
                    syntax: objref.variable_name= value  (inside any method)
              
                    acccessing instance variables:
                        objectreference.variable_name   #inside the class
                     
                    modifying instance variables:
                        objectreference.variable_name= newvalue


'''
class Student:
       course='python full stack'
       institute='DCL'

       def __init__(self,name,age,email):
           self.name=name
           self.age=age
           self.email=email

Student.roomnumber=101
print(Student.__dict__)

print(Student.roomnumber)
print(Student.institute)
print(Student.course)

Student.institute="Dhee Coding Lab"

print(Student.__dict__)

s1=Student('sai ram',21,'example@gmail.com')
print(s1.__dict__)

print(s1.course)
print(s1.age)
print(s1.email)

s1.email='sairampanchak@gmail.com'

print(s1.email)
