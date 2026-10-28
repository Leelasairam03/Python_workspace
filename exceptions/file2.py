print(1)
print(2)
l=[10,20,30]
try:
    print("inside try block")
    print(l[4])
    print("normal flow")
except IndexError as e:
    print(e)
    print("exception handled")
print(3)
print(4)