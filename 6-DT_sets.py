'''
1. sets, it is pre defined data type in python which is used to store multiple values in a single variable
2. does not allow duplicate values, it is unordered collection of data, it is mutable, it is iterable, it is unindexed, it is dynamic in nature
3. set allows both homogeneous and heterogeneous data, it is used to perform mathematical operations like union, intersection, difference, symmetric difference etc
4. memory allocation of sets is stored in a single block of memory, so it is faster than lists and tuples,uses hash table to store elements, so it is faster than lists and tuples
'''

#create an empty set
s=set() #empty set
print(s) #set()

s1={10,20,30,40,50,50,50} #set,even if we try to add duplicate values in the set it will not throw error but it will not add the duplicate values in the set
print(type(s1)) #<class 'set'>
print(s1) #{10, 20, 30, 40, 50}

'''methods of set'''

#add element to the set
s1.add(6) #add method is used to add element to the set
print(s1)

#remove element from the set
s1.remove(6) #remove method is used to remove specific element from the set,if element is not present then it will throw error-->key error
print(s1)

#discard method is used to remove specific element from the set,if element is not present then it will not throw error
s1.discard(6) #discard method is used to remove specific element from the set,if element is not present then it will not throw error
print(s1)

#pop method is used to remove random element from the set
s1.pop() #pop method is used to remove random element from the set
print(s1)

#clear method is used to remove all elements from the set
s1.clear() #clear method is used to remove all elements from the set
print(s1)

#update method is used to add multiple elements to the set,add using list
s1.update([1,2,3,4,5]) 
print(s1)

#adding string to the set using update method
s1.update("hello") #adding string to the set using update method
print(s1)

#adding string to the set using add method
s1.add("hello") #adding string to the set using add method  
print(s1)

#adding tuple to the set using update method
s1.update((88,99,100)) #adding tuple to the set using update method
print(s1)

#adding tuple to the set using add method
s1.add((77,88,99)) #adding tuple to the set using add method,stores the entire tuple as a single element in the set
print(s1)

#difference_update method is used to remove the elements of another set from the set
s2={1,2,3,4,5}  
s3={4,5,6,7,8}
s2.difference_update(s3) #difference_update method is used to remove the elements of another set from the set
print(s2) #{1, 2, 3}

#subset method is used to check if a set is a subset of another set
s4={1,2,3}
s5={1,2,3,4,5}
print(s4.issubset(s5)) #True, s4 is a subset of s5
print(s5.issubset(s4)) #False, s5 is not a subset of s4

#superset method is used to check if a set is a superset of another set
print(s5.issuperset(s4)) #True, s5 is a superset of s4
print(s4.issuperset(s5)) #False, s4 is not a superset of s5

#union method is used to combine two sets and return a new set
s6={1,2,3}  
s7={4,5,6}
s8=s6.union(s7) #union method is used to combine two sets and return a new set
print(s8) #{1, 2, 3, 4, 5, 6}

#intersection method is used to find the common elements of two sets
s9={1,2,3,4,5}
s10={4,5,6,7,8}
s11=s9.intersection(s10) #intersection method is used to find the common elements
print(s11) #{4, 5}

#disjoint method is used to check if two sets have no common elements
s12={1,2,3}
s13={4,5,6}
print(s12.isdisjoint(s13)) #True, s12 and s13 have no common elements
s14={1,2,3}
s15={3,4,5}
print(s14.isdisjoint(s15)) #False, s14 and s15 have common elements 

#symmetric_difference method is used to find the elements which are present in either of the sets but not in both
s16={1,2,3,4,5} 
s17={4,5,6,7,8}
s18=s16.symmetric_difference(s17) #symmetric_difference method is used to find the elements which are present in either of the sets but not in both
print(s18) #{1, 2, 3, 6, 7, 8}

#symmetric_difference_update method is used to update the set with the elements which are present in either of the sets but not in both
s19={1,2,3,4,5} 
s20={4,5,6,7,8}
s20.symmetric_difference_update(s19) #symmetric_difference_update method is used to update the set with the elements which are present in either of the sets but not in both
print(s20) #{1, 2, 3, 6, 7, 8}

#union_update method is used to update the set with the elements of another set
s21={1,2,3}
s22={4,5,6}
s21.update(s22) #union_update method is used to update the set with the elements of another set
print(s21) #{1, 2, 3, 4, 5, 6}

#difference method is used to find the elements which are present in the set but not in the other set
s23={1,2,3,4,5}
s24={4,5,6,7,8}
s25=s23.difference(s24) #difference method is used to find the elements which are present in the set but not in the other set
print(s25) #{1, 2, 3}