# Note: Outer Loop controls the Rows (Number of Rows) and Inner Loop controls the Columns (Number of Columns)

# Implementation 1 (Nested For 4) Loops)
number1 = int(input("Enter any number: "))
for x in range (number1):
    for y in range(1,number1 + 1):
        print(y, end=" ")
    print()

# Implementation 2 (Nested For-While 4) Loops)
number2 = int(input("Enter any number: "))
for a in range(1, number2 + 1):
    while a % 2 == 0:
        print(a, end=" ")
        break
    print()

# Implementation 3 (Nested While 4) Loops)
number3 = int(input("Enter any number: "))
while number3 > 0:
    while not number3 % 2 == 0:
        print(number3, end=" ")
        break
    print()
    number3 = int(input("Enter any number: "))
print("Loop Exited Because You Have Entered Either Zero or a Negative Number!")

# Implementation 4 (Nested While-For 4) Loops)
number4 = int(input("Enter any positive number: "))
while number4 > 0:
    for b in range(1, number4 + 1):
        print(b, end=" ")
    print()
    number4 = int(input("Enter any positive number: "))
print("Loop Exited Because You Have Entered Either Zero or a Negative Number!")