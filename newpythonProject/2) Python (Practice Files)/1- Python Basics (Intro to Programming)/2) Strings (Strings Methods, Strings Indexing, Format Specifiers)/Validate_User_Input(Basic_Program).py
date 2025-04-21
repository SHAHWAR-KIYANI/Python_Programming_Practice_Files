# Validate User Input such that it is no more than 12 characters long, must not contain spaces and digits
username = input("Enter Username without White Spaces: ")
if len(username) < 12 and username.find(" ") == -1 and username.isalpha() == True:
    print(f"Welcome, {username}")
elif len(username) > 12:
    print("Your Username Cannot Be More Than 12 Characters Long")
elif username.find(" ") != -1:
    print(f"Your Username Cannot Contain White Spaces")
elif not username.isalpha():
    print("Your Username Cannot Contain Digits")