from unittest.mock import patch

"""
task 8
"""

inputs = ['6 6 6', '90 800 90', '-1 -3 0']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        numbers = map(int, input("numbers: ").split())
        numbers_list = list(numbers)

        if  numbers_list[0] == numbers_list[1] == numbers_list[2]:
            print(f"Для входных данных '{numbers_list}': 3")
        elif numbers_list[0] == numbers_list[1] or numbers_list[0] == numbers_list[2] or numbers_list[2] == numbers_list[1]:
            print(f"Для входных данных '{numbers_list}': 2")
        else:
            print(f"Для входных данных '{numbers_list}': 0")
