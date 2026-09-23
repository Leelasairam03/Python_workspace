class BankCustomer:
    @staticmethod
    def cal_interest(P,T,R):
        return P*T*R/100

print(BankCustomer.cal_interest(10000,10,5.5))

b1=BankCustomer()
print(b1.cal_interest(10000,10,5.5))