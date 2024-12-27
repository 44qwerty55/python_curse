from unittest.mock import patch
"""
task 3
We provide an input of a float number , and we need to round them to the 2nd and 3rd decimal places 
respectively. The obtained results should be displayed separated by a space on a single line.
"""

inputs = ['0.123456789', '45.789437823721']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = input("number: ")
        round_number_2 = round(float(number), 2)
        round_number_3 = round(float(number), 3)
        print(f"Для входных данных '{input_value}': {round_number_2}, {round_number_3}")