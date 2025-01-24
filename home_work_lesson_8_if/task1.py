from unittest.mock import patch
"""
task 1
1. Create a variable named 'value' prompt the user for a value, convert it to an int, and store it off in a variable.
2. Print "FizzBuzz" if the value Is a multiple of 3 and 5 (example -> value % 5 == 0) or just print the value otherwise.
3. Add additional cases. Print "Fizz" if the value is just a multiple of 3, and "Buzz" if it's a multiple of 5.
"""

inputs = ['20', '19', '15']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        number = int(input("number: "))
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)