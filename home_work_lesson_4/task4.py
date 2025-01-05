from unittest.mock import patch
"""
task 4
The program receives three integers as input - the sides of a triangle.
It should output True if these sides form an isosceles triangle (2 sides are equal), otherwise - False.
You need to solve the task without using conditional statements.
"""

inputs = ['4 6 9', '7 8 7']

for input_value in inputs:
    with (patch('builtins.input', return_value=input_value)):
        numbers = map(int, input("numbers: ").split())
        numbers_list = list(numbers)

        actual_result = (numbers_list[0] == numbers_list[1]) or (numbers_list[1] == numbers_list[2]) or (numbers_list[0] == numbers_list[2])
        print(f"Для входных данных '{input_value}': {actual_result}")