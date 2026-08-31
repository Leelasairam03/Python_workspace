'''
nested collection-when one collection is present inside another collection eg list inside list,dict inside list etc
types:
1) nested list
       list of lists
2) nested dict
       dict of dicts
3) list of dictionary
       list containing dictionaries
json stands for java script object notation
it's basically a format to store and share structured data- especially between client and server in web apps,api's,etc.
'''
l=[['amy',23,94000],['ben',44,75000],['chad',12,80000]]
for i in l:
    print(i[0])

l=[['amy',23,94000],['ben',44,75000],['chad',12,80000]]
for i in l:
    print(i[-1])

l=[['amy',23,94000],['ben',44,75000],['chad',12,80000]]
for i in l[::-1]:
    print(i[0])

l=[['amy',23,94000],['ben',44,75000],['chad',12,80000]]
for i in range(2,-1,-1):
    print(l[i][0])
print("-------------------------")

l=[['amy',23,94000],['ben',44,75000],['chad',12,80000]]
l.reverse()
for i in l:
    print(i[0])
print("-----------")

l=[['amy',23,94000],['ben',44,75000],['chad',12,80000]]
for i in l:
       if i[2]>78000:
              print(i[0])
print("-----------")

for i in l:
       if i[2]>90000:
              i[0]=i[0].upper()
              print(i[0])
print(l)
print("---------------------------------")
#nested dict

company={
       'emp1':{'name':'amy','salary':94000,'dept':'HR'},
       'emp2':{'name':'ben','salary':75000,'dept':'research'},
       'emp3':{'name':'chad','salary':80000,'dept':'sales'}
       }
for i in company:
       print(i)
print("-----------------")

for i in company:
       print(company[i])
print("-----------------")

for i in company:
       print(company.get(i))
print("-----------------")

for i in company.values():
       print(i)
print("-----------------")

for i in company:
       print(company[i]['name'])
print("-----------------")

for i in company.values():
       print(i['name'])
print("-----------------")

for i in company:
       a=company.get(i)
       print(a['name'])
print("-----------------")

for i in company:
       print(company[i]['salary'])
print("-----------------")

for i in company:
       b=company[i]['salary']
       if b>78000:
              print(company[i]['name'])
print("-----------------")

for i in company.values():
       if i['dept'].lower()=='hr':
              print(i['name'])
print("-----------------")

for i in company.values():
       print(i.values())
print("-----------------")

for i in company.values():
       for j in i.values():
              print(j)
print("-----------------")

#list of dict

company=[
       {'name':'amy','salary':94000,'dept':'HR'},
       {'name':'ben','salary':75000,'dept':'research'},
       {'name':'chad','salary':80000,'dept':'sales'}
       ]
for i in company:
       print(i['name'])
print("-----------------")

for i in company:
       if i['salary']>78000:
              print(i['name'])
print("-----------------")

#dictionary of list
company={
       'names':['amy','ben','chad'],
       'salaries':[94000,75000,80000],
       'depts':['HR','research','sales'],
       'ids':[101,112,123]
}

for i in company:
       print(i)
print("-------------------")

for i in company:
       print(company[i])
print("-------------------")
#print amy,hr,9400,101
for i in company.values():
       print(i[0])
print("--------------------")
for i in company['names']:
       print(i)
print("--------------------")
'''
if salary is greater than 85000 print the name
'''
for i in range(0,3):
       if company['salaries'][i]>85000:
              print(company['names'][i])
              

