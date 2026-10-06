from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def find_area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def find_area(self):
        return self.side*self.side

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def find_area(self):
        return self.l*self.b

sq=Square(10)
print(sq.find_area())

rec=Rectangle(5,10)
print(rec.find_area())
    

