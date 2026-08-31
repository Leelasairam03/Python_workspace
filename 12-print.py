'''
print()- it is a pre-defined function in python which is used to display output on the console/screen.
       - it helps the programmer to see the results of the program/code execution.
       - it has 2 default arguments:
                1. sep-separator: it is used to separate the arguments.(default value - " ")
                      - whenever multiple values are to be printed using print() the value of the seperator will be printed in between those values.
                      - Syntax: print(arg1,arg2,arg3,....,sep="value")
                      - if we do not provide value to the sep argument it will take the default value of sep argument i.e " "
                      - if there are n values to be printed the seperator value will be printed n-1 times in between the values.
                2. end-end: it is used to end the output.(default value - "\n")
                      - whenever the print() function is called it will print the output and then it will end with the value of the end argument.
                      - if we do not provide value to the end argument it will take the default value of end argument i.e "\n"

'''

print("hello","world",sep="@")
print("hello","world",sep="\n")
print()
print("hello","world",end=".")
print("hi")
