#method overriding - runtime polymorphism
from typing_extensions import override
class Chef:
    def cook(self):
        print("Chef is cooking")

class ItanlianChef(Chef):
    @override                     #not mandatory to write @override,    #pip install typing_extensions 
    def cook(self):
        print("ItanlianChef is cooking")

ic=ItanlianChef()
ic.cook()
