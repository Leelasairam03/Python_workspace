'''
map function:
        - predefined higher order function
        - applies a given function to each item in iterable.
        - returns a map object(an iterator)
syntax - map(function,iterable)
     function should take one argument and return one value
     iterable ->sequence(list,tuple,etc)

'''
print(list(map(lambda n:n**2,[10,20,30,40,50])))
print(list(map(lambda n:n+50,[10,20,30,40,50])))

