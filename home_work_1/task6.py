from unittest.mock import patch

"""
task 6
Write a program that will find how many full kilograms can fit into a given number of grams.
"""

inputs = '3456'

with patch('builtins.input', return_value=inputs):
    grams = int(input("numbers: "))
    actual_kilograms = grams // 1000

    print(f"Для входных данных '{grams}': {actual_kilograms}")
