from unittest.mock import patch

"""
task 4
Your task is to output, given the values of a, b, and c, what is the maximum value of the expression that 
can be obtained.
"""

inputs = ['1 2 3', '2 10 3', '1 1 1', '8 4 1', '6 5 3']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        numbers = map(int, input("numbers: ").split())
        numbers_list = list(numbers)

        first_number_result = numbers_list[0] + numbers_list[1] * numbers_list[2]
        second_number_result = numbers_list[0] * (numbers_list[1] + numbers_list[2])
        fired_number_result = numbers_list[0] * numbers_list[1] * numbers_list[2]
        fourth_number_result = (numbers_list[0] + numbers_list[1]) * numbers_list[2]
        actual_result = max(first_number_result, second_number_result, fired_number_result, fourth_number_result)

        print(f"Для входных данных '{numbers_list}': {actual_result}")
