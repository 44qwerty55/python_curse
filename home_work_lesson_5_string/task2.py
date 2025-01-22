from unittest.mock import patch
"""
task 2
The program receives a string as input. Your task is to print all characters of this string that have even indices
"""

inputs = ['Manchester City', 'Testt']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = input("number: ")
        actual_result = number[0::2]
        print(f"Для входных данных '{input_value}': {actual_result}")