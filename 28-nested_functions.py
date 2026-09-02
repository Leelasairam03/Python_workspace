'''
- when a function is defined inside a function,it is called as nested function
- the inner function can access the variables of the outer function, and the function itself can be accessed only inside the outer function
- it is a helper function but private inside the main function
syntax:
def outer():
    def inner():
        print("inner")
    inner()
outer()
'''

def outer():                        #1.outer function defined
    print("outer function")         #3 print outer function
    def inner():                    #4 inner function defined
        print("inner function")     #6 print inner function
    inner()                         #5 inner function call
outer()                           #2 outer function call


