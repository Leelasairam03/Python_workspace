#tuples
t1=(1,2,3,4,5) #tuple
dtt=type(t1)
print(dtt)

#it is a pre defined data type in python which is used to store multiple values in a single variable
#tuples are immutable, so we cannot modify them after creation
#t1[0]=10 #TypeError: 'tuple' object does not support item assignment
#memory allocation of tuples is stored in a single block of memory, so it is faster than lists
#memory allocation of lists is stored in multiple blocks of memory, so it is slower than tuples

#we can access elements of a tuple using indexing,if index is not present then it will throw error-out of range error
print(t1[0]) #1
print(t1[-1]) #5

#we can slice a tuple,while slicing tuple indexing starts from 0 and ends at n-1 where n is the length of the tuple
print(t1[1:4]) #(2, 3, 4)

#we can find the length of a tuple
print(len(t1)) #5

#we can count the number of occurrences of an element in a tuple
t2=(1,2,3,4,5,2,2,2) #tuple
print(t2.count(2)) #4

#we can find the index of an element in a tuple,if duplicate elements are present then it returns the index of the first occurrence of the element
print(t2.index(2)) #1 if trying to find the index of an element which is not present in the tuple then it will throw error-gives value error

#we can concatenate two tuples
t3=(6,7,8,9,10)
t4=t1+t3 #concatenation of two tuples
print(t4) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#we can repeat a tuple
t5=t1*2 #repetition of a tuple
print(t5) #(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

#we can check if an element is present in a tuple
print(2 in t1) #True
print(6 in t1) #False

#we can check if an element is not present in a tuple
print(2 not in t1) #False
print(6 not in t1) #True

#creating empty tuple
t6=() #empty tuple
print(t6) #()
#creating empty tuple using class
t7=tuple() #empty tuple using class
print(t7) #()
#creating tuple with single element
t8=(1,) #tuple with single element
print(t8) #(1,)