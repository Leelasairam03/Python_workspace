'''
function alias
- when a function is assigned to a variable,it is called as function alias
'''

#function alias
def wish(name):
    return "Hello",name

print(wish("sai"))

#function alias
f1=wish #now f1 is also a function pointing to the same function
print(f1("ram"))

#passing function as a argument/higher order function
def checkout(payment_type): #higher order function, payment_type acting as a function aliasing
    payment_type()

def upi():
    print("upi")
def card():
    print("card")

checkout(upi)  #function passes is called callback function
checkout(card)  #function passes is called callback function


def conduct_exam(subject):
    subject(90)

def java_exam(time):
    print(f"conducting java exam for {time} minutes")

def python_exam(time):
    print(f"conducting python exam for {time} minutes")


conduct_exam(python_exam)
conduct_exam(java_exam)