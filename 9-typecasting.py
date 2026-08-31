#typecasting- converting one data type to another
#used for mathematical operation,comparison,storing in correct data type,user input,function arguments
#types- implicit,explicit
#implicit- no type casting performed by user,automatically performed by python,from smaller data type to larger data type
#explicit- type casting performed by user,from larger data type to smaller data type

#implicit example
x = 10       # integer
y = 5.5      # float
z = x + y    # integer + float = float (implicit typecasting)

print("Implicit Typecasting:")
print("x is of type:", type(x))
print("y is of type:", type(y))
print("z =", z, "| z is of type:", type(z))
print()

#converting boolean to int,#boolean<int<float<complex
b=True
print(b)
print(type(b))
print(int(b))
print(type(int(b)))

#explicit example

a = "100"    # string
print("Explicit Typecasting:")
print("a is of type:", type(a))

# converting string to integer
b = int(a)
print("b =", b, "| b is of type:", type(b))

# converting integer to float
c = float(b)
print("c =", c, "| c is of type:", type(c))

# converting float to string
d = str(c)
print("d =", d, "| d is of type:", type(d))

#convert float to int
a=10.56565
print(int(a))
print(type(a))
print(type(int(a)))

#single values data types support both higher to lower and lower to higher conversions in explicit typecasting
c=10
d=float(c)
e=complex(c)
f=bool(c)
g=str(c)
print("int to float: ",d)
print("int to complex: ",e)
print("int to bool: ",f)
print("int to str: ",g)

h=10.78
print(int(h))

i=10+3j
print(bool(i))

#complex to int and float is not possible because it has two components.
#bigger type conversion into smaller is possible only by explicit type conversion,but data loss occurs.

'''
type casting with multivalued data types
- list, tuple, set
- string can be converted to list, tuple, set
- we can interchange list, tuple, set
-can only be done through explicit type casting
'''

print("\n--- Typecasting with Multivalued Data Types ---")
#explicit type casting among collections
# String to List, Tuple, Set,dict
string_val = "hello"
print(f"Original string: {string_val}")
print("String to List:", list(string_val))
print("String to Tuple:", tuple(string_val))
print("String to Set (unordered, no duplicates):", set(string_val))
#string cannot be converted into dictionary because it does not have key
print()

# List to Tuple, Set,string 
list_val = [10, 20, 20, 30]
print(f"Original list: {list_val}")
print("List to Tuple:", tuple(list_val))
print("List to Set (removes duplicates):", set(list_val))
print("List to String:", str(list_val))
#list cannot be converted into dictionary
print()

# Tuple to List, Set,string,dict    
tuple_val = (1, 2, 3, 3)
print(f"Original tuple: {tuple_val}")
print("Tuple to List:", list(tuple_val))
print("Tuple to Set:", set(tuple_val))
print("Tuple to String:", str(tuple_val))
print()

# Set to List, Tuple,string,dict
set_val = {100, 200, 300}
print(f"Original set: {set_val}")
print("Set to List:", list(set_val))
print("Set to Tuple:", tuple(set_val))
print("Set to String:", str(set_val))
#set to dictionary is not possible without modifying original set because it does not have key.
print()

# dictionary to list, tuple, set,string

dict_val = {"a": 1, "b": 2, "c": 3}
print(f"Original dictionary: {dict_val}")
print("Dictionary to List:", list(dict_val))  #list of keys
print("Dictionary to Tuple:", tuple(dict_val))  #tuple of keys
print("Dictionary to Set:", set(dict_val))  #set of keys
print("Dictionary to String:", str(dict_val))

#try converting single valued data types into multivalued data types
#int
num=10
# print(list(num)) #TypeError: 'int' object is not iterable
# print(tuple(num)) #TypeError: 'int' object is not iterable
# print(set(num)) #TypeError: 'int' object is not iterable
print(str(num)) #single valued data types can be converted to string

#bool
b=True
# print(list(b)) #TypeError: 'bool' object is not iterable
# print(tuple(b)) #TypeError: 'bool' object is not iterable
# print(set(b)) #TypeError: 'bool' object is not iterable
print(str(b)) #single valued data types can be converted to string

#float
f=10.565656
# print(list(f)) #TypeError: 'float' object is not iterable
# print(tuple(f)) #TypeError: 'float' object is not iterable
# print(set(f)) #TypeError: 'float' object is not iterable
print(str(f)) #single valued data types can be converted to string

#complex
c=10+3j
# print(list(c)) #TypeError: 'complex' object is not iterable
# print(tuple(c)) #TypeError: 'complex' object is not iterable
# print(set(c)) #TypeError: 'complex' object is not iterable
print(str(c)) #single valued data types can be converted to string

#try converting multivalued data types into single valued data types

#list
list_val = [10, 20, 20, 30]
# print(int(list_val)) #ValueError: invalid literal for int() with base 10: '[10, 20, 20, 30]'
# print(float(list_val)) #ValueError: invalid literal for float(): '[10, 20, 20, 30]'
# print(complex(list_val)) #ValueError: invalid literal for complex(): '[10, 20, 20, 30]'
print(bool(list_val)) #ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

#tuple
tuple_val = (1, 2, 3, 3)
# print(int(tuple_val)) #ValueError: invalid literal for int() with base 10: '(1, 2, 3, 3)'
# print(float(tuple_val)) #ValueError: invalid literal for float(): '(1, 2, 3, 3)'
# print(complex(tuple_val)) #ValueError: invalid literal for complex(): '(1, 2, 3, 3)'
print(bool(tuple_val)) #ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

#set
set_val = {100, 200, 300}
# print(int(set_val)) #ValueError: invalid literal for int() with base 10: '{100, 200, 300}'
# print(float(set_val)) #ValueError: invalid literal for float(): '{100, 200, 300}'
# print(complex(set_val)) #ValueError: invalid literal for complex(): '{100, 200, 300}'
print(bool(set_val)) #ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

#dictionary
dict_val = {"a": 1, "b": 2, "c": 3}
# print(int(dict_val)) #ValueError: invalid literal for int() with base 10: '{'a': 1, 'b': 2, 'c': 3}'
# print(float(dict_val)) #ValueError: invalid literal for float(): '{'a': 1, 'b': 2, 'c': 3}'
# print(complex(dict_val)) #ValueError: invalid literal for complex(): '{'a': 1, 'b': 2, 'c': 3}'
print(bool(dict_val)) 

#string,can be done only with integer in a string, 
#parsing- converting string into it's corresponding single valued data type explicitly
s="10"
a=int(s)
b=float(s)
c=complex(s)
d=bool(s)
print(a)
print(b)
print(c)
print(d)

s="10.0"
a=float(s)
b=complex(s)
print(a)
print(b)
print(type(a))

s="10+5j"
a=complex(s)
print(a)
print(type(a))

#boolean on default values gives false
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(""))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(False))


'''
character convertion- it means changing a character into it's numeric value and vice versa
#python internally represents every character by unicode code point(unique number assigned to every character)
#character conversion is a form of single valued type casting
2 important functions w.r.t character convertions
    - ord('charater') #returns the unicode code point of the character
    - chr(number)     #returns the character corresponding to the unicode code point
'''

print(ord('A')) #returns the unicode code point of the character 'A'
print(ord('B')) #returns the unicode code point of the character 'B'
print(ord('C')) #returns the unicode code point of the character 'C'
print(chr(65)) #returns the character corresponding to the unicode code point 65
print(chr(66)) #returns the character corresponding to the unicode code point 66
print(chr(10084)) #returns the character corresponding to the unicode code point ❤


