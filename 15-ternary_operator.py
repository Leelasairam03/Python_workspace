#ternary operator/conditional operator,short hand form of if-else
#Syntax: expression_if_true if condition else expression_if_false
num=10
result="positive" if num>0 else "negative"
print(result)

#if num>0 -num+100, else num-100
result1=num+100 if num>=0 else num-100
print(result1)

#list
l=["mohan","rohini","kiran"]
result2=len(l) if "kiran" in l else "name is not present"
print(result2)

