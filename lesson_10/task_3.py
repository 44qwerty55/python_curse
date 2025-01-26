"""
task 3

Define a function exponentiation() that gets as an input an integer and prints the square and cube
of this number to the screen separated by a space

"""
from unittest.mock import patch

def exponentiation(n: int):
    square = n ** 2
    cube = n ** 3
    print(square, cube)

inputs = ['3', '2', '10']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
       number = int(input("number: "))
       exponentiation(number)