from unittest.mock import patch

"""
task 9
"""

inputs = ['6', '1', '0']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = int(input("numbers: "))
        match number:
            case 1:  print(f"Для входных данных '{number}': january")
            case 6:  print(f"Для входных данных '{number}': iun")
            case _:  print(f"Для входных данных '{number}': Invalid month")
