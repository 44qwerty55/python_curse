from unittest.mock import patch

"""
task 10
"""

inputs = ['qwerty qwerty', 'qwerty123 qwerty', 'qwertyuio qwertyuio', 'qwert qwerty']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        pass1, pass2 = map(str, input("pass: ").split())

        if  len(pass1) < 7:
            print(f"Для входных данных '{pass1}': Short")
        else:
            if pass1 != pass2:
                print(f"Для входных данных '{pass1}' '{pass2}'  : Difference")

            if len(pass1) >= 7 and pass1 == pass2:
                print(f"Для входных данных '{pass1}': Ok")



