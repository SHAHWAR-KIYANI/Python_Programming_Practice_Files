# Lists are an ordered collection of elements which means they can be accessed through numerical indexes (Like if some value is stored at an index 0 then it will not change its position through-out the Lifecycle of list and whenever the print() will be executed then it will always be at that same index unless if value is changed at that index through indexing operator )
# Lists are mutable (changeable) which means that later in the program, value of a list at some individual index can be changed through indexing operator like list[0] = "Something" etc.
# Duplicate Values are Allowed in Lists  because like sets there is no requirement defined for unique presence of elements.

fruits = ["Apple","Orange","Banana","Coconut"]
# Implementation 1:
for fruit in fruits:
    print(fruit, end=" ")
print()

# Implementation 2:
for fruit in fruits[0:4]:
    print(f"Fruit Name: {fruit}")

# Implementation 3: We want to access value of list at index 3 which is Coconut
for fruit in fruits[3]:
    print(f"Fruit Name: {fruit}")

# Implementation 4: e want to access value of list at index 4, but it will throw an index error which is  (List Index out of Range)
for fruit in fruits[4]:
    print(f"Fruit Name: {fruit}")

# Example 1
fruits.sort()
print(f"Sorted Fruits List: {fruits}")
fruits.reverse()
print(f"Reversed Fruits List: {fruits}")
# print(dir(fruits))