#inheritance module
'''
inheritance- aquisition of properties of one class by another class, it can be refered to as "is-a" relationship
"parent class"  -class whose properties are aquired (also called super class or base class)
"child class"   -class that aquires properties of parent class (also called sub class or derived class)

types:
1.single level
    syntax: 
      class parent:
          ...

      class child(parent):
          ...
    
    note: MRO: Method resolution order
               ->method python uses to find methods in classes.

               classname.__mro__ --> returns tuple of classes in the order of method resolution
                                     returns attribute error if the method is not found

2.multi level
    syntax: 
      class parent:
          ...

      class child(parent):       #act as both parent of grandchild and child of parent
          ...

      class grandchild(child):
          ...

3.hierarchical - one parent and more than one child
    syntax: 
      class parent:
          ...

      class child1(parent):   
          ...

      class child2(parent):
          ...

4.multiple - 1 child class inherited from multiple parents
   syntax: 
      class parent1:
          ...

      class parent2:
          ...

      class child(parent1,parent2):
          ...

5.hybrid - combination of 2 or more different inheritance types
   example: 
      class A:
          ...

      class B(A):
          ...

      class C(A):
          ...

      class D(B,C):
          ...

Advantages:
    -> code reusability-reuses code of parent in child classes
    -> logical class hierarchy-code will be in structured and heirarchical manner
    -> extensibility-child class can override the methods of parent class to give new functionality
'''
