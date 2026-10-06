from api.payment_api import PaymentAPI
from random import randint
class UPI(PaymentAPI):
    def authenticate(self):
        pin = randint(100,999)
        print(f"upi pin is {pin} verified successfully")
        print("upi authentication successful")

    def pay(self,amount):   
        transaction_id = randint(10000,99999)
        print(f"transaction id is {transaction_id}")
        print(f"{amount} Rs paid successfully using UPI")



