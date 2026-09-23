print(__name__)  #executed directly so returns "__main__" (string)
print(type(__name__))
print(__name__=="__main__")


def add(a,b):
    """adding two numbers"""
    print(a+b)

add(10,20)                #this will be executed when another file  imports this module

if __name__ == "__main__":
    add(10,20)            #this will not be executed when another file imports this module
