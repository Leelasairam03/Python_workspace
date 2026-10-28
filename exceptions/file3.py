print("start")
l=[10,20,30]
try:
    n=int(input("enter numerator"))
    d=int(input("enter denominator"))
    print(n/d)
    print(l[5])
except ZeroDivisionError as e1:
    print(e1)
except IndexError as e2:
    print(e2)
except ValueError as e3:
    print(e3)
print("end")
