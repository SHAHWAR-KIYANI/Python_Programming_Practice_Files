                                                                # Variables and Data Types
variable1: float  = 1.5
print(type(variable1))

variable2: int  = 1
print(type(variable2))

variable3: complex  =  1 + 3j
print(type(variable3))

# Example: Adding Complex Numbers
complex1: complex = 1+2j
complex2: complex = 2+3j
sum_of_complex = complex1 + complex2
print(sum_of_complex)

variable4: str = "Alpha Bravo Charlie"
print(type(variable4))

variable5: bool  = True
print(type(variable5))
variable5 = False
print(type(variable5))

variable6: None = None
print(type(variable6))
                                                            # Input In Python and int(),float(),str(),bool() for Type Casting

# Input is taken in the form of a String and String will be either Empty or Non-Empty
number1: int = int(input("Enter Any Number1: "))
print(number1)
print(type(number1))

number2 = int(input("Enter Any Number2: "))
print(number2)
print(type(number2))

# print(f"Sum of Numbers = {number1 + number2}")
print("Sum of Numbers =",number1 + number2)
print()
                                                                                                                        # Output In Python
print("Hello!",end=" ")
print("Shahwar: ",end="")
print("Welcome to Python World!")
print()
print("Have a nice day!")
