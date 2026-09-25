#module dunder methods
'''
object class-
--> in python every class automatically inherits from a built in class called object
-->it is the ultimate base class - the root of python's hierarchy

importance-
    - the object class provides a set of useful predefined special methods(dunder methods) that give "default behaviour's to all objects" such as
    1) printing/string representation
    2) comparsion operations
    3) hashing
    4) identity and type checking etc

few dunder methods:
1)__new__(cls)
    -->called when an object is created
    -->responsible for creating the instance(memory allocation)
    -->returns the new object
    
2)__init__(self)
    -->called after the object is created
    -->responsible for initializing the object's state(assigning values to instance variables)

3)__str__(self)
    -->called when object is converted to string
    -->should return a user friendly string representation

4)__repr__(self)
    -->called when object is converted to string
    -->should return an unambiguous string representation(developer friendly)
    -->used for debugging

5)__hash__(self)
    -->returns the hash value of the object
    -->used for storing objects in hash based data structures like sets and dict keys

6)__eq__(self,other)
    -->called when two objects are compared using ==
    -->should return True if objects are equal,False otherwise

7)__ne__(self,other)
    -->called when two objects are compared using !=
    -->should return True if objects are not equal,False otherwise

8)__lt__(self,other)
    -->called when two objects are compared using <
    -->should return True if first object is less than second object,False otherwise

9)__le__(self,other)
    -->called when two objects are compared using <=
    -->should return True if first object is less than or equal to second object,False otherwise

10)__gt__(self,other)
    -->called when two objects are compared using >
    -->should return True if first object is greater than second object,False otherwise

11)__ge__(self,other)
    -->called when two objects are compared using >=
    -->should return True if first object is greater than or equal to second object,False otherwise

'''

