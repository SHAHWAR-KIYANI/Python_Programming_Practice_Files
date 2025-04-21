import time
# Implementation 1: Time Count Down Program
time_countdown = int(input("Enter the Number to start the Count Down: "))
for x in range(1, time_countdown + 1, 1):
    time.sleep(1)
    print(x)
print("Time's Up")

# Implementation 2: Time Count Down Program
time_countdown = int(input("Enter the Number to start the Count Down: "))
for x in reversed(range(1, time_countdown + 1, 1)):
    time.sleep(1)
    print(x)
print("Time's Up")

# Implementation 3: Time Count Down Program
time_countdown = int(input("Enter the Number to start the Count Down: "))
for x in range(time_countdown,0, -1):
    time.sleep(1)
    print(x)
print("Time's Up")

# Implementation 4: Time Count Down Program in the Form of Do While Loop Behaviour
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

# Example 1: Program to Calculate (Years,Days,Hours,Minutes,Seconds)
time_countdown = int(input("Enter the Number to start the Count Down: "))
for x in range(time_countdown, 0,  -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600) % 24
    days = (x // 86400) % 365
    years = (x // 31536000)
    print(f"{years:03}Years: {days:03}Days: {hours:02}Hours: {minutes:02}Minutes: {seconds:02}Seconds")
    time.sleep(1)
print()
# Example 2: Program to Calculate (Years,Days,Hours,Minutes,Seconds) since 1st January 1970.
time_countdown = int(time.time())
for x in range(time_countdown, 0,  -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600) % 24
    days = (x // 86400) % 365
    years = (x // 31536000)
    print(f"{years:03}Years: {days:03}Days: {hours:02}Hours: {minutes:02}Minutes: {seconds:02}Seconds")
    time.sleep(1)