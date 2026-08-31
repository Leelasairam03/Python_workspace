'''
#operators-are the symbols/keywords which perform any operation on the operands.
#operands- are the values on which the operators perform any operation.
#types of operators:
        1.Arithmetic operators
          #addition
          #subtraction
          #multiplication
          #division
          #modulo
          #floor division
          #exponent
        2.Comparison operators
          #less than 
          #greater than
          #less than or equal to
          #greater than or equal to
          #equal to
          #not equal to
        3.Logical operators
          #and
          #or
          #not
        4.Assignment operators
          =
          +=
          -=
          *=
          /=
          //=
          %=
          **=
        5.Identity operators
          #is
          #is not  
        6.Bitwise operators
          &
          |
          ^
          ~
          <<
          >>
        7.Membership operators
          #in
          #not in
#syntax: op1 operator op2
'''
#arithmetic operators
print("arithmetic operators:")
num1=100
num2=20
print("addition: ",num1+num2)
print("subtraction: ",num1-num2)
print("multiplication: ",num1*num2)
print("division: ",num1/num2)
print("modulo: ",num1%num2)
print("floor division: ",num1//num2)
print("exponent: ",3**3)

#assignment operator
print("assignment operator:")
a=10
b=3
a+=b
print(a)

a=10
a-=b
print(a)

a=10
a*=b
print(a)

a=10
a/=b
print(a)

a=10
a//=b
print(a)

a=10
a%=b
print(a)

a=10
a**=b
print(a)
print()

#comparision operators/relational operators
print("comparision operators")
a=50
b=30

c=a==b
d=a!=b
e=a<=b
f=a>=b
g=a<b
h=a>b
print(c,d,e,f,g,h)
print()

#logical operators- used to evaluate/combine conditions, and,or, not are key words/operators
#they return actual values(true/false), not booleans, if the operands are true/false the operator will return true/false
#but if the operands are not true/false the operator will return the actual values
#also called short circuiting operators
# A and B, if A is true, then B is returned, else A is returned
# A or B, if A is true, then A is returned, else B is returned
# not A, if A is true, then False is returned, else True is returned
print("logical operators")
a=True
b=False

c=a and b
d=a or b
e=not a
f=not b
print(c,d,e,f)

print(1 and 0) #0
print(0 and 1) #0
print(1 or 0) #1
print(0 or 1) #1
print(not 1) #False
print(not 0) #True
print(0.1 and 0.5) #0.5
print(None and "None") #"None" , default values are falsy values, so it return second value
print()

#identity operators
print("identity operators")
a=10
b=10
c=20

d=a is b #True, because a and b are same objects in memory
e=a is not b #False, because a and b are same objects in memory
f=a is c #False, because a and c are different objects in memory
g=a is not c #True, because a and c are different objects in memory
print(d,e,f,g)


l1=[1,2,3]
l2=[1,2,3]
print(l1 is l2) #False, because l1 and l2 are different objects in memory
print(l1==l2) #True, because l1 and l2 have same values

#membership operators
print("membership operators")
# a=[1,2,3]
# b=[1,2,3]
# print(a in b)
# print(a not in b)

st="raghavendra"
d={47:"rajmouli",28:"yogesh",67:"yashaswini"}
print("raj" in st) 
print("432" not in st) 
print(28 in d) 
print(47 not in d) 
print("rajmouli" in d.values()) 
print("rajmouli" in d) 
print()

#bitwise operators
print("bitwise operators")
a=10 #0000 1010
b=4  #0000 0100
print(a&b) #0, 0000 0000 #bitwise AND operator
print(a|b) #14, 0000 1110 #bitwise OR operator
print(a^b) #12, 0000 1100 #bitwise XOR operator, 1 if both bits are different
print(~a) #-11 #1111 0101 #bitwise NOT operator, if the left most bit is 1 then it is negative number(most significant bit)
print(~b) #-5 #1111 1011 #bitwise NOT operator
print(a<<b) #160, 1010 0000 #left shift operator, adding zeros at the end, formula= num*(2**shift_value)
print(a>>b) #2, 0000 0010 #right shift operator, removing bits from the end, formula= num//(2**shift_value)
print()

