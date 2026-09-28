#__str__
class Employee:
    def __init__(self,ename,esalary,edept):
        self.ename=ename
        self.esalary=esalary
        self.edept=edept

    def __str__(self):
        return f"employee name {self.ename} and salary {self.esalary} and dept {self.edept}"
        
e=Employee("sai ram",75000,"IT")
print(e)
