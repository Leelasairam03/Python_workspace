'''
generator is function that is used to create a custom sequence of elements using the "yield" keyword.
-if a user-defined function contains atleast one yield keyword,then that function becomes a generator function.
-generators generate values one-by-one(not all at once)
-generators are 'mainly used to create custom sequences'(like even numbers,oddnumbers,fibonacci,primes etc.)
-generator object is created only once,when the "function containing yeild keyword" is called.
-each yield returns one value,when next() or loop asks for it.


yield- when python executes yield:
       - it returns yielded value to the caller
       - it pauses the function(remembers variables and the next line)
       - when you call next() again,it "resumes right after yield".
       - automatically creates an iterator
'''


def mygenerator():
    print("first")
    yield 10
    print("second")
    yield 20
    print("third")
    yield 30
    print("fourth")


gen_obj=mygenerator()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))

print("---------------")
gen_obj=mygenerator()
for i in gen_obj:
    print(i)

print("-----------------")

def fun():
    value=0
    yield value
    value+=1
    yield value
    value=value+2
    yield value**2
    value=value+3
    yield value**3
    value=value-2
    yield value**2

gen_obj=fun()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))

print("-------------")
gen_obj=fun()
for i in gen_obj:
    print(i)
print("-------------")



#generator function for fibonacii

def fibo_generate(n):
    a=0
    b=1
    count=0
    while(count<n):
        yield a
        a=b
        b=a+b
        count+=1


for i in fibo_generate(10):
    print(i)
