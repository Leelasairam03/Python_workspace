#single level
class Employee:
    def work(self):
        print("employee works")

class Developer(Employee):
    def code(self):
        print("developer codes")

d1=Developer()
d1.code()
d1.work()
print(Developer.__mro__)
