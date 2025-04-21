# 1
# The pass statement serves as a placeholder for future code, preventing errors from empty code blocks.
# It's typically used where code is planned but has yet to be written.
def future_function():
    pass
# this will execute without any action or error
future_function()

# 2
# Suppose we didn't use pass or just put a comment as:
# n = 10
# if n > 10:
#   # Code Here
# print('Hello')
# Here, we will get an error message: IndentationError: expected an indented block

# Note:
# The difference between a comment and a pass statement in Python is that:
# While the interpreter ignores a comment entirely, pass is not ignored.