class BankAccount:
    def __init__(self,cname):
        self.cname=cname
        self.__balance=1000
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("invalid amount")
    

    def withdraw(self,amount):
        if amount<self.__balance and amount>0:
            self.__balance-=amount
        else:
            print("no sufficient balance")
    
    def view_balance(self):
        return self.__balance


b=BankAccount("lathika")
b.withdraw(500)
print(b.view_balance())
b.deposit(1000)
print(b.view_balance())

print(b._BankAccount__balance)