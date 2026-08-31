'''
a function is a named reusable block of code that performs a specific task
types:
1.built in/pre defined functions (print(),len(),input(),id(),type(),min(),max(),sum(),sorted(),range(),etc)
2.user defined functions
     - these are functions that are created by the programmer to perform user specific tasks/functionalities
     - they help in modularity,reusability,and code organization
     - syntax:
             def function_name(parameters):
                 """
                 docstring - describes the function's purpose and usage
                 """
                 function body
                 return expression
     - parameters are optional
     - function name should start with a letter or underscore
     - function body is indented
     - return statement is optional
def keyword:used to define a function,followed by function name and parentheses
function name:follows same rules as variables
parameters:optional,comma separated values in parentheses
docstring:optional,triple quoted string describing function
'''
'''
working of a function-
     - when python encounters a def keyword,it creates a function object in memory
     - the function's code is stored inside that object
     - the function name becomes a reference pointing to that function object,
     - printing the function name(without parenthesis)displays its memory reference

Execution of function
     - when you call the function using parentheses, control is transferred to the function's code
     - a new stack frame is created to hold its local variables(a,b,etc.)
     -after executing the code(or hitting 'return'),
          -control goes back to the calling point
          -local variables are destroyed
          -but the function object itself remains in memory and can be called again
'''
'''
4 ways of defining a function:
     1. function without parameter and without return
     2. function without parameter and with return
     3. function with parameter and without return
     4. function with parameter and with return
'''
import random 
def send_otp():
     print("otp sent successfully")
     return random.randint(100,999)

def order_food(name,dish,price):
     print(f"{name} has ordered {dish} which costs {price}Rs.")

def book_ticket(name,flight):
     print(f"{name} has booked a ticket for {flight} flight ")

def add(a,b):
     return a+b
def substraction(a,b):
     return a-b
def multiplication(a,b):
     return a*b
def division(a,b):
     return a/b

print(send_otp())
print("------------------------")
order_food("sairam","pizza",499)
print("------------------------")
book_ticket("sairam","indigo")
print("------------------------")
print(add(10,20))
print(substraction(10,20))
print(multiplication(10,20))
print(division(10,20))
print("------------------------")
