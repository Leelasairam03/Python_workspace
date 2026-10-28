#read
f=open("file/demo.txt","r")
print(f.readable())
print(f.writable())
#print(f.read())  #reads entire file
print(f.read(5))  #reads first 5 characters,if i want to read again it resumes from where it left
print(f.tell())   #return the current position of the file pointer
f.seek(0)   #move the file pointer to the specified position
print(f.tell())
print(f.readlines()) #reads all the lines in the file in the form of list
#print(f.write("this is new line")) #error because file is opened in read mode, unsupported operation : not writable
f.close()

