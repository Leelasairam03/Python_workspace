'''
zip fucntion:
-it is a pre defined function in python that combines multiple iterables element by element 
-it creates tuples of corresponding elements from each iterable 
-it accepts 2 or more iterables and returns zip object(which is list of tuples)

syntax- zip_obj=zip(iterable1,iterable2,....)

note: - each element in a zip object is a tuple
      - zip stops at the shortest iteration
      - it is used for mapping and pairing
'''

rolls=[32,40,60,33]
names=['amy','ben','chad','denzo']

#make rolls and names into dictionary
zip_obj=zip(rolls,names)
print(list(zip_obj))

rolls=[32,40,60,33,12,40,55]
zip_obj=zip(rolls,names)   #stops at shortest iteration
print(list(zip_obj))

rolls=[2,3,4,5,6,7]
marks=[30,65,90,50,25,95]

dc={k:("pass" if v>35 else "fail") for k,v in zip(rolls,marks)}
print(dc)

