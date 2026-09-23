#single level
class Noodles:
    def use(self):
        print("fork")

class ChineseNoodles(Noodles):
    def use(Self):
        print("chopsticks")

cn=ChineseNoodles()
cn.use()           #child class hides the parent class

