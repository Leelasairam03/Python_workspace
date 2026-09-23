'''
oops:

 -objects : entities in a program
   -entity can have data/state
   -entity can have behaviour/functionality

   syntax:
   object_name=classname()     #instantiation

 -class :blueprint/prototype of an object
         data represented using variables
         behviours represented using methods

        syntax:
        class classname:
            variables
            methods

        -n number of objects can be created using 1 class, but still each object created is unique in terms of memory allocation


1)inheritance
2)encapsulation
3)abstraction
4)polymorphism

object oriented: representing everything in program in the form of objects that store data/states and perform operations/behaviour on that data

memory allocation wrt class and instances:

-> when class is defined,class dictionary gets created and inside it variable and methods of that class is stored in the form of key and values
-> when instance is created ,instance dictionary gets created and inside it instance data is stored in the form of key and values,it will have a reference to class

note: print(classname.__dict__) - displays the class dictionary
      print(objreference.__dict__) - displays the instance dictionary

'''
class currency:  #class definition
    ''' this class is about currency'''
    pass


c1=currency()   #instantiation
c2=currency()
c3=currency()

print(c1) #<__main__.currency object at some adress>
print(c2) #<__main__.currency object at some adress>
print(c3) #<__main__.currency object at some adress>

print(currency.__dict__)
print(c1.__dict__)