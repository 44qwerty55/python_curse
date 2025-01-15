from unittest.mock import patch

"""
task 2
"""

inputs = ['10000', '30000', '23581']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = int(input("number: "))
        if number >= 20000:
            tax = number*13/100
            end_value = number - tax
            print(f"Для входных данных '{number}': {end_value}")
        else:
            print(f"Для входных данных '{number}': {number}")



