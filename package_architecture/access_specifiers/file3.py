#private
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    
    def get_marks(self):
        return self.__marks
    
s1=Student('sai ram',95)
print(s1.get_marks())

print(s1._Student__marks)
