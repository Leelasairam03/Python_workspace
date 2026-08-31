#datatypes- it represents the nature/type of data assigned to variable
'''
single valued data types-
1) int-
        number without decimal point
        +ve,-ve,0
        default value is 0
2)float
        number with decimal point
        +ve,-ve,0.0
        default value is 0.0
3)bool
        it represents T- true, F-false
        bool is sub class of int
        true- 1,false- 0
        default value of boolean is false F
4)complex
        it is a combination of real part and imaginary part where in the imaginary part is compulsory and is represented using j/J.
        c=+-p +-q j, p-real part, q - imaginary part
        default value is 0j

multivalued data types-
1) mutable-
        1. list
        2. set
        3. dict
2) immutable-
        1. tuple
        2. str
'''
age=23 #int
dt=type(age)
print(dt) # type returns the data type of the object
print(int()) #default value of int

fl=12.0 #float
dtf=type(fl)
print(dtf)
print(float()) #default value of float

boolean=True
dtb=type(boolean)
print(dtb)
print(bool()) #default value of bool

comp=8j
dtc=type(comp)
print(dtc)
print(complex()) #default value of complex


#lists
l1=[1,2,3,4,5] #list
dtl=type(l1)
print(dtl)

#insert element in list
l1.append(6) #append method is used to insert element at the end of the
print(l1)

#pop method is used to remove element from the end of the list
l1.pop() #pop method is used to remove element from the end of the list,takes index as argument,if index is not provided then it removes the last element of the list
print(l1)

#insert element at specific index of the list
l1.insert(2,10) #insert method is used to insert element at specific index
print(l1)

#remove element from the list
l1.remove(10) #remove method is used to remove specific element from the list,if duplicate elements are present then it removes the first occurrence of the element
print(l1)
'''
#if trying to remove element which is not present in the list then it will throw error,gives value error
l1.remove(10) #ValueError: list.remove(x): x not in list

'''
#remove all elements from the list
l1.clear() #clear method is used to remove all elements from the list
print(l1)

l2=[1,2,3,4,5,2,2,2] #list
#count method is used to count the number of occurrences of an element in the list
print(l2.count(2)) 
print(l2.count(6)) #if element is not present in the list then it returns 0

#index method is used to find the index of an element in the list
print(l2.index(2)) #returns the index of first occurrence of the element
#print(l2.index(6)) #if element is not present in the list then it will throw error

##sort method is used to sort the elements of the list in ascending order
l2.sort() #sort method is used to sort the elements of the list in ascending order
print(l2)

#reverse method is used to reverse the elements of the list
l2.reverse() #reverse method is used to reverse the elements of the list
print(l2)

#copy method is used to create a copy of the list
l3=l2.copy() #copy method is used to create a copy of the list
print(l3)

#extend method is used to add elements of one list to another list
l4=[6,7,8,9,10]
l2.extend(l4) #extend method is used to add elements of one list to another list
print(l2)       