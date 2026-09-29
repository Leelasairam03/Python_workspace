#__eq__
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def __eq__(self,other):
        if isinstance(other,Car):
            return self.model==other.model
        return False


c1=Car("bmw","m4",2020)
c2=Car("bmw","m4",2020)
print(c1==c2)            #compares address of object by default, we override __eq__ to compare object by values

'''
isinstance(objref,classname) -> returns true if objref is an instance of classname,False otherwise
    -->it implicitly uses __eq__() method for comparison
    -->it uses both value based and memory based comparsion
    -->it internally uses == operator to compare objects.
    -->if __eq__() method is overridden,it uses the overridden method for comparison
    -->if __eq__() method is not overridden,it uses the default method for comparison
'''
print(isinstance(c1,Car))
print(isinstance(c1,int))


