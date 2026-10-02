class Politician:
    def __init__(self,name,wealth):
        self.name=name
        self.__wealth=wealth
    
    def __raise_funds(self):
        print("raising funds")
    
    def ed_raids(self):
        print(self.__wealth)
        self.__raise_funds()

p=Politician('rahul',1000000)
p.ed_raids()

        
        



