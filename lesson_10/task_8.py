
"""
task 8

Define a function named count_args(). A function should return a number of the provided
arguments when a function is called

"""
def count_args(*arguments):
    return len(arguments)

inputs = [(1, 2, 3), (1, 2), (4,), ()]

for input_value in inputs:
    print(count_args(*input_value))
