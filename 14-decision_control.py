'''
#Decision Control Statements - used to control the flow of execution of a program based on certain conditions.
                             - they allow the program to decide what to execute depending on true/false condititons.
indentation- providing space before the statement(1 tab space)
             in python indentation is mandatory to define any block of code, unlike other languages where braces {} are used.
             ex: if block,function block,loop block,class block
#types:
        1.if statement
        2.if else statement
        3.if elif else statement
        4.nested if statement
        5.match statement
'''
#if statement- if is a keyword in python,it executes the indented block of code only when the condition passed is true
#syntax: if condition:
#            code_block
#it is used to check a single condition

print("if statement")
marks=80
print("start of the program")
if marks>35:
    print("you passed")
print("end of the program")

students={21:"krishna",49:"balram",99:"kamsa"}
if "kamsa" in students.values():
    print("Danger")

#if-else statement- it is used to check a single condition,if the condition is true it executes the indented if block of code,else it executes the else block of code
#note:else is not followed by a condition and it should be written at the same level as that of the if block
#use if-else when the condition can only be true or false,only one among the 2 blocks are executed
#syntax: if condition:
#            code_block
#        else:
#            code_block
print("\nif-else statement")
marks=35
if marks>=35:
    print("congratulations you passed")
else:
    print("Better luck next time")

'''
name=input("enter the name: ")
if len(name)>8:
    print("username valid")
else:
    print("username invalid")
'''
'''
#accept a sentence from the user , if the sentence has more than 4 words print "valid sentence" otherwise print "invalid sentence"
sentence=input("enter a sentence: ").strip()
if len(sentence.split())>4:
    print("valid sentence")
else:
    print("invalid sentence")
'''

#if-elif-else statement- it is used to check multiple conditions,if the first condition is true it executes the indented if block of code,else it checks the next elif condition,if it is true it executes the indented elif block of code,else it executes the else block of code
#note:elif is followed by a condition and it should be written at the same level as that of the if block
#used when the condition can be true or false,or many true/false scenarios,only one among the if,elif,else block is executed
#syntax: if condition1:
#            code_block1
#        elif condition2:
#            code_block2
#        elif condition3:
#            code_block3
#        ...
#        else:
#            code_block

print("\nif-elif-else statement")

#accept the temperature from user if temperature is <8 then print "freezing",if temperature is between 8 and 14 then print "cold",if temperature is between 15 and 35 then print "warm",if temperature is greater than 35 print "hot"
temp=30.5
if temp<8:
    print("freezing")
elif temp>=8 and temp<=14:
    print("cold")
elif temp>=15 and temp<=35:
    print("warm")
else:
    print("hot")

#marks
marks=1000
if marks>=90 and marks<=100:
    print("grade A")
elif marks>=70 and marks<90:
    print("grade B")
elif marks>=50 and marks<70:
    print("grade C")
elif marks>=35 and marks<50:
    print("grade D")
elif marks<35 and marks>=0:
    print("fail")
else:
    print("invalid marks")

#match statement- it is used to match a value with multiple cases,if the value matches with any case it executes the indented code block of that case,else it executes the default block of code
#syntax: match value:
#            case pattern1:
#                code_block1
#            case pattern2:
#                code_block2
#            case _:
#                code_block
print("\n match statement")
#match can work with single value or multiple values, match,case,_,type are soft keywords
choice=6
match choice:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7|0:
        print("Sunday")
    case _:
        print("invalid choice")

#nested if statement- it is used to check a condition inside another if condition
#syntax: if condition1:
#            if condition2:
#                code_block1
#            else:
#                code_block2
#        elif condition3:
#            code_block3
#        ...
#        else:
#            code_block
'''
#accept the age and citizenship from user,if the age is greater than or equal to 18 and the citizenship is true then print "eligible for voting" else print "not eligible for voting"
age=int(input("enter the age: "))
is_citizen=eval(input("are you indian: "))
if age>=18:
    if is_citizen==True:
        print("eligible for voting")
    else:
        print("not eligible for voting")
else:
    print("not eligible for voting")
'''
#design a nested conditon wherein accept username and check if it is correct
#only if it is correct,accept the password

username="sairam"
password="sairam123"

user_input=input("enter the username: ")
if user_input==username:
    print("username is correct")
    pass_input=input("enter the password: ")
    if pass_input==password:
        print("login successfull")
    else:
        print("incorrect password")
else:
    print("username not found")
    

