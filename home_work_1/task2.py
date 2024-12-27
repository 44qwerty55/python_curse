from unittest.mock import patch
"""
task 2
Write a program that calculates the length of a line segment (i.e., the distance between two points) given 
two values x1 and x2 (can be either integers or float numbers)
"""

inputs = ['-2 6.5', '3 -9', '5 3', '10.5 8.0']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number1, number2 = input("number: ").split()
        max_number = max(float(number1), float(number2))
        min_number = min(float(number1), float(number2))
        actual_result = max_number - min_number
        print(f"Для входных данных '{input_value}': {actual_result}")