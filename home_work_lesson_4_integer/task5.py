from unittest.mock import patch
"""
task 5
The program receives two integers on the same line as input.
The program should output True if both numbers are divisible by 7, otherwise - False.
You need to solve the task without using conditional statements.
"""

inputs = ['77 14', '35 10']

for input_value in inputs:
    with (patch('builtins.input', return_value=input_value)):
        numbers = map(int, input("numbers: ").split())
        numbers_list = list(numbers)

        actual_result = numbers_list[0] % 7 == 0 and numbers_list[1] % 7 == 0
        print(f"Для входных данных '{input_value}': {actual_result}")