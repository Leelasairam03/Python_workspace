'''
Ditionary is a collection of key-value pairs. Each key is unique and maps to a specific value. 
Dictionaries are mutable, meaning you can change their content without changing their identity. 
They are defined using curly braces {} and consist of key-value pairs separated by colons.
it is a pre defined data type in python which is used to store multiple values in a single variable.
item->(key,value),therefore dictionary is a collection of items.
unordered collection of data, it is mutable, it is iterable, it is key based(not index based), it is dynamic in nature.
keys and values can be homogeneous and heterogeneous
only immutablw data types can be positioned as keys
'''

# Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)  
print(type(my_dict))

#empty dictionary
empty_dict = {}
empty_dict1 = dict() #using dict() 
print(empty_dict)
print(empty_dict1)

# Accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York

# Adding a new key-value pair
my_dict["country"] = "USA"
print(my_dict["country"])  # Output: USA
 
#key and  value can homogeneous and heterogeneous
d={1: "one", 2: "two", 3: "three"} #homogeneous
print(d)   

d1={"name": "Alice", 5: 30, "city": "New York"} #heterogeneous
print(d1)   

#if duplicate key is used then the last value will be considered,values can be duplicate but keys should be unique
d2={"name": "Alice", 5: 30, "city": "New York", 5: 40} #duplicate key
print(d2[5])  # Output: 40

#modifying values in a dictionary
print(my_dict["age"])  # Output: 30
my_dict["age"] = 31
print(my_dict["age"])  # Output: 31

'''methods of dictionary
1. clear() - Removes all items from the dictionary.
2. copy() - Returns a shallow copy of the dictionary.
3. fromkeys() - Creates a new dictionary with keys from an iterable and values set to a specified value.
4. get() - Returns the value for a specified key, or a default value if the key is not found.
5. items() - Returns a view object that displays a list of dictionary's key-value tuples.
6. keys() - Returns a view object that displays a list of all keys in the dictionary.
7. values() - Returns a view object that displays a list of all values in the dictionary.
8. setdefault() - Returns the value of a specified key. If the key does not exist, inserts the key with a specified value.
9. update() - Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs.
10. pop() - Removes the specified key and returns the corresponding value. Raises a KeyError if the key is not found.
11. popitem() - Removes and returns the last inserted key-value pair as a tuple. Raises a KeyError if the dictionary is empty.
'''
#clearing a dictionary
my_dict.clear() 
print(my_dict)  # Output: {}

#copying a dictionary
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {}

#creating a dictionary from keys
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0} 

#using get() method
value = new_dict.get('a')   #if key not present return None
print(value)  # Output: 0
print(new_dict.get('d'))  

#using items() method
items = new_dict.items()
print(items)  # Output: dict_items([('a', 0), ('b', 0), ('c', 0)]),list of tuples containing key-value pairs

#using keys() method
keys = new_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b', 'c'])

#using values() method
values = new_dict.values()
print(values)  # Output: dict_values([0, 0, 0]) 

#setdefault() method
default_value = new_dict.setdefault('d', 1) 
print(default_value)  # Output: 1
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0, 'd': 1}
print(new_dict.setdefault('a', 5))  # Output: 0 (existing value is returned, not changed)]

#updating a dictionary
new_dict.update({'a': 10, 'e': 2})
print(new_dict)  # Output: {'a': 10, 'b': 0, 'c': 0, 'd': 1, 'e': 2}
new_dict.update(f=3, g=4)  # Using keyword arguments
print(new_dict)  # Output: {'a': 10, 'b': 0, 'c': 0, 'd': 1, 'e': 2, 'f': 3, 'g': 4}

#adding dictionary to dictionary
dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4} #duplicate key 'y' in dict2 will update the value of 'y' in dict1
dict1.update(dict2) 
print(dict1)  # Output: {'x': 1, 'y': 3, 'z': 4} (the value of 'y' is updated to 3)

#pop() method
popped_value = new_dict.pop('e') # Removes the key 'e' and returns its value,if key is not found then it will raise KeyError
print(popped_value)  # Output: 2
print(new_dict)  # Output: {'a': 10, 'b': 0, 'c': 0, 'd': 1, 'f': 3, 'g': 4}

#popitem() method
popped_item = new_dict.popitem() # Removes and returns the last inserted key-value pair
print(popped_item)  # Output: ('g', 4)
print(new_dict)  # Output: {'a': 10, 'b': 0, 'c': 0, 'd': 1, 'f': 3} 

