from unittest.mock import patch

"""
task 9
In this task, we will decide ourselves what value to use as a separator in the `sep` parameter. 
The program takes a string as input, which will be used as a separator, and your task is to print the 
numbers from 1 to 5, with the entered separator between them.
"""

inputs = ['!', '$', 'BoB']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        separator = input("numbers: ")
        numbers_list = ['1', '2', '3', '4', '5']
        print(*numbers_list, sep=separator)
