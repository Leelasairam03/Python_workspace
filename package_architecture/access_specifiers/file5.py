#encapsulation
class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    
    #setter methods
    def set_marks(self,marks):
        if marks<=100 and marks>=0:
            self.__marks=marks
        else:
            print("invalid marks")
    
    #getter methods
    def get_marks(self):
        return self.__marks

s=Student('lathika',80)
print(s.get_marks())
s.set_marks(90)
print(s.get_marks())
