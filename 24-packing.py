'''
packing:the process of packaging multiple values into a single variable.
1) manual packing - user decides which collection type (list,tuple,set,dict)the values should be packed into
2) automatic packing/implicit packing - the values are automatically packed into a tuple when they are assigned to a single variable without an explicit collection type

unpacking:the process of extracting multiple values from a collection into separate variables
'''
#implicit packing
a=10,20,30
print(a)
print(type(a))

#unpacking
x,y,z=a
print(x,y,z)

d={1:10,2:20,3:30}
a,b,c=d.values() #unpack values
print(a,b,c)

a,b,c=d   #unpack keys
print(a,b,c)

a,b,c=d.items() #unpack items into seperate tuples
print(a,b,c)


s="rcb"
a,b,c=s
print(a,b,c)


#Extend iterable unpacking using *,returns a list for any collection
l=[10,20,30,40,50]

a,*b,c=l
print(a,b,c)