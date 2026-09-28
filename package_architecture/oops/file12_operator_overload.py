#operator overloading
'''
-->in python we can perform operations on objects using operators like +,-,*,/,%,**etc
-->when an operator is used on objects,python automatically calls the corresponding dunder method
-->we can override these dunder methods to implement custom behavior for operations on objects

some dunder methods for operators

#1)arithemetic dunder methods
    
    #1)__add__(self,other)
    -->called when + operator is used on objects
    -->must return the result of the operation
    -->syntax:result=obj1+obj2
    --> a+b ----> a.__add__(b)
    
    #2)__sub__(self,other)
    -->called when - operator is used on objects
    -->must return the result of the operation
    -->syntax:result=obj1-obj2
    --> a-b ----> a.__sub__(b)
    
    #3)__mul__(self,other)
    -->called when * operator is used on objects
    -->must return the result of the operation
    -->syntax:result=obj1*obj2
    --> a*b ----> a.__mul__(b)
    
    #4)__truediv__(self,other)
    -->called when / operator is used on objects
    -->must return the result of the operation
    -->syntax:result=obj1/obj2
    --> a/b ----> a.__truediv__(b)
    
    #5)__floordiv__(self,other)
    -->called when // operator is used on objects
    -->must return the result of the operation
    -->syntax:result=obj1//obj2
    --> a//b ----> a.__floordiv__(b)
    
    #6)__mod__(self,other)
    -->called when % operator is used on objects
    -->must return the result of the operation
    -->syntax:result=obj1%obj2
    --> a%b ----> a.__mod__(b)
    
    #7)__pow__(self,other)
    -->called when ** operator is used on objects
    -->must return the result of the operation
    -->syntax:result=obj1**obj2
    --> a**b ----> a.__pow__(b)

'''