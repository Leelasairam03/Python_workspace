def add(a,b):
    return a+b

def compress(fun,l):
    sum=0
    for i in l:
        sum=fun(sum,i)
    return sum

l=[10,20,30,40,50]
print(compress(add,l))

''' 
reduce function:
        - predefined higher order function
        - it's a function from functools module(from functools import reduce)
        - applies a given function to each item in iterable in a cumulative way.
        - returns a single value
syntax - reduce(function,iterable)
          function should take two arguments and return one value
          iterable ->sequence(list,tuple,etc)
'''
from functools import reduce
print(reduce(lambda a,b:a+b,[10,20,30,40,50]))

print(reduce(lambda a,b:a*b,[10,20,30,40,50]))


print(list(map(lambda x:x**2,(filter(lambda n:n%2==0,[10,15,20,25,30,25])))))

