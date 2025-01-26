"""
task 4

Write a program to create function calculation() such that it can accept two variables (integers) and
calculate addition and subtraction. Also, it must return both addition and subtraction in a single
return call.
"""

def calculation(a: int, b: int) -> tuple:
    addition = a + b
    subtraction = a - b
    return (addition, subtraction)

res = calculation(40, 10)
print(res)