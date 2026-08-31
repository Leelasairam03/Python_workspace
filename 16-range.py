#range(stop)
#range(start,stop)
#range(start,stop,step)
#range is a class in python,we can create immutable objects from the range class.like tuple or string,lazy-memory efficient-doesn't generate all numbers at once,support indexing and slicing
#stop is the mandatory parameter,no default value.
#start and step are optional parameters,default value of start is 0 and default value of step is 1.
#uses - when you need a sequence of numbers.
#       for loop is used to iterate over the range.
#       to avoid creating large lists in memory.
#creates numbers only on demand while executing untill then nothing is created.
r=range(8)
print(r,type(r))
print(list(r)) #convert range to list
print(tuple(r)) #convert range to tuple


print(list(range(-9,2,2)))

