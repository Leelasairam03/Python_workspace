#single line comment

'''multi
line
comment'''

'''variable - it is named container for storing data values
            - memory locatiof an object
            - variable name=value
'''
a=10 #intialisation of variable - assigning a value to variable
print(a)

a=100 # reassigning a new value to variable a
print(a)

#different variables with same value point to same memory location
x=10
y=10

z=id(x) #returns the memory location of the object
print(z)

w=id(y) #returns same memory location as x
print(w)