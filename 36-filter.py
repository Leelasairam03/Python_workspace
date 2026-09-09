def check_even(n):
    return n%2==0

def segregate(fun,l):
    even=[]
    for i in l:
        if fun(i):
            even.append(i)
    return even

        

l=[3,8,12,13,19,22]
print(segregate(check_even,l))

'''
filter function:
        - predefined higher order function
        - applies condition to each element in the iterable.
        - returns a filtered object(an iterator)(only true values are returned)
syntax - filter(function,iterable)
     function should take one argument and return one value(true or false)
     iterable ->sequence(list,tuple,etc)
'''

#filter
print(list(filter(lambda n:n%2==0,[3,8,12,13,19,22])))

l1=["lathik","YASHAS","sagar","RAJ","SAI","abin"]

print(list(filter(lambda name:name.isupper(),l1)))

print(list(map(lambda name:len(name),l1)))