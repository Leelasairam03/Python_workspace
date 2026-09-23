'''this is the docstring of the module which gives details of the module''' 
print(__file__)
print(__package__)
print(__cached__)

print(__doc__) #only line 1 docstring will be printed, or it returns none if no doc string is there on line1

def play():
    '''this function plays bold like RCB'''

print(play.__doc__) #docstring of function 'play' will be printed

