#pickle - loads,dumps
import pickle
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name} {self.age}"

with open("file/student.pkl","w+b") as f:
    s=Student("akash",20)
    binary_data=pickle.dumps(s)
    f.write(binary_data)

    f.seek(0)
    data=f.read()
    obj=pickle.loads(data)
    print(obj)

    
    




    



    


    