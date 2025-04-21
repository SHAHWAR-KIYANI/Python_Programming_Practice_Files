# Example 1
# Description: Here Invalid inputs are empty string and only whitespaces (spaces,tabs,newlines) and everything else is valid
name = input ("Enter Your Complete Name: ")
name = name.strip()
while name == "" or name.isspace() == True:
     print("You did not Enter any Name! Enter Again: ")
     name = input("Enter Your Complete Name: ")
     name = name.strip()
print(f"Welcome! {name}")

# Example 2
# Description: Here if inputs are q/Q, an empty string, the loop will not execute else it will execute and will keep on asking for one of the favourite foods.
food = input ("Enter the Food You Like: (Q to Quit): ")
food = food.strip()
food = food.upper()
while not food =="" and food != "Q":
     print(f"You like {food}")
     food = input ("Enter the Food You Like: (Q to Quit): ")
     food = food.strip()
     food = food.upper()
if food == "Q":
     print(f"You have Entered {food} to Quit and That's why loop is Exited!")
else:
     print("You have Entered an Empty String. That's why loop is Exited!")

# Example 3
# Description: Here only valid number will be accepted and printed on the screen and for invalid numbers, while loop will be executed until valid number is entered.
number = int(input("Enter a Number Between 1 to 10: "))
while number < 1 or number > 10:
     print("You Have Entered an invalid Number Which is: ",end=" ")
     print(f"{number}")
     number = int(input("Enter a Number Again Between 1 to 10: "))
     print()
print(f"You have Entered {number} Which is within the range")