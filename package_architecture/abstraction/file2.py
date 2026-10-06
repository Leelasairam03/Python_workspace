from abc import ABC,abstractmethod
class Minister(ABC):
    @abstractmethod
    def create_awareness(self):
        pass

    def publish_report(self):
        print("Publishing the report")

class FinanceMinister(Minister):
    def create_awareness(self):
        print("creating awareness for the public")
    
fm=FinanceMinister()
fm.create_awareness()
fm.publish_report()
    
    

