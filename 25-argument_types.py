'''
argument types in python:
1.positional/sequenced arguments
2.keyword arguments
3.default arguments
4.variable length arguments
    a)arbitrary arguments (*args)
    b)keyword arbitrary arguments (**kwargs)

#positional arguments - values are passed in the same order as function definition
def add(a,b):
    return a+b
print(add(10,20))

#keyword arguments - values are passes along with it's parameter names (order doesnt matter)
print(add(b=20,a=10))

#default arguments - values are set in function definition (can be overridden)
def add(a=10,b=20):
    return a+b
print(add())

#variable length arguments - *args collects all positional arguments into a tuple
def add(*args):     # *args can be used only once in the function definition and it should come after positional arguments.
    return sum(args)
print(add(10,20,30,40,50))

#keyword arbitrary arguments - **kwargs collects all keyword arguments into a dictionary
def add(**kwargs):  # **kwargs can be used only once in the function definition and it should come after positional arguments.
    return sum(kwargs.values())
print(add(a=10,b=20,c=30,d=40,e=50))
'''
#positional arguments
def add(a,b):
    return a+b
print(add(10,20)) #  order matters,10 goes to a, and 20 goes to b

#keyword arguments
print(add(b=20,a=10)) # order does not matter

print("--------------------------")
#args
def fun(a,b,c):
    print(a,b,c)
l=[10,20,30]
fun(*l)  # unpacking , note:number of parameter passed in function call should be equal to number of elements in list

def sum_values(*args):  
    return sum(args)
print(sum_values(10,20,30,40,50))  #packing

def argument(*args):  #packing of *args
    print(args)   
l=[10,20,30,40,50]
argument(*l)#unpacking of *args

#kwargs
def display(**kwargs):#packing of **kwargs
    print(kwargs)
display(a=10,b=20,c=30,d=40,e=50)


def sum_values(**kwargs):
    print(sum(kwargs.values()))

d={'a':10,'b':20,'c':30,'d':40,'e':50}
sum_values(**d)#unpacking of **kwargs

d1={'a':10,'b':20,'c':30,'d':40,'e':50}
sum_values(**d1)#unpacking of **kwargs

#default arguments
def greet(name="Guest"):
    print("Hello",name)
greet()
greet("Sai")

#combine all 4 types in one function
def sample(a,*args,b=10,**kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

# Call with positional args for a, b, and *args, and keyword args for **kwargs (not reusing parameter names 'a' or 'b')
l=[3,4,5]
d={'c':3,'d':4}
sample(1,*l,**d)
