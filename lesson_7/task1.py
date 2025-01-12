from unittest.mock import patch
"""
task 1
"""

inputs = ['8 11']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number1, number2 = map(int, input().split())
        actual_result = tuple(range(number1, number2 + 1))
        print(f"Для входных данных '{input_value}': {actual_result}")