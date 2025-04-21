# The continue statement skips the current iteration of the loop and the control flow of the program goes to the next iteration.
# Example 1: continue Statement with for Loop
# We can use the continue statement with the for loop to skip the current iteration of the loop and jump to the next iteration.
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output of Example 1:
# 0
# 1
# 2
# 4

# Example 2: continue Statement with while Loop
# We can use the continue statement with the while loop to skip the current iteration of the loop and jump to the next iteration.
# Program to print odd numbers from 1 to 10
num = 0
while num < 10:
    num += 1
    if (num % 2) == 0:
        continue
    print(num)
# Output of Example 2:
# 1
# 3
# 5
# 7
# 9