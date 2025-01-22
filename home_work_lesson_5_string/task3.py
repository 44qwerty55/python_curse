from unittest.mock import patch
"""
task 3
We're going to write a script that takes user input, so that we're not working with static content, and print 
out some information and permutations of the string that the user has entered.
• Print first character from the User's Input
• Print last character from the User's Input
• Print middle character from the User's Input
• Print the Even Index Characters
• Print the Odd Index Characters
• Print the String in Reverse"""

inputs = ['Manchester City', 'Testt', 'ABCDEFGHIJKLMNOP']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        text_value = input("number: ")
        actual_result = text_value[0]
        print(f"Для входных данных '{input_value}' Print first character from the User's Input: {actual_result}")

        actual_result = text_value[-1]
        print(f"Для входных данных '{input_value}' Print last character from the User's Input: {actual_result}")

        len_value = len(text_value)
        index_value = int(len_value/2)
        actual_result = text_value[index_value]
        print(f"Для входных данных '{input_value}' Print middle character from the User's Input: {actual_result}")

        actual_result = text_value[::2]
        print(f"Для входных данных '{input_value}' Print the Even Index Characters: {actual_result}")

        actual_result = text_value[1::2]
        print(f"Для входных данных '{input_value}' Print the Odd Index Characters: {actual_result}")

        actual_result = text_value[::-1]
        print(f"Для входных данных '{input_value}' Print the String in Reverse: {actual_result}")













