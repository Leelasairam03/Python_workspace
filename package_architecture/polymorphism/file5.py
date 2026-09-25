class ParentClass:
    def __init__(self,a,b):
        print("parent implementation")

class ChildClass(ParentClass):
    def __init__(self,a,b):
        super().__init__(a,b)             #constructor chaining(like overriding)
        print("child implementation")
 

