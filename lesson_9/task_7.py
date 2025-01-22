
"""
task 7

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 251] and makes a new 
list of only the first and last elements of the given list. For practice, write this code inside a function.
You'll need to define a function list_ends().

"""

def list_ends(numbers: list) -> list:
    return list(filter(lambda x: x == numbers[0] or x == numbers[-1], numbers))


a = [5, 10, 15, 20, 251]
result = list_ends(a)
print(result)