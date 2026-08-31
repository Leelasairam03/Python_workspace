'''
for-else:
    when loop completes normally (without break) else block is executed, or if break is encountered else doesn't execute(when loops gets interrupted)
syntax:
for variable in iterable:
    statement(s)
    if condition:
        break
else:
    statement(s)
'''
for i in range(1,5):
    if i==3:
        break
    print(i)
else:
    print("loop completed normally")
print("------------------")
for i in range(1,5):
    print(i)
    continue
else:
    print("else block")

roll=[2,4,1,6,8,10,19]
rono=int(input("enter roll no"))
for i in roll:
    if rono==i:
        print("rollnumber found")
        break
else:
    print("roll not found")