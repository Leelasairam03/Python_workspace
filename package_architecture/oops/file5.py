class Student:
       course='python full stack'
       institute='DCL'

       def __init__(self,name,age,email):
           self.name=name
           self.age=age
           self.email=email

s1=Student('sai ram',21,'example@gmail.com')

print(s1.name)
print(s1.age)
print(s1.email)

s1.email='sairampanchak@gmail.com'

print(s1.email)

print("-----------------------------------")
s2=Student('kishore',22,'kishore@gmail.com')

print(s2.name)
print(s2.age)
print(s2.email)

