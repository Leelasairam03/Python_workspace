# Strings in Python
'''
1. Strings are sequences of characters enclosed in single quotes (' ') or double quotes (" ") or triple quotes (''' ''').
2. Strings are immutable, meaning that once they are created, their content cannot be changed.
3. Strings can be concatenated using the + operator and repeated using the * operator.
4. characters include uppercase,lowercase,digits,spaces,special characters
5. index based collection
'''
s='''Sai ram'''
print(s)

s1=str()
print(s1)
print(type(s1))

print(s[2])
print(s[-2])
'''
String Slicing- it is the process of extracting a part or subquence from a sequence type in python.
slicing works only on index based,ordered sequences.(lists,tuples,strings)
it uses a special slice operator : inside the []
syntax: sequence[start:stop:step]
    start: starting index(inclusive), default=0, it can be negative
    stop: ending index(exclusive), default=len(sequence), it can be negative
    step: step size(increment/decrement), default=1, it can be negative
'''
print("\n--- Slicing ---")
text = "Hello, Python!"
print(f"Original: {text}")
print(f"text[0:5]: {text[0:5]}")    # From index 0 to 4
print(f"text[7:]: {text[7:]}")      # From index 7 to end
print(f"text[:5]: {text[:5]}")      # From start to index 4
print(f"text[::-1]: {text[::-1]}")  # Reverse the string

# String Operations
print("\n--- Operations ---")
s1 = "Hello"
s2 = "World"
print(f"Concatenation (+): {s1 + ' ' + s2}")
print(f"Repetition (*): {s1 * 3}")
print(f"Membership (in): {'o' in s1}")
print(f"Membership (not in): {'x' not in s1}")

# String Methods
print("\n--- String Methods ---")
msg = "  learning Python is fun!  "
print(f"Original: '{msg}'")
print(f"len(): {len(msg)}")                   # Length of the string
print(f"upper(): {msg.upper()}")              # Convert to uppercase
print(f"lower(): {msg.lower()}")              # Convert to lowercase
print(f"title(): {msg.title()}")              # Capitalize first letter of each word
print(f"capitalize(): {msg.capitalize()}")    # Capitalize first letter of the string
print(f"strip(): '{msg.strip()}'")            # Remove leading and trailing whitespaces
print(f"lstrip(): '{msg.lstrip()}'")          # Remove leading whitespaces
print(f"rstrip(): '{msg.rstrip()}'")          # Remove trailing whitespaces
print(f"replace(): {msg.replace('fun', 'awesome')}") # Replace substring

# Searching and Counting
print("\n--- Searching and Counting ---")
data = "apple, banana, apple, orange"
print(f"Original: '{data}'")
print(f"count('apple'): {data.count('apple')}") # Count occurrences
print(f"find('banana'): {data.find('banana')}") # Find index (returns -1 if not found)
print(f"index('banana'): {data.index('banana')}")# Find index (raises error if not found)
print(f"startswith('apple'): {data.startswith('apple')}")
print(f"endswith('orange'): {data.endswith('orange')}")

# Splitting and Joining
print("\n--- Splitting and Joining ---")
words_list = data.split(', ')                 # Split string into a list
print(f"split(', '): {words_list}")
joined_string = " - ".join(words_list)        # Join list elements into a string
print(f"join(' - '): {joined_string}")

# String Formatting
print("\n--- String Formatting ---")
name = "Alice"
age = 25
print(f"f-string: My name is {name} and I am {age} years old.") # f-string (Python 3.6+)
print("format(): My name is {} and I am {} years old.".format(name, age))

# Boolean Methods
print("\n--- Boolean Methods ---")
word1 = "Python3"
word2 = "12345"
print(f"isalnum() for '{word1}': {word1.isalnum()}") # True if alphanumeric
print(f"isalpha() for '{word1}': {word1.isalpha()}") # True if all alphabets
print(f"isdigit() for '{word2}': {word2.isdigit()}") # True if all digits
print(f"isupper() for 'HELLO': {'HELLO'.isupper()}") # True if uppercase
print(f"islower() for 'hello': {'hello'.islower()}") # True if lowercase


