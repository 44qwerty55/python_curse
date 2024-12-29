from unittest.mock import patch
"""
task 2
"""

inputs = ['100', '6.3']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = float(input("number: "))
        number *= 1.5
        print(f"Для входных данных '{input_value}': {number}")