from unittest.mock import patch
"""
task 2
The program receives three integers as input - the sides of a triangle.
It should output True if these sides have equal length (regular triangle), otherwise - False.
You need to solve the task without using conditional statements.
"""

inputs = ['5 5 5', '4 5 6']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        numbers = map(int, input("numbers: ").split())
        numbers_list = list(numbers)

        actual_result = numbers_list[0] == numbers_list[1] == numbers_list[2]
        print(f"Для входных данных '{input_value}': {actual_result}")