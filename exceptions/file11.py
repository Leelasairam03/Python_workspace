#raise our own exception object
print(1)
try:
    raise ZeroDivisionError("my own exception")  
except:
    print("handled")
print(2)

