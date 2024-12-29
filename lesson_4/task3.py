from unittest.mock import patch
"""
task 3
"""

inputs = ['43', '0', '-9']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = int(input("number: "))
        actual_result = bool(number)
        print(f"Для входных данных '{input_value}': {actual_result}")