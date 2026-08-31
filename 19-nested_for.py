#nested for loops- one for loop inside another for loop
'''
syntax:
for outer_variable in outer_iterable:
    statement
    for inner_variable in inner_iterable:
        statement(s)
'''
for i in range(2,5):
    for j in range(1,4):
        print(f"{i} * {j} = {i*j}")
print("------------------------")      

main=["dosa","idli","poori"]
sides=["chutney","sambar","aloo curry"]
for i in main:
    for j in sides:
        print(f"{i}---->{j}")
print("------------------------")      
