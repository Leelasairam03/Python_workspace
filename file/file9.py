#with
with open("file/sample.txt","r") as f:
    print(f.read())
print(f.closed)   #file closed after exiting with