from unittest.mock import patch

"""
task 7
"""

inputs = ['imagine enigami?', 'imagine imagine']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        worlds = input("inputs: ")

        if  worlds[-1] == "?":
            print(f"Для входных данных '{worlds}': Question")
        else:
            print(f"Для входных данных '{worlds}': Regular")
