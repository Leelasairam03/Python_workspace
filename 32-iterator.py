'''
iterator is an object that can iterate through all the elements of collection one by one
-without needing to know the structure of the collection
-it is unidirectional(iterates from left to right, cannot go back)
-it supports partial iteration(can stop iteration anytime)
-after iteration is done, it raises StopIteration exception
-after iteration is done, it cannot be reset or reused(single use object)

it has two methods
    iter(collection/iterable) -> takes an iterable(list,tuple,set,dict) and returns an iterator object
                  the iterator object keeps a cursor(internal pointer) that moves to next element everytime next() is called
    next(iteratorobject) -> returns the next item
'''
l=[10,20,30,40]
itr_obj=iter(l)
print(itr_obj)
print(next(itr_obj))
print(next(itr_obj))
print(next(itr_obj))
print("hello")   #perform some unrelated operation
print(next(itr_obj)) #returning back to the iteration after unrelated operation

itr_obj=iter(l)
for i in itr_obj:
    print(i)

itr_obj=iter(l)
print(tuple(itr_obj))

itr_obj=iter(l)
i=0
while i<len(l):
    print(next(itr_obj))
    i+=1