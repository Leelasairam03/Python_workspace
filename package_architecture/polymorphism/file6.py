class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

class Citizen(Person):
    def __init__(self,name,age,height,citizen_id,nation,currency):
        super().__init__(name,age,height)
        self.citizen_id=citizen_id
        self.nation=nation
        self.currency=currency

class Refugee(Person):
    def __init__(self,name,age,height,refugee_id,origin,exit_date):
        super().__init__(name,age,height)
        self.refugee_id=refugee_id
        self.origin=origin
        self.exit_date=exit_date


c=Citizen("sai ram",22,5.10,1234567890,"india", "inr")
print(c.__dict__)

r=Refugee("lathik",22,5.8,999999999,"pakistan","25-09-2026")
print(r.__dict__)