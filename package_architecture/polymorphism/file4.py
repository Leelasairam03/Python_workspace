from typing_extensions import override
class Person:
    def register(self,name):
        print(f"{name} registering as person")

class Employee(Person):
    @override
    def register(self,name):
        super().register(name)
        print(f"{name} registering as an Employee")

class Student(Person):
    @override
    def register(self,name):
        super().register(name)
        print(f"{name} registering as Student")

e=Employee()
e.register("sai ram")
print("---------------------------")
s=Student()
s.register("lathik")