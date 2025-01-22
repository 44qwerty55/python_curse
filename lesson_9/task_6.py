from unittest.mock import patch
"""
task 6

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a
string that reads the same forwards and backwards.)
You'll need to define a function reverse() , use a loop and conditions

"""



def show_palindrome(name: str):
    reverse_string = name[::-1]
    if name == reverse_string:
        print("palindrome")
    else:
        print("not palindrome")


inputs = ['alex', 'abba']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        world = input("number: ")
        show_palindrome(world)