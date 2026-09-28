#__hash__
class Product:
    def __init__(self,pid,name,price):
        self.pid=pid
        self.name=name
        self.price=price
    
    def __hash__(self):
        return hash(self.pid)

p1=Product(101,"mobile",10000)
print(hash(p1))