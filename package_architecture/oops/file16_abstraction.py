'''
abstraction:
-defining requirements/ specifications in parent class
-implementing those requirements in child class is compulsory
-child class inherits the requirements from parent class

abstract class(incomplete class)
->it is a class that is meant only for inheritance, because it cannot be instantiated
->abstract class is idea/concept and is incomplete by design
->should have atleast 1 abstract method
->apllies rules upon child class

->decorated using @abstractmethod
->is an incomplete method,having method name and parameter,but no implementation
->it meant to be overriden/implemented in child class

syntax:

class parent_class(ABC):

    @abstractmethod
    def method(self,arguments):
        pass

class child_class(parent_class):
    def method(self,arguments):
        pass

-abstract base classes,is a module in python used to support abstraction
-base class is ABC, our class should inherit ABC class to become a abstract class
-@abstractmethod decorator is used to define a abstract method

'''