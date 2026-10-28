#writing
f=open("file/demon.txt","w") #clears the file content and writes new content , if file doesn't exist it creates a new file
f.write("this is new line")
print(f.writable())
f.writelines(["\nline1","\nline2","\nline3"])
#print(f.readlines())  #unsupported operation: not readable
print(f.tell())
f.close()

