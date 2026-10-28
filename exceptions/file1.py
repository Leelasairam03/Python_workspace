print(1)
print(2)
print(3)
try:
    print(hi) #abnormal flow  variable name error
    print("how are you")  # will be skipped if above lines generate an exception
except NameError:
    print("handled") #abnormal flow  variable name error
print(4)
print(5)

