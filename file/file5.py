# read and write, pointer is at the starting for both read and write, for write it overwrites the file
f=open("file/demo.txt","r+") #file should exist
print(f.tell())   #to find the current position of the file pointer
print(f.read())     #reads from the current position of the file pointer
f.write("\nnew line added")   #overwrites the file from the current position of the file pointer
f.close()
