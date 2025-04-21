# Sets are an unordered collection of elements which means they cannot be accessed through indexing operator as no indexes exist in case of sets because each time when a set is executed ,its each element will be at a different place. Like apple is at position (index 0) in below example of set named fruits, but automatically it will be at some other position if we execute print again and again.
# Sets contain only unique elements (No Duplicate Values are Allowed in Sets)
#  Sets are mutable (changeable) which means that later in the program, value of a set can be changed through the use of set methods which are built-in like add(),update(),pop() etc.
fruits = {"apple","banana","cherry"}
numbers = {2, 3, 4, 5}
A = {1,2,3,4,5}
B = {4,5,6,7,8}
SetA = {1,2,3,4,5}
SetB = {4,5}
SetC = {4,5}
SetD = {6,7,8,9,10}
print(f"fruits Set Before any Method Applied: {fruits}")
                                                                                                            # Sets Methods
# .len() Method
print(f"Length of Set: {len(fruits)}")
# .add() Method
fruits.add("orange")
print(f"fruits After Add(): {fruits}")
# .update() Method
fruits.update(["mangoes","grapes"])
print(f"fruits After Update(): {fruits}")
# .remove() Method
fruits.remove("orange")
print(f"fruits After Remove(): {fruits}")
                                            # The remove() removes the specified element from the set and updates the set. It doesn't return any value.
                                            # If the element passed to remove() doesn't exist, KeyError exception is thrown.
                                            # You can use the set discard() method if you do not want this error.
                                            # The discard() method removes the specified element from the set.
                                            # However, if the element doesn't exist, the set remains unchanged; you will not get an error.
# .discard() Method
numbers.discard(3)  # removes 3 and returns the remaining set
print(numbers) # Output: numbers =  {2, 4, 5}
# .pop() Method
fruits.pop() # It will pop/remove an element that comes first in the set and that element can be any set element.
print(f"fruits After Pop(): {fruits}")
# .copy() Method
fruits_shallow_copy = fruits.copy()
print(f"Fruits Shallow Copy: {fruits_shallow_copy}")
# .clear() Method
fruits.clear()
print(f"fruits After Clear(): {fruits}")
# .union() Method
print(f"Union of Set A and Set B = {A.union(B)}")
                                                                     # Multiple Implementations of Intersection Method
# .intersection() Method
print(f"Intersection of Set A and Set B Using intersection() = {A.intersection(B)}")
print(f"Intersection of Set A and Set B  Using & Operator = {A & B}")
# .intersection_update() Method
print(f"Set A Before intersection_update() = {A}")
print(f"Set B Before intersection_update() = {B}")
A.intersection_update(B)
print(f"Set A after intersection_update() = {A}")
print(f"Set B after intersection_update() = {B}")
# Output:
# Set A Before intersection_update() = {1, 2, 3, 4, 5}
# Set B Before intersection_update() = {4, 5, 6, 7, 8}
# Set A after intersection_update() = {4, 5}
# Set B after intersection_update() = {4, 5, 6, 7, 8}
                                                                     # Implementations of Difference and Difference Update Methods
# .difference() Method
print(f"Difference of Set A and Set B Using difference() = {A.difference(B)}") # It means Elements of set1 which are not present in set2
print(f"Difference of Set B and Set A Using difference() = {B.difference(A)}") # It means Elements of set2 which are not present in set1
# .difference_update() Method
print(f"Set A Before difference_update() = {A}")
print(f"Set B Before difference_update() = {B}")
A.difference_update(B)
print(f"Set A after difference_update() = {A}")
print(f"Set B after difference_update() = {B}")
# OutPut:
# Set A Before difference_update() = {1, 2, 3, 4, 5}
# Set B Before difference_update() = {4, 5, 6, 7, 8}
# Set A after difference_update() = {1, 2, 3}
# Set B after difference_update() = {4, 5, 6, 7, 8}
                                        # Implementations of Symmetric Difference and Symmetric Difference Update Methods
# .symmetric_difference() Method => It means Elements of Set A and Set B, which are not common (It is exactly opposite of Intersection)
print(f"Symmetric Difference of Set A and Set B Using symmetric_difference() = {A.symmetric_difference(B)}")
# OutPut = {1, 2, 3, 6, 7, 8}
# .symmetric_difference_update() Method
A.symmetric_difference_update(B)
print(f"After Using Symmetric Difference Method A = { A }")
# OutPut: A = {1, 2, 3, 6, 7, 8}
                                                 # Checking If Sets are Superset, Subset, Disjoint Using Relevant Methods
# .issuperset() Method
print(f"Is SetA a Superset of SetB: {SetA.issuperset(SetB)}")
print(f"Is SetA a Superset of SetC: {SetA.issuperset(SetC)}")
print(f"Is SetC a Superset of SetA: {SetC.issuperset(SetA)}")
print(f"Is SetB a Superset of SetA: {SetB.issuperset(SetA)}")
print(f"Is SetB a Superset of SetC: {SetB.issuperset(SetC)}")
print(f"Is SetC a Superset of SetB: {SetC.issuperset(SetB)}")
# .issubset() Method
print(f"Is SetB a Subset of SetA: {SetB.issubset(SetA)}")
print(f"Is SetC a Subset of SetA: {SetA.issubset(SetA)}")
print(f"Is SetB a Subset of SetC: {SetB.issubset(SetC)}")
print(f"Is SetC a Subset of SetB: {SetC.issubset(SetB)}")
# .isdisjoint() Method
print("Disjoint Sets Checking: ")
print(f"A and B are Disjoint Sets: {SetA.isdisjoint(SetB)}")
print(f"A and C are Disjoint Sets: {SetA.isdisjoint(SetC)}")
print(f"A and D are Disjoint Sets: {SetA.isdisjoint(SetD)}")

# print(help(set))
# print(dir(set))