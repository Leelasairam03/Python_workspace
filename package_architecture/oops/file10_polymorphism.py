#polymorphism module
'''
polymorphism - 'poly' means many and 'morph' means forms. so polymorphism means many forms.
-it is the ability of the single interface(method/operator) to perform different action depending on the object it is applied to.
1)operator overloading
    ->using operators in different ways
    ->+ is used for adding two numbers or concatenating two strings
    ->* is used for multiplying two numbers or repeating a string

2)method overriding
    ->it is a feature of inheritance were child class provides its own implementation of a method that is already defined in its parent class using the same mehtod name and signature
    ->run time polymorphism
    steps:
    1)define a method in parent class
    2)override the same method in child class(implementation in child is different)

    note:overloading not possible in python, we can simulate using default arguments or *args

example:
        class parent:
            def show(self):
                print("parent show")

        class child(parent):
            def show(self):
                print("child show")


3)Duck Typing
    ->if it walks like a duck and quacks like a duck
    ->if the object has the method that is called,it will be executed



super()
->it is used to access the parent class method or constructor from the child class.
->proper way to access parent functionality when we are overriding methods

why do we need super?
->retain and reuse: it helps to retain and reuse the functionality of parent class and also provide custom implementation in child class
->avoid code repitition: instead of rewriting parent class logic in the child class, we can use super() to call the parent class method and add your own customizations
->maintain consistency: when overriding methods,super() ensures that the parent's initialization and behaviour is not lost.

2 situations when super is used:
1)method overriding
2)constructor chaining

class Parent:
    def methodname(self):
        print("methodname of parent class")

class Child(Parent):
    def methodname(self):
        super().methodname()
        print("methodname of child class")


constructor chaining-
it is the process wherein parent class constructor is invoked/called from child class constructor using super()
note:
1)super().__init__() is used to "reuse/restore the common initialisation logic of the parent constructor/initializer from the child constructor ,which reduces repetition
of code and this is called constructor chaining
2)defining a constructor in child class will stop the parent class constructor from being automatically called.parent init won't execute
3)super() follows the MRO , super doesn't directly mean calling a parent
'''
