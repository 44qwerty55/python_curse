from unittest.mock import patch
"""
task 6
"""

inputs = ['32', '76']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = int(input("number: "))
        actual_result = bool(number % 10 == 2)
        print(f"Для входных данных '{input_value}': {actual_result}")