from unittest.mock import patch

"""
task 8
Write a program that takes three integers as input in a single line separated by spaces and then outputs 
them sequentially with commas.
"""

inputs = ['1 2 3', '5 43 21', '8 7 -98', '5 4 3']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        numbers = map(int, input("numbers: ").split())
        numbers_list = list(numbers)
        numbers_str = ', '.join(map(str, numbers_list))

        print(f"Для входных данных '{numbers_list}': {numbers_str}")
        print("или через sep:")
        print(*numbers_list, sep=',')
