'''
global variables - these are the variables which are declared outside the function and can be accessed anywhere in the program
                 - can be modified outside the function,but to modify inside a function.we need to use global keyword or else it will throw unboundlocalerror
local variables -  these are the variables which are declared inside the function and can be accessed only inside that function
                  - cannot be accessed outside the function
                  - can be modified only inside

'''
#global variables
x=20  #global variable

def display():
    print("accessing global variable inside the function:",x)

print("accessing global variable outside the function:",x)
display()

#modifying global variable inside a function
def modify():
    global x
    x=30
    print("modified global variable inside function:",x)

print("global variable before modification:",x)
modify()
print("global variable after modification:",x)

print("---------local variables------------")
#local variable
y=10 #global variable

def display_local():
    y=20 #local variable
    print("local variable inside the function:",y)

print("global variable outside the function:",y)
display_local()
print("global variable outside the function:",y)

