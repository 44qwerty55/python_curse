from unittest.mock import patch
"""
task 1
Find the result of the expression: |a| + |b|
The values of variables 'a' and 'b' are provided as input on separate lines and can only be of integer type.
"""

inputs = ['-5 9', '-1 -4']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number1, number2 = input("number: ").split()
        actual_result = abs(int(number1)) + abs(int(number2))
        print(f"Для входных данных '{input_value}': {actual_result}")