from unittest.mock import patch

"""
task 4
"""

inputs = ['imagine enigami', 'imagine imagine']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        worlds = map(str, input("numbers: ").split())
        worlds_list = list(worlds)
        if  worlds_list[0] == worlds_list[1][::-1]:
            print(f"Для входных данных '{worlds_list}': YES")
        else:
            print(f"Для входных данных '{worlds_list}': NO")
