# Return keyword controls the execution of the function etc., returns some value or returns None.
# Example 1 (Value Returning Function)
def addition (num1: int, num2: int ) -> int:
    return num1 + num2
result: int = addition(2,3)
print(result)

# Example 2 (Scenario 1: Non-Value Returning Function)
def find_square(num):
    square = num * num
    print('Square:', square)
find_square(3)

# Example 2 (Scenario 2: No Value Returning Function => If we check the returned value, it will be None)
def find_squ(num):
    square = num * num
    print('Square:', square)
# result = find_squ(3) # Remove this line Code Comment Before Execution to see the Output
print(result)

# Example 3 (Multiple Positional Arguments Scenario 1)
def add (*args ):
    sum1 = 0
    for num in args:
        sum1 += num
    return sum1
result = add(1,2,3,4,5)
print(result)

# Example 4 (Multiple Positional Arguments Scenario 2)
list_numbers = [1,2,3,4,5,6]
def sum (*args ):
    sum2 = 0
    for num in args:
        sum2 += num
    return sum2
result = sum(*list_numbers) # List Unpacking
print(result)

# Example 5 (Multiple Keyword Arguments)
def intro(**kwargs):
    print("\nData type of argument:",type(kwargs))
    for key, value in kwargs.items():
        print("{} is {}".format(key,value))
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


# ---------- Pass by Value & Pass by Reference ----------#
