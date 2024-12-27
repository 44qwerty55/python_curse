from unittest.mock import patch

"""
task 7
The program receives one positive integer as input, and your task is to output its last digit
"""

inputs = ['123', '87632']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = int(input("numbers: "))
        actual_result = number % 10

        print(f"Для входных данных '{number}': {actual_result}")
