'''
closure is a nested function that remembers the values of the enclosing variables even after outer function is executed
1.outer function with a local variable
2.inner function accessing the outer function variable
3.outer function returns inner function
when we call outer function it returns inner function
when we call inner function it prints the value of outer function variable

example:
def outer():
    x=10
    def inner():
        print(x)
    return inner
outer()()


'''

def outer():
    print("outer function")
    x=10
    def inner():
        print(x)
    return inner
inner=outer()  #outer function is executed and its local variable is destroyed
inner()        #inner function is executed and it remembers the value of outer function variable
print("-----------------------")
def get_color():
    color="red"
    def show_color():
        print(color)
    return show_color
show_color=get_color()
show_color()
print("-------------------")
def counter():
    count=0
    def increment():
        nonlocal count
        count=count+1
        print(count)
    return increment
increment=counter()
increment()
increment()
increment()
