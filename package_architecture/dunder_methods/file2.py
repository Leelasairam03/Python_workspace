#__str__
class Pen:
    def __init__(self,color,cost,brand):                    
        self.color=color
        self.cost=cost
        self.brand=brand

    def __str__(self):
        return f"the pen is {self.color} and costs {self.cost} and brand {self.brand}"
    
p=Pen("blue",10,"reynolds")

print(p)  #__str__ method is called automatically-->  p.__str__()
print(str(p))
