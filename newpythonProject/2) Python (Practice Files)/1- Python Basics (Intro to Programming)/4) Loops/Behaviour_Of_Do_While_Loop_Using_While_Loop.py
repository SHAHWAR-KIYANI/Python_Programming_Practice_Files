import time
# Implementation 1: Time Count Down Program
time_countdown = int(input("Enter the Number to start the Count Down: "))
for x in range(1, time_countdown + 1, 1):
    time.sleep(1)
    print(x)
print("Time's Up")
option = input ("Do You Want to Continue? (Y/N): ")
option = option.upper()
while option == "Y" or option == "YES":
    time_countdown = int(input("Enter the Number to start the Count Down: "))
    for x in range(1, time_countdown + 1, 1):
        time.sleep(1)
        print(x)
    print("Time's Up")
    option = input ("Do You Want to Continue? (Y/N): ")
    option = option.upper()
print("Thanks For Using This Timer Program")