'''
comprehension:
            - they are python's way of writing loops that produce collections in a comapct,readable form.
            - it combines=>iteration + transformation + filtering
3 types-
    1. list comprehension - easier way to create lists(transformation + filtering)
    2. set comprehension - same as list but use {} instead of [],unordered
    3. dict comprehension 
'''
#list comprehension- syntax- l=[expression for variable in sequence]  #iteration + transformation + appending
ol=[2,3,4,5,6]
nl=[i+10 for i in ol]
print(nl)

cube=[i**3 for i in ol]
print(cube)

ol=["amy","ben","chad","divya","evan"]
print([len(i) for i in ol])

#list comprehension - l=[expression for variable in sequence if condition] #iteration + filtering + transformation + appending
ol=[4,7,10,13,18]
print([i**2 for i in ol if i%2==1])

ol=["amy","ben","chad","divya","evan"]
print([i for i in ol if len(i)>3])

ol=["ms amy","mr ben","mr chad","ms divya","ms evan"]
print([i for i in ol if i[0:2]=='ms'])
print([i for i in ol if 'ms' in i])
print([i for i in ol if i.startswith('ms')])

#if else
#list comprehension - l=[true_exp if condition else false_exp for variable in sequence] #iteration + filtering + transformation + appending
ol=[2,3,4,5,6,7]
print([i**2 if i%2==0 else i**3 for i in ol])

ol=["ms amy","mr ben","mr chad","ms divya","mr evan"]
print(['beautiful '+i if 'ms' in i else 'handsome '+i for i in ol])

print([i.replace('ms','beautiful') if 'ms' in i else i.replace('mr','handsome') for i in ol])

print("----------------------------------------------------")


#dictionary comprehension - syntax - d={key_exp:value_exp for item in iterable} #iteration + transformation + appending
l=[5,7,8,10,11]
d={i:i**2 for i in l}
print(d)

print({i**2:i**3 for i in l})

candidates=["amy","bennet","chadwick","divya","evanjovelin"]
print({i:len(i) for i in candidates})

print({i:i[::-1] for i in candidates})

#dictionary comprehension - syntax - d={key_exp:value_exp for item in iterable if condition} #iteration + filtering + transformation + appending
print({i**2:i**3 for i in l if i%2==1})


ol=["ms amy","mr ben","mr chad","ms divya","mr evan"]
print({i:"handsome" for i in ol if 'mr' in i})

#if-else
#dictionary comprehension - syntax - d={key_exp:(true_val exp if condition else false_val_exp) for item in iterable } #iteration + filtering + transformation + appending

l=[4,5,6,7,8,9]
d={i:(i**2 if i%2==0 else i**3 ) for i in l}
print(d)

#dictionary to dictionary
od={2:10,3:20,4:30,5:40,6:50}
nd={k:(v**2 if k%2==0 else v**3) for k,v in od.items()}
print(nd)

