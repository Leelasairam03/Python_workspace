class Pen:
    def __init__(self):                    
        print("Pen created successfully")

p=Pen()    #1.creates object and return using Pen.__new__() method. 
           # 2.calls Pen.__init__(p) method.                                 #constructors gets executed and initialize instance variables
print("-------manual object creation--------")
#internal object creation and initialisation looks like
d=Pen.__new__(Pen)
Pen.__init__(d)


