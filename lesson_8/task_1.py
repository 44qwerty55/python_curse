from unittest.mock import patch

"""
task 1
"""

inputs = ['Python', 'lo Python']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        world = input("number: ")
        if world == "Python":
            print("Yes")
        else:
            print("No")



