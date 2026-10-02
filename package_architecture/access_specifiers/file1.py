#public
class Park:
    authority="gba"                 #public class variables

    def __init__(self,name,location):
        self.name=name                #public instance variables
        self.location=location
    
    def open_park(self):             #public instance method
        print("park opens on weekdays",self.name)
    
    @classmethod                     #public class method
    def change_authority(cls,new_authority):
        cls.authority=new_authority

P1=Park('cubbon park','bengaluru')
p1.open_park()
