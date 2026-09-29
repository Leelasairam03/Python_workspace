#duck typing
class Zomato:
    def deliver(self):
        print("zomato is delivering the order")

class Swiggy:
    def deliver(self):
        print("swiggy is delivering the order")

class Swish:
    def deliver(self):
        print("swish is delivering the order")

class Rapido:
    def commute(self):
        print("bike ride started")  

x=Zomato()
y=Swiggy()
z=Swish()
r=Rapido()  # r.deliver will give attribute not found error

def process_delivery(partner):
    partner.deliver()
    
l=[x,y,z,r]
for i in l:
    if hasattr(i,'deliver'):                  #checking if the class has attribute or not
        process_delivery(i)
    else:
        print("object does not have deliver method")
