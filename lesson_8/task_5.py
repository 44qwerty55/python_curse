from unittest.mock import patch

"""
task 5
"""

inputs = ['8', '7']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = int(input("number: "))
        if number % 2 == 0:
            print(f"Для входных данных '{number}': Even")
        else:
            print(f"Для входных данных '{number}': Odd")



