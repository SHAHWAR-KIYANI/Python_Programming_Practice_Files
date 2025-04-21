# (1) Length Method => len(variable_name)
# Description: Length of the String Variable is found using length function

name1 = input ("Enter the Name For Length Checking: ")
length = len(name1)
print(f"Your Name Length is: {length} (Including the Whitespaces)")
print()

# (2) Reversed Method => reversed ()
# Description: It returns an iterator object that provides access to the elements of an iterable (list, tuple, string, etc.) in reverse order.

# It will convert the iterator (reversed iterator object) to  an iterable (list here) and will print it.
# It cannot be directly printed in an iterator object format.
string = 'Python'
result = reversed(string)
print(list(result))

# Iterator objects can be easily converted into sequences such as lists and tuples. They can also be directly iterated over using a loop.
full_name = 'Shahwar Kiyani'
for name_char in reversed(full_name):
    print(name_char)
print()

 # In case of dictionary, it will reverse the keys
country_capitals = {
  'England': 'London',
  'Canada': 'Ottawa',
  'Germany': 'Berlin'
}
country = tuple(reversed(country_capitals))
print(country)
print()

# (3) Type Method => type ()

# (4) IsInstance Method => isinstance ()

# (5) Min Method => min ()

# (6) Max Method => max ()

# (7) Sum Method => sum ()

# (8) Power Method => pow ()

# (9) Absolute Method => abs ()

