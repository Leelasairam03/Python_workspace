print("start")
l=[10,20,30]
try:
    print(l[1])             #risky code
except Exception as e:
    print(e)                #handles the exception if it occurs
else:
    print("else block")     #excecutes only if exception is not occured
finally:
    print("finally block")  #executes always
