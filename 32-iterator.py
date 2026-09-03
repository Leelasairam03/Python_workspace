'''
iterator is an object that can iterate through all the elements of collection one by one
-without needing to know the structure of the collection
-it is unidirectional(iterates from left to right, cannot go back)
-it supports partial iteration(can stop iteration anytime)

it has two methods
    __iter__() -> takes an iterable(list,tuple,set,dict) and returns an iterator object
                  the iterator object keeps a cursor(internal pointer) that moves to next element everytime next() is called
    __next__() -> returns the next item
'''

