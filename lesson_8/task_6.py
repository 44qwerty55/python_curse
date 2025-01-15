from unittest.mock import patch

"""
task 6
"""

inputs = ['8 11', '90 800', '-1 -3']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        numbers = map(int, input("numbers: ").split())
        numbers_list = list(numbers)
        if  numbers_list[1] > numbers_list[0]:
            print(f"Для входных данных '{numbers_list}': {numbers_list[0]} , {numbers_list[1]}")
        else:
            print(f"Для входных данных '{numbers_list}': {numbers_list[1]} , {numbers_list[0]}")
