# Dictionary is an Ordered Collection of Pairs {key:value}.
# It is Mutable (Changeable).
# No Duplicates are allowed in the Dictionary.

capitals = {
    "India": "New Delhi",
    "US": "Washington DC",
    "UK": "London",
    "Australia": "Canberra",
    "China": "Beijing",
    "Pakistan": "Islamabad"}

for capital in capitals:
    print(f"{capital} : {capitals[capital]}")
print()
                                                                                                 # Dictionary Methods
# 1) .get() Method
# It will get the value for the key passed.
scores = {
    'Physics': 67,
    'Maths': 87,
    'History': 75
}
result = scores.get('Physics')
print(result)
# If no such key exist or if key is not found then there are two scenarios:
# Scenario 1: It will return None if no default value is provided inside the get function along with the key like get(key).
person = {'name': 'Phill', 'age': 22}
print('Value of Name: ', person.get('name'))
print('Value of Age: ', person.get('age'))
print('Value of Salary: ', person.get('salary')) # This key does not exist and has no default value given so it will follow Scenario 1.
# Scenario 2: It will return a Default Value if default value is provided inside the get function along with the key like get(key,default_value).
print('Salary: ', person.get('salary', 0.0)) # Here default value is given along with the key so it will follow scenario 2.
# Special Case: Accessing dictionary value for salary using [ ] will raise KeyError Exception.
print(person['salary'])

# 2) .update() Method => It will push/update key:value pair at the end of the dictionary and behaves like the push operation.
capitals.update({'Japan':'Tokyo'})
print(f"Dictionary Named Capitals After Update: \n {capitals}")
print()
# 3) .pop() Method => It will remove the key:value pair whose key is passed.
capitals.pop("Japan")
print(f"Dictionary Named Capitals After Popping Japan: {capitals}")
print()
# 4) .popitem() Method => It will remove the key:value which is at the end of the dictionary (the last added pair).
capitals.popitem()
print(f"Dictionary Named Capitals After Popping Item: {capitals}")
print()
# 5) .keys() Method => It will get all the keys of the dictionary in the form of a dictionary object with list collection containing  keys.
capitals_keys = capitals.keys()
print(f"Just Keys: {capitals_keys}")
print("Keys are: ", end=" ")
for keys in capitals_keys:
    print(keys, end=" ,")
print()
print()
# 6) .values() Method => It will get all the values of the dictionary in the form of a dictionary object with list collection containing dictionary values.
capitals_values = capitals.values()
print(f"Just Values: {capitals_values}")
print("Values are: ", end=" ,")
for values in capitals_values:
    print(values, end=" ")
print()
print()
# 7) .items() Method => It will return a dictionary object with a 2D Sequence i.e. list[tuples]. Tuples values will be keys and values separated by comma.
items = capitals.items()
print(f"Dictionary Items: {items}")
print()
for Keys, Values in items:
    print(f"{Keys}: {Values}")
print()

# 8) .clear() Method => It will remove all the key:value pair from the dictionary.
capitals.clear()
print(f"Dictionary Named Capitals After Clearing: {capitals}")
print()

# 9) .copy() Method

# It returns a copy (shallow copy) of the dictionary. It doesn't modify the original dictionary.
# When the copy() method is used, a new dictionary is created which is filled with a copy of the references from the original dictionary.
# When the = operator is used, a new reference to the original dictionary is created.
# In simple words, copy() generates a shallow copy whereas, assignment operator behaves like deep copy where in it keeps reference to the original dictionary.

# Example 1: Shallow Copy using .copy() Method
original_marks = {'Physics':67, 'Maths':87}
copied_marks = original_marks.copy()
print('Original Marks:', original_marks)
print('Copied Marks:', copied_marks)

# Example 2: Deep Copy using assignment operator
original = {1:'one', 2:'two'}
new = original
new.clear()
print('new: ', new)
print('original: ', original)
# OutPut:
# new:  {}
# original:  {}

# 10) .setdefault() Method
# It works exactly like get() method but with one exception and i.e. it will also push that key at the end of the dictionary whose value will be either None or a default value of provided along with the key.
# Whatsoever is passed to setdefault(), it will become a part of the dictionary eventually, with key having some value or None as a value.
person = {'name': 'Phill'}
# Scenario 1: Key is not in the dictionary with no default value.
salary = person.setdefault('salary')
print('person = ',person)
print('salary = ',salary)
# Scenario 2: Key is not in the dictionary with default value provided.
# age = person.setdefault("age", 22)
# print('person = ',person)
# print('age = ',age)

# 11) .fromkeys() Method =>
# It creates a dictionary from the given sequence of keys and values.
# The same value is assigned to all the keys of the dictionary because all the keys are pointing to the same memory address of the value.
# If the value of the dictionary is not provided, None is assigned to the keys.

# Example 1: When optional value is provided
alphabets = {'a', 'b', 'c'}
number = 1
dictionary = dict.fromkeys(alphabets, number)
print(dictionary)

# Example 2: When optional value is not provided
keys = [1, 2, 4 ]
numbers = dict.fromkeys(keys)
print(numbers)

# Example 3: To Create A Dictionary From Mutable Object. Here values are mutable object i.e. list which can be appended.
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]
vowels = dict.fromkeys(keys, value)
print(vowels)
value.append(2)
print(vowels)

# print(dir(capitals))
# print(help(capitals))
