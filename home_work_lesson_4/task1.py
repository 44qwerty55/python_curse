from unittest.mock import patch
"""
task 1
The input is an integer.
The program should output True if the entered value is not divisible by 9, otherwise - False.
You need to solve the task without using conditional statements.
"""

inputs = ['45', '21']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = int(input("number: "))
        actual_result = number % 9 != 0
        print(f"Для входных данных '{input_value}': {actual_result}")