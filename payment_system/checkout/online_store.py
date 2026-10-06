from payment_method.upi import UPI
from payment_method.credit_card import CreditCard
class OnlineStore:
    def __init__(self,payment_method):
        self.payment_method = payment_method

    def process(self,amount):
        print("processing Transaction")
        self.payment_method.authenticate()
        self.payment_method.pay(amount)
        print("transaction processing complete")

os=OnlineStore(UPI())
os.process(100)
print("------------------------------------")
os=OnlineStore(CreditCard())
os.process(200)
