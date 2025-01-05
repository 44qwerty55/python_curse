from unittest.mock import patch
"""
task 3
The program receives an integer as input. It should output True if the entered value belongs to the 
interval from 5 (exclusive) to 19 (inclusive). Otherwise, it should output False.
You need to solve the task without using conditional statements.
"""

inputs = ['10', '5', '19']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = int(input("number: "))
        actual_result = 5 < number <= 19
        print(f"Для входных данных '{input_value}': {actual_result}")