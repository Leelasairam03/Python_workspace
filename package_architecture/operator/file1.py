# dunder arithmetic operators
class Money:
    def __init__(self,value):
        self.value=value
    
    def __add__(self,other):
        return Money(self.value+other.value)
    
    def __sub__(self,other):
        return Money(self.value-other.value)
    
    def __mul__(self,other):
        return Money(self.value*other.value)
    
    def __truediv__(self,other):
        return Money(self.value/other.value)
    
    def __floordiv__(self,other):
        return Money(self.value//other.value)
    
    def __mod__(self,other):
        return Money(self.value%other.value)
    
    def __pow__(self,other):
        return Money(self.value**other.value)

    def __str__(self):
        return f"Rs.{self.value}"

m1=Money(100)
m2=Money(200)
print(m1+m2)

m3=Money(300)
m4=Money(100)
print(m3-m4)

m5=Money(200)
m6=Money(400)
print(m5*m6)

m7=Money(100)
m8=Money(200)
print(m7/m8)  

m9=Money(100)
m10=Money(200)
print(m9//m10)

m11=Money(50)
m12=Money(40)
print(m11%m12)

m13=Money(2)
m14=Money(3)
print(m13**m14)



