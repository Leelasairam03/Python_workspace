'''
looping- repeating a block of code for a specified number of times or until a certain condition is met.
#also used to traverse elements in collections
why to use-
- avoid code duplication
- automate repetitive tasks
- iterate through collections
types:
1.For loops - used when we know the number of iterations,iterating over sequence,works with range
            #syntax-for variable in iterable:
                        statement(s)
            - variable recieves one element at a time from the sequence,iteration ends when all elements are traversed
            - loop body executes each time the variable/element is recieved
        
2.While loops - used when we dont know the number of iterations,condition based
            #syntax-while condition:
                        statement(s)
                        updation code
            - condition is checked before each iteration
            - if condition is true,loop body executes
            - if condition is false,loop terminates
3.For each loop - used for iterating over the elements of a collection
'''
l=[10,20,30,40,50,60,70]
for i in range(0,len(l),3):
    print(l[i])
print("---------------------------")
for i in range(5,0,-2):
    print(l[i])
print("---------------------------")
s={11,22,33,44}
d={1:10,2:20,3:30}

for i in s:
    print(i)
print("---------------------------")
for i in d:    #we get only keys
    print(i)
print("---------------------------")
for i in d.values():  #gives values
    print(i)
print("---------------------------")
for i in d.items():   #guve both key,value tuples
    print(i)
print("---------------------------")

st="aizen"
for i in st:
    print(i)
print("---------------------------")

dictionary={"goku":"DragonBallz","yagami":"Deathnote","ichigo":"Bleach","migi":"parasyte"}

for i in dictionary:
    if i=="yagami":
        print(dictionary[i])
print("---------------------------")
for i in dictionary:
    if "i" in i:
        print(dictionary[i].upper())
print("---------------------------")

print("--------------while loop-------------")

i=1#initialisation
while i<=5:#condition
    print("hello")
    i+=1#updation
print("---------------------------")
i=51#initialisation
while i<=60:#condition
    print(i)
    i+=1#updation
print("----------------------------")
i=8
while i>1:
    print(i)  #8 7 6 5 4 3 2
    i-=1
print("----------------------------")
i=80
while i>61:
    print(i)  #80 77 74 71 68 65 62
    i-=3
print("----------------------------")
l=[90,80,70,60,50,40,30,20,10]
i=0
while i<len(l)-1:
    print(l[i])
    i+=2
print("----------------------------")