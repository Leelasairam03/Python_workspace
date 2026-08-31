#input function- it is a builtin function in python used to take input from the user through keyboard
#whatever the user enters is recieved in the form of string
#WHY input- when the user/programmer plans to write interactive programs that takes data from an external entity we use input function
#use cases - menu driven, calculator etc.
#syntax : variable = type(input("prompt"))

name= input("Enter your name:")
print(f"hello {name}")
age= int(input("enter your age:"))  #explicit type casting/parsing/coercion
print("your age is",age)
if age>18:
    print(f"{name},you are eligible for voting!")
else:
    print(f"{name},you are not eligible for voting!")

print(float(input("enter your height:"))+2.1)

iscitizen=bool(input("are you indian citizen?")) #entering false also becomes true because 'false' it is truthy valur
print(iscitizen)
print(type(iscitizen))


''' eval()'''
#overcoming the flaw of input function, eval()
#eval()-builtin function, evaluates string as a python expression and retunrs the result
#syntax- eval(input("prompt"))

result=eval(input("are you indian citizen?"))
print(result)
print(type(result))

result1=eval(input("enter a python expression:"))
print(result1)
print(type(result1))

a=100
b=25
res=eval("a-b+100")
print(res)

l=[10,20,30]
res2=eval("len(l)+24")
print(res2)

print(type(eval("(10,10,10)"))) #automatically does type casting