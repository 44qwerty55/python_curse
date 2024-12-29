from unittest.mock import patch
"""
task 1
"""

inputs = ['8', '190']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = int(input("number: "))
        number += 1
        print(f"Для входных данных '{input_value}': {number}")