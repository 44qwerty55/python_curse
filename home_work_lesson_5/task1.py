from unittest.mock import patch
"""
task 1
The program receives a string as input and your task is to output last 4 element of this string.
"""

inputs = ['Manschester', 'Testt']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = input("number: ")
        actual_result = number[-4:]
        print(f"Для входных данных '{input_value}': {actual_result}")