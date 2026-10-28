#pickle - load,dump
import pickle
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name} {self.age}"

with open("file/student.pkl","w+b") as f:
    s=Student("akash",20)
    pickle.dump(s,f)
    
    f.seek(0)
    obj=pickle.load(f)
    print(obj)

    
    




    



    


    