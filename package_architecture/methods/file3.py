class Ornaments:
    def __init__(self,metal,price,grams):
        self.metal=metal
        self.price=price
        self.grams=grams
    
    def display(self):
        print(self.metal)
        print(self.price)
        print(self.grams)

    def change_price(self,new_price):
        self.price=new_price
    


o1=Ornaments("gold",100000,10)
o2=Ornaments("silver",20000,5)
o3=Ornaments("copper",1000,10)

o1.display()
print("----------------")
o1.change_price(110000)
o1.display()




