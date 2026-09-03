'''
decorator is a function that 
-takes another function as input
-adds extra behaviour
-returns a new function

steps:
1)define a nested function
2)outer function should take one parameter(which is the function to be decorated)
3)decorator logic should be in the inner function
4)the outer function should return the inner reference

note: 1)the outer functionname usually can be named as decorator and inner function can be named as wrapper
      2)wrapper function parameters should be same as the function to be decorated

syntax:
@decorator_name
def function_name():
    pass
'''
def decorator(fun):
    def wrapper():  #0 parameters
        print("select gift paper")
        fun()
        print("add label to the gift")
    return wrapper

def gift():      #0 parameters
    print("coffee mug gift")

gift=decorator(gift)
gift()

print("-----------------------")


def decor(fun):
    def wrap():
        print("put the cake in box")
        print("place the candle")
        print("add the label to the cake box")
        fun()
    return wrap
def cake():
    print("cake is ready")

cake=decor(cake)
cake()


print("-------------------------------------")
def decorator(fun):
    def wrapper(name):  #0 parameters
        print("select gift paper")
        fun(name)
        print("add label to the gift")
    return wrapper

def gift(name):      #0 parameters
    print(f"prepare {name} gift")

gift=decorator(gift)
gift("smiling buddha")

print("------------------------------")
def decor(fun):
    def wrap(name,cost):
        print("put the cake in box")
        print("place the candle")
        print("add the label to the cake box")
        fun(name,cost)
    return wrap
def cake(name,cost):
    print(f"{name}cake is ready which cost {cost}")

cake=decor(cake)
cake("death by chocalate",1500)

print("-------------------------------")
def decorator(fun):
    def wrapper(*args):
        print("take the gift paper")
        fun(*args)
        print("add a label")
    return wrapper
def gift(*args):
    print("gift selected",args)

gift=decorator(gift)
gift("teddy","global gift store",500)

print("------------------------------")
def decor(fun):
    def wrap(*args):
        print("making in progress")
        fun(*args)
        print("pack the cake in box")
        print("cake is delivered")
    return wrap
def cake(*args):
    print("ingridients",args)

cake=decor(cake)
cake("bread","cream","mold","egg","water","Salt","Sugar","yeast")

print("------------------------------")

def decorator(fun):
    def wrapper(**kwargs):  #0 parameters
        print("select gift paper")
        fun(**kwargs)
        print("add label to the gift")
    return wrapper

def gift(**kwargs):    
    print(f"prepared {kwargs}")

gift=decorator(gift)   #manual
gift(ceramic="smiling buddha",cost=5000)

print("------------------------------")
def decorator(fun):
    def wrapper(*args,**kwargs):  
        print("select gift paper")
        fun(*args,**kwargs)
        print("add label to the gift")
    return wrapper

@decorator                     #automatic(name is given same as outer function which is acting as decorator, ex:@baker,@chef,@gift)
def gift(*args,**kwargs):      
    print(f"prepared {args} , {kwargs}")

#gift=decorator(gift)
gift("global gift store",ceramic="smiling buddha",cost=5000)

print("---------------------------------")

def operation(fun):
    def wrapper():  #0 parameters
        print("function started")
        fun()
        print("function ended")
    return wrapper

@operation
def login():
    print("login operation")

@operation
def payment():
    print("payment operation")

@operation
def logout():
    print("logout operation")

login()
print("---------")
payment()
print("---------")
logout()

