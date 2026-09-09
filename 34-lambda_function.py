'''
lambda functions are anonymous functions 
they are defined without a name and are used for small and simple operations
they are defined using the lambda keyword
they can have any number of arguments but only one expression

note: it is best when we need to pass simple helper function for a higher order function

syntax:
lambda parameters:expression
'''

add=lambda x,y:x+y
print(add(10,20))

check_even=lambda n:n%2==0
print(check_even(2))

print((lambda n:n**2)(2)) #square
print((lambda a,b:a+b)(10,20)) #add
print((lambda n:n%2==0)(10)) #check even


def transform(fun,col):
    l1=[]
    for i in col:
        num=fun(i)
        l1.append(num)
    return l1

l=[10,20,30,40,50]

print(transform((lambda n:n**2),l))
print(transform((lambda n:n**3),l))