fruits = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(f"Tuple Named Fruits: {fruits}")
                                                                                        # Tuple Methods ( Only Two Methods: .index() and .count() )
# 1) len() Method
print(f"Length of Tuple: {len(fruits)}")
# 2) .count() Method
print(f"Count of 'apple': {fruits.count('apple')}")
# 3) .index() Method
print(f"Index of 'apple' is: {fruits.index('apple')}")
print(f"Index of 'cherry' is: {fruits.index('pineapple')}") # ValueError will be thrown which means value(x) => "pineapple" is not in tuple
