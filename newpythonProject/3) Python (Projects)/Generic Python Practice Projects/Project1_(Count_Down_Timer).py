import time

def display_header():
    print("=" * 50)
    print("\t\tTIMER PROGRAM")
    print("=" * 50)

def countdown_timer(start_time: int):
    print("\nStarting Countdown Timer...\n")
    for x in range(start_time, 0, -1):
        seconds = x % 60
        minutes = (x // 60) % 60
        hours = (x // 3600) % 24
        days = (x // 86400) % 365
        years = x // 31536000
        print(f"{years:03} Years | {days:03} Days | {hours:02} Hours | {minutes:02} Minutes | {seconds:02} Seconds")
        time.sleep(1)
    print("\nCountdown Completed!\n")

def timer_since_epoch():
    print("\nDisplaying Time Since Epoch...\n")
    start_time = int(time.time())
    countdown_timer(start_time)

def main():
    while True:
        display_header()
        print("1. Countdown Timer")
        print("2. Timer Since Epoch")
        print("3. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            start_time = int(input("Enter the number to start the countdown: "))
            countdown_timer(start_time)
        elif choice == "2":
            timer_since_epoch()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        retry = input("Do you want to run the timer again? (yes/y or no/n): ").strip().lower()
        if retry not in ('yes', 'y'):
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()