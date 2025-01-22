from unittest.mock import patch
"""
task 6
The program receives an integer as input. It should output True if the given number is a two-digit number, 
otherwise - False.
You need to solve the task without using conditional statements.
"""

inputs = ['77', '777']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = int(input("number: "))
        actual_result = 10 <= number <= 99
        print(f"Для входных данных '{input_value}': {actual_result}")