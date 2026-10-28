'''
file handling
-data is lost when program is terminated
-so we have to store data persistently,we can store it in a file on secondary storage such as an ssd,hard disk,or pendrive.
-then the data remains available even after termination

file - a file is a named location on a storage device where data is stored permanently so that we can use it later.

file handling - creating,closing,reading,writing files using a program

1)text files- stored data as characters/text  --->  .txt
2)binary files- store data in binary form(generally not intended to read by human)   --->audio,vedio,images(.mp3,.mp4,.jpg)
3)database used when data becomes structured and large

syntax:
file_obj=open("file_name","mode")

file_name- name of the file to be opened including the path 

mode- determines the mode in which the file is to be opened i.e. to read,write or both
    - r - read (default mode)  -> file should exist,it opens the file in read mode,if file does not exist it raises FileNotFoundError
    - w - write -> creates file if it doesn't exist,clears the content of the file if it exists , and write operation can be performed
    - a - append  -> file should exist if not it will create a new file,adds content to the file at the end
    - r+ - read and write -> file should exist if not it will raise FileNotFoundError
    - w+ - write and read -> file may or may not exist,clears the content if it exists,and write operation can be performed, read operation can be performed only after write
    - a+ - append and read -> file may or may not exist,adds content to the file at the end, read operation can be performed
    - x (exclusive) - create a new file -> if file exists it will raise FileExistsError,creates file if it doesn't exist,and write operation can be performed

file_obj.close()  #close file operation

file methods:
reading methods
1. file_object.readable() - returns True if file is opened in read mode
2. file_object.writable() - returns True if file is opened in write mode
3. file_object.read(n) - reads n characters from the file
4. file_object.readline(n) - reads n lines from the file
5. file_object.readlines() - reads all the lines from the file

writing methods
1. file_object.write("string") - returns the number of characters written in the file
2. file_object.writelines(iterable of strings) - returns the number of characters written in the file 

additional methods
1. file_object.tell() - returns the current position of the file pointer
2. file_object.seek(offset,whence) - move the file pointer to the specified offset
3. file_object.close() - close the file operation

attributes:
    1)file_object.name - returns the name of the file
    2)file_object.mode - returns the mode in which the file is opened
    3)file_object.closed - returns True if file is closed

1. open() : open a file 
    syntax: open(filename,mode)
    
    it is a built in python function that opens a file and establishes a connection between the python program and the file,.
    returns file object through which we can perform operations
    file_object=open("file_name","mode")
    file_object.close()

2. with statement : used to open a file and close it automatically after the operations are performed
syntax:
with open(file,mode) as file_object:
    # perform operations on file_object   
    # close() is not required    
    #closed even if exception occurs

-----------------------------------------------
serialization
process of converting an object(datastructure) into byte stream to store it in a file or database or to send it over a network
that format is usually

1.json (javascript object notation) - readable
2.binary format - not readable(pickle)

json module- for handling json files - only for pre defined types(lists,dict,int,float,str,tuple,bool,none)

1.dumps() - return in json string format
dumps(python object)
2.dump() - writes in file
dump(python object,file_object)

deserialization: convert json into python object
3.loads() - json string -> python object
obj=loads(json_string)

4.load() - json file -> python object
obj=load(file_object)

pickle module- for handling custom objects (classes and objects)
1.dump() - pickle.dump(obj,file_object)
2.load() - pickle.load(file_object)

pickling - conversion of python object to byte stream
1.dump() - pickle.dump(obj,file_object)
2.dumps() - pickle.dumps(obj) - return in binary string format

unpickling - conversion of byte stream to python object
3.load() - pickle.load(file_object)
4.loads() - pickle.loads(binary_string) - return in python object


'''