# For generating random numbers, random module is used in python which contains multiple different methods.
import random
# 1) random.randint() Method
#  It generates integers. It takes two parameters, which define the range of the numbers to be generated like starting and ending points.
low = int(input("Enter the lower limit for randint(): "))
high = int(input("Enter the higher limit for randint(): "))
generate_integers = random.randint(low, high)
print(f"The Random Number Generated is Between {low} and {high} such as: {generate_integers}")
print()

# 2) random.random() Method
# It generates floating point number between 0 and 1.
floating_number = random.random()
print(f"The Random Number Generated is: {floating_number}")
print()

# 3) random.choice() Method
rpsGame = ("Rock","Paper","Scissors")
option = random.choice(rpsGame)
print(f"The Random Option Generated is: {option}")
print()

# 4) random.shuffle() Method
list_of_numbers = [1,2,3,4,5,6]
random.shuffle(list_of_numbers)
print(list_of_numbers)

# print(help(random))
# print(dir(random))