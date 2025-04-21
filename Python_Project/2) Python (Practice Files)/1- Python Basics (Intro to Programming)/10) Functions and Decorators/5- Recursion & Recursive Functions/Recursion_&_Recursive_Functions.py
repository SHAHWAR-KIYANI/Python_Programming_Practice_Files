# Return keyword and Local variables play an important role in the recursion.
# Return keyword controls the execution of the function etc., returns some value or returns None.
# 10) Functions and 9- Decorators can call themselves. 10) Functions and 9- Decorators that call themselves are called recursive functions, and this programming technique is known as recursion.
# First Call is the Original Function Call and then Subsequent Recursive Calls are Generated depending on the condition.
# Each Recursive Function Call has its own separate Local Variable.

#  Example 1: Infinite Recursion
def greet():
    print("Hello")
    # recursive function call
    greet()
# function call
greet()

#  Example 2: Infinite Recursion
def print_numbers(n):
    print (n)
    print_numbers(n)
print_numbers(100)

#  Example 3: Finite Recursion
def print_numbers(n):
    if n>0:
        print(n)
        print_numbers(n-1)
print_numbers(3)

#  Example 4: Finite Recursion
def print_numbers(n):
    if n>0:
        print_numbers(n-1)
        print(n)
print_numbers(3)

                                                                           # ---------- Types of Recursion in Python ---------- #

# Recursion can be broadly classified into two types: tail recursion and non-tail recursion.
# The main difference between them is related to what happens after the recursive call.

# 1) Tail Recursion:
# This occurs when the recursive call is the last operation executed in the function, with no additional work or calculation following the recursive call.
# In many programming languages, tail recursion can be optimized by the compiler into iterative loops to improve performance and prevent stack overflow.

def tail_fact(n, acc=1):
    # Base case
    if n == 0:
        return acc
    # Tail recursive call with an accumulator
    else:
        return tail_fact(n-1, acc * n)
print(tail_fact(5))

# 2) Non-Tail Recursion:
# This occurs when there are operations or calculations that follow the recursive call.
# This type prevents the compiler or interpreter from optimizing the recursion into an iteration.

def nontail_fact(n):
    # Base case
    if n == 1 or n==0:
        return 1
    # Non-tail recursive call because the multiplication happens after the call
    else:
        return n * nontail_fact(n-1)
print(nontail_fact(5))


# Programs to Practice for Recursion
# 1) Check Palindrome String
# 2) Find the Length of the String
# 3) Decimal to Binary Conversion
# 4) Power of a Number
# 5) Fibonacci Series
# 6) Factorial of a Number