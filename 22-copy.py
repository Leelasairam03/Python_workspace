'''
l1=[1,2,3]
l2=l1 # if we modify any of the list,both will be modified,general copy
copy()-creates new list, and modifying one list won't affect the other,shallow copy
      - changes in nested elements still affects both copies in shallow copy
deepcopy()-creates new list, and modifying one list won't affect the other,deep copy
      - it is used to copy nested collections completely
      -recursively copies objects
'''
#copy
import copy
l1=[1,2,3]
l2=copy.copy(l1)
l2.append(4)
l1.append(5)
print(l1)
print(l2)

#deep copy
l1=[[1,2],[3,4]]
l2=copy.deepcopy(l1)
l2.append([5,6])
l1.append([7,8])
print(l1)
print(l2)
