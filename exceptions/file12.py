# create a custom exception class
class InvalidAmountException(Exception):
    pass

class InsufficientBalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,cname):
        self.owner=cname
        self.balance=5000
        
    def deposit(self,amount):
        if amount<0:
            raise InvalidAmountException("amount is negative")
        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        if amount<0:
            raise InvalidAmountException("amount is negative")
        elif amount>self.balance:
            raise InsufficientBalanceException("Insufficient balance")
        self.balance-=amount
        return self.balance

b=BankAccount("Sai ram")

try:
    b.deposit(-1000)
    print("balance",b.balance)
except InvalidAmountException as e:
    print(e)

try:
    b.withdraw(10000)
    print("balance",b.balance)
except (InvalidAmountException,InsufficientBalanceException)  as e:
    print(e)
    