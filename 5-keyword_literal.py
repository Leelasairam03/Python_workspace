#list of keywords in python
''' 
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, 
if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield 
'''
#keywords are the reserved words in python which have special meaning and cannot be used as identifiers.
#keywords are also indentifiers but not all identifiers are keywords.

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist)) #total number of keywords in python

#types of keywords in python
'''
1. asynchronous keywords- async, await
2. conditional keywords- if, else, elif,break, continue,pass,for, while
3. literal keywords- True, False, None
4. logical keywords- and, or, not, is, in
6. functional keywords- def, lambda, return, yield
7. import keywords- import, from, as
8. object oriented keywords- class, nonlocal, global, del
9. resource management keywords- with
10. exception handling keywords- try, except, finally, raise,assert,raise
'''
#types of literals in python
'''
#literals are the direct values assigned to a variable or constant in python.
1) boolean literals- True, False
2) nonetype literal- None
'''
'''
#conventions are rules or guidelines which are followed to write a program in python.(conventions are identifiers)
1. variables,modules,functions should,filenames be in lowercase letters and if the name is made up of multiple words then the words should be separated by underscore(_).
2. constants should be in uppercase letters and if the name is made up of multiple words then the words should be separated by underscore(_).
3. snake case convention- the words are separated by underscore(_). example- my_variable
4. camel case convention- the first word is in lowercase and the first letter of each subsequent word is capitalized. example- myVariable.
5. pascal case convention- the first letter of each word is capitalized. example- MyVariable.
'''