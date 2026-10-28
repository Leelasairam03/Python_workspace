# append and read
f=open("file/sample.txt","a+") # pointer at the end
f.write("\nappended data") #writes at the end
f.seek(0)
print(f.read())
f.close()
