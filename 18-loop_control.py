'''
loop control statement- used to control the flow of loop execution
1.break - exits the loop immediately,remaining iterations are skipped
2.continue - skips the current iteration,loop continues with next iteration,helps to ignore unwanted conditions
3.pass - does nothing,used as a placeholder

syntax:

for variable in iterable:
    statement(s)
    if condition:
        break/continue/pass
    statement(s)

while condition:
    statement(s)
    if condition:
        break/continue/pass
    statement(s)
'''
#break
print("--------break------------")
for i in range(51,71):
    if i%11==0:
        break
    print(i)
print("--------------------")
i=51
while i<71:
    if i%11==0:
        break
    print(i)
    i+=1
print("--------------------")
for i in range(45,68):
    if i%11==0:
        print(i)
        break
print("--------------------")
for i in range(45,68):
    if i%11==0 and i%3==0:
        print(i)
        break
print("--------------------")
rolls=[497,19390,32,18,7,38,24]
for i in rolls:
    if i==18:
        print("found",i)
print("---------continue------------")
for i in range(43,63):
    if i%3==0:
        continue
    print(i)
print("---------continue------------")
for i in range(43,63):
    if i%2==0 and i==5:
        continue
    print(i)
print("---------continue------------")
marks=[45,-74,62,74,52,-48,92,-35,27,93]
for i in marks:
    if i<=0:
        continue
    print(i)
print("---------continue------------")
names=["nandan","basu","raj","om","raghu","shravani","daniel"]
for i in names:
    if len(i)==5:
        break
    if len(i)<5:
        continue
    print(i)

print("--------pass------------")
if 5<6:
    pass

