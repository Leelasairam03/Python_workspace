class Employee:
    def __init__(self):
        self.__salary=0
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,new_salary):
        if new_salary>6000:
            self.__salary=new_salary
        else:
            print("invalid salary")

e=Employee()
e.salary=50000
print(e.salary)
