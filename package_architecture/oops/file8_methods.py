#methods module
'''
methods:-in python it is a block of code which is written within the class
            and it is used to perform specific operations


types of methods:
    1.instance methods   -methods that operate on instance variables

    -it is used to perform operations on instance variables
    -it recieves the instance reference as the 1st parameter(self)
    -when operation is related to a particular instance we use instance methods

    syntax: def method_name(self,para1,para2,...):   #n para
            #implementation/instance method body

    calling: obj.method_name(arg1,arg2,...)

    2.class methods      -methods that operate on class variables
         
        -belongs to the class itself,not to the instance
        -works on class level data
        -it recieves the class reference as the 1st parameter(cls)
        -declared using @classmethod decorator just above the method
        -when operation is related to a class and not particular instance we use class methods

        syntax: @classmethod
                def method_name(cls,para1,para2,...):   #n para
                    #implementation/class method body
        
        calling: class_name.method_name(arg1,arg2,...)  #n-1 arguments

    3.static methods     -methods that operate on both instance and class variables
       
        -when we want to define a method inside a class,but it neither operates on instance variables nor on class variables then we use static methods

        -does not take cls or self as parameter
        -declared using @staticmethod decorator just above the method
        -can be called using either class name or instance name

        syntax: @staticmethod
                def method_name(para1,para2,...):   #n para
                    #implementation/static method body
        
        calling: class_name.method_name(arg1,arg2,...)  #n arguments
                 obj.method_name(arg1,arg2,...)  #n arguments

'''
'''
advantages of methods
1)enforce a logic before chaging data
2)avoids code suplication
3)adheres to oop principles
4)provides a structured way to interact with objects
'''



