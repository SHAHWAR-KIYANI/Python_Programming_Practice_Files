# The break statement terminates the loop immediately when it's encountered.
# Example 1: break Statement with for Loop
for i in range(5):
    if i == 3:
        break
    print(i)
# Output of Example 1:
# 0
# 1
# 2

# Example 2: break Statement with while Loop
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
# Output of Example 2:
# 0
# 1
# 2