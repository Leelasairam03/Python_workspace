'''
-when inner function wants to access variables of outer function,it is called enclosing variables
-a variable becomes enclosing/non local variable only if the nested function uses it.
-if we try to modify the variable of the outer function(enclosing)inside the inner function,we get unboundlocalerror,therefore we use nonlocal key word inside the nested function
syntax:
def outer():
    x=10
    def inner():
        nonlocal x
        print(x)
    inner()
outer()
'''
y=100
def outer():
    x=10
    print("outer function:",x,y)
    def inner():
        nonlocal x
        global y
        print("inner function:",x,y)
        x=x+10
        y=y+10
        print("inner function:",x,y)
    inner()
outer()

def counter():
    count=0
    def increment():
        nonlocal count
        count=count+1
        print(count)
    def decrement():
        nonlocal count
        count=count-1
        print(count)
    increment()
    decrement()
counter()



