from api.payment_api import PaymentAPI
from random import randint
class CreditCard(PaymentAPI):
    def authenticate(self):
        otp = randint(100,999)
        print(f"credit card otp is {otp} verified successfully")
        print("credit card authentication successful")

    def pay(self,amount):
        transaction_id = randint(10000,99999)
        print(f"transaction id is {transaction_id}")
        print(f"{amount} Rs paid successfully using credit card")



    


