#write and read
f=open("file/sample.txt","w+") #data is gone
f.writelines(["hello"," good morning"]) # cannot read after writing,cursor has moved to the end of the file
f.seek(0)   #move the file pointer to the starting
print(f.read())   #reads from the current position of the file pointer
f.close()
