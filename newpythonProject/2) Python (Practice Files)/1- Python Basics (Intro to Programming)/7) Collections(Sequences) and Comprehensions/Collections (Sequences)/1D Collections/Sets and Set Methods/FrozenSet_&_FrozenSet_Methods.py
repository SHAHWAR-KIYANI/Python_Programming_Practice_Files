# Frozen Set is just an immutable version of a Python Set Object.
# While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
# But like sets, it is not ordered (the elements can be set at any index).
# We cannot have any duplicate values in the frozen set.
# Frozen Set takes a single parameter (optional) which is an iterable (list/dictionary/set/tuple)
# The frozenset() function returns an immutable frozenset initialized with elements from the given iterable.
# If no parameters are passed, it returns an empty frozenset.
fs1 = frozenset([1,2])
print("Simple Frozen Set Created from a List: ",fs1)
fs: frozenset = frozenset()
print("Empty Frozen Set Looks Like This: ",fs)
# Example 1 (frozenset() for Dictionary)
# When you use a dictionary as an iterable for a frozen set, it only takes keys of the dictionary to create the set.
person = {"name": "John", "age": 23, "sex": "male"}
d = frozenset(person)
print(f"Frozen Set For Dictionary: {d}")
# Example 2 (frozenset for List)
animals = frozenset(["cat", "dog", "lion"])
print(f"Frozen Set For List: {animals}")
# Example 3 (frozenset() for Set)
s = frozenset({1,2,3,4,5,6,7,8,9,10})
print(f"Frozen Set For Set: {s}")
# Example 4 (frozenset() for Tuple)
t = frozenset((1,2,3,4,5))
print(f"Frozen Set For Tuple: {t}")
                                                                                                  # FrozenSet Methods
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])
# 1) .copy()
D = A.copy()
# 2) .union()
print("Union = ",A.union(B))
# 3) .intersection()
print("Intersection = ",A.intersection(B))
# 4) .difference()
print("Difference = ",A.difference(B))
# 5) .symmetric_difference()
print("Symmetric Difference = ",A.symmetric_difference(B))
# 6) .isdisjoint()
print("Is Disjoint: ",A.isdisjoint(C))
# 7) .issuperset()
print("Is Superset: ",C.issubset(B))
# 8) .issubset()
print("Is Subset: ",B.issuperset(C))
                                                                    # Exceptions while using the frozenset() method in Python
# If by mistake we want to change the frozen set object, then it throws a TypeError
# creating a list
favourite_subject = ["OS", "DBMS", "Algo"]
f_subject = frozenset(favourite_subject)
# f_subject[1] = "Networking"  # This will raise a TypeError because frozensets are immutable

# print(type(fs))
# print(dir(fs))
# print(help(fs))