print("start")
l=[10,20,30]
try:
    n=int(input("enter numerator"))
    d=int(input("enter denominator"))
    print(n/d)
    print(l[5])
except Exception as e:
    print(e)
print("end")
