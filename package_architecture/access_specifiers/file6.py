class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    
    #setter methods
    def set_salary(self,salary):
        if salary<=100000 and salary>=0:
            self.__salary=salary
        else:
            print("invalid salary")
    
    #getter methods
    def get_salary(self):
        return self.__salary

e=Employee('lathika',80000)
print(e.get_salary())
e.set_salary(90000)
print(e.get_salary())
    