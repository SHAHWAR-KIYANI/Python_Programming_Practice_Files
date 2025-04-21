string = "Raja"
# Implementation 1 (Print the String Value Character By Character and here loop will run depending upon the size/length of the string)
for x in string:
    print(f"OutPut = {x}")

# Implementation 2 (Print the String in Reverse Order)
for y in reversed(string):
    print(f"Output In Reverse Order = {y}")

# Implementation 3 (It will print from index 0 to 3 and here 4 means the end value)
for value in string[:4]:
    print(value)

# Implementation 4 (It will print from index 0 until last index and here 0 means the start value)
for value in string[0:]:
    print(value)

# Implementation 5 (It will print from start until end with a step value of 1)
for value in string[::]:
    print(value)

# Implementation 6 (It will print the whole string but in reverse order)
for value in string[::-1]:
    print(value)

# Implementation 7 (Using the Slicing Operator to Access The Elements of a String)
for counter in string[0:4:1]:
    print(f"Output = {counter}")

# Implementation 8 (Using the Slicing Operator to Access The Elements of a String but in reverse order using reversed function)
for counter in reversed(string[0:4:1]):
    print(f"Output = {counter}")

# Implementation 9 (Using the Slicing Operator to Access The Elements of a String but in reverse order)
for counter in string[0:4:-1]:
    print(f"Output = {counter}")

# Implementation 10 (Here 10 represents the End Value which is exclusive because when single value is used it means end => It will store numbers in num from 0 to 9. If Start is not defined then it means start value will be zero)
for num in range(10):
    print(num)

# Implementation 11 (It will print numbers from 1 until 10)
for num in range(1,11):
    print(num)

# Implementation 12 (It will run from 1 to 5 but in reverse order)
for num in reversed(range(1,6)):
    print(num)

print()
print()
# Example 1
for num in range(1,21):
    if num == 13:
        continue
    else:
        print(num)


print()
print()
# Example 2
for num in range(1,21):
    if num == 13:
        break
    else:
        print(num)