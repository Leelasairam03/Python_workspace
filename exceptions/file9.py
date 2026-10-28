def division(n,d):
    print(n/d)
try:
    division(10/0)                   #prefer placing the try,except to the caller instead of inside the function
except ZeroDivisionError as e:
    print(e)
