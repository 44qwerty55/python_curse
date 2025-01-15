from unittest.mock import patch

"""
task 3
"""

inputs = ['8 11', '50 21']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        numbers = map(int, input("numbers: ").split())
        numbers_list = list(numbers)
        if  numbers_list[0] > numbers_list[1]:
            print(f"Для входных данных '{numbers_list}': {numbers_list[0]}")
        else:
            print(f"Для входных данных '{numbers_list}': {numbers_list[1]}")
