#protected
class BankAccount:
    bank_name=" SBI"       #public class variable
    _interest_rate=5       #protected class variable

    def __init__(self,cname,accno):
        self.cname=cname              #public instance variable
        self._accno=accno             #protected instance variable

    def _calculate_interest(self,amount):         #protected instance method
        return (amount*self._interest_rate)/100


class SavingsAccount(BankAccount):
    def show_interest(self,amount):                  #public instance method
        print(self._calculate_interest(amount))
        

sa=SavingsAccount('sai ram',12345)
sa.show_interest(50000)

    

