#append
f=open("file/demo.txt","a")  #adds content to the file,file should exist if not it will create a new file
f.write("\na new line added")
f.writelines(["\nline1","\nline2","\nline3"])
f.close()
