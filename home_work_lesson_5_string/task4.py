from unittest.mock import patch
"""
task 4
Accept user input of a string that contains several words separated by blank space.
Print the Lowercase, Uppercase, Title Case, and Capitalized Versions of the User's Input.
Separate the String and Print the Individual Words as a List.
Print the Alphabetic First and Last Words from the words list (search about sorted() method).

"""

inputs = ['This is a test message!']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        text_value = input("number: ")
        actual_result = text_value.lower()
        print(f"Для входных данных '{input_value}' Print Lowercase: {actual_result}")

        actual_result = text_value.upper()
        print(f"Для входных данных '{input_value}' Print Uppercase: {actual_result}")

        actual_result = text_value.title()
        print(f"Для входных данных '{input_value}' Print Title Case: {actual_result}")

        actual_result = text_value.capitalize()
        print(f"Для входных данных '{input_value}' Print Capitalized: {actual_result}")

        list_worlds = text_value.split()
        actual_result = "','".join(list_worlds)
        print(f"Для входных данных '{input_value}' Print list: '{actual_result}'")

        sorted_list =sorted(list_worlds)
        actual_result = sorted_list[0]
        print(f"Для входных данных '{input_value}' Print first world: {actual_result}")

        actual_result = sorted_list[-1]
        print(f"Для входных данных '{input_value}' Print last world: {actual_result}")














