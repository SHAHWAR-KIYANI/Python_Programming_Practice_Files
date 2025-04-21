# 12) Scope of Variables: Local Scope vs Global Scope
# The scope of variable in python is an environment where it can be recognizable.
# For example, the scope of parameter is always inside the function.
# The variable existing outside the function has a global scope. Means, it can be accessed inside the function.

# Example 1:
def greetings(name):
    print(name)
greetings("Rehan")
# Explanation:  In above example, the scope of parameter name is only inside the function. If we try to use it outside the function, it will generate error.

# Example 2:
def greetings(name):
    print(name)
greetings("Rehan")
# print(name) # NameError: name 'name' is not defined
# Explanation: The variable existing outside the function has a global scope. Means, this variable named (name) can only be accessed inside the function.

# Example 3: (What if variable existing outside the function has the same name as the parameter of the function?)
# Answer:
# If the name of the variable is same, the python is intelligent enough to differentiate it.
# It will print the value provided as argument (parameter value) inside the function,
# and outside the function, it will print the value of the variable existing outside the function.
name : str = "Musa"
def greetings():
    name: str = "Rehan"
    print(f"Name Inside Function: {name}")
greetings()
print(f"Name Outside Function:{name}")

# Example 4: Global Keyword
# We can declare a variable outside the function and access it inside the function with global keyword.
teacher_name : str = "Usman"
def greetings():
    global teacher_name
    teacher_name = "Rehan"
    print(f"Inside Function: {teacher_name}")
greetings()
print(f"Outside the Function: {teacher_name}")

                                                                                        # Pass by Value and Pass by Reference
# Scenario 1: Pass by Value
# For Immutable Objects: Value passed is actually Pass by Value i.e. Shallow Copy.
# Thus, here, shallow copy exists and therefore, changes will not be reflected outside the function because of existence of duplicate/shallow copy.
def any_function (value):
    print(f"value Received: {value}")
    value += 100
    print(f"value changed inside func : {value}")
value = 4
any_function(value)
print(f"Value outside the func: {value}")
# Conclusion Scenario 1: When a scalar is passed to a function, Python creates a copy of the value (since they are immutable).
# Any modifications inside the function will be applied to the local copy, and the original variable outside the function remains unchanged.

# Scenario 2: Pass by Reference
# For Mutable Objects: Value passed is actually Pass by Reference i.e. Deep Copy.
# Thus, here, deep copy exists and therefore, changes will be reflected outside the function too.
def any_function (num_list):
    print(f"value Received: {num_list}")
    num_list.append(500)
    print(f"num_list changed inside func : {num_list}")
num_list = [1, 2, 4, 5]
any_function(num_list)
print(f"num_list outside the func: {num_list}")
# Conclusion Scenario 2: In contrast, if the function were modifying a mutable object like a list or dictionary, the changes would be reflected outside the function.
# This is because, mutable objects are passed by reference, and their internal state can be altered without creating a new copy.