from unittest.mock import patch
"""
task 2
1. Create a variable named 'value' prompt the user for a value, convert it to an int, and store it off in a variable.
2. Print "FizzBuzz" if the value Is a multiple of 3 and 5 (example -> value % 5 == 0) or just print the value otherwise.
3. Add additional cases. Print "Fizz" if the value is just a multiple of 3, and "Buzz" if it's a multiple of 5.
"""

inputs = ['1', '2', '15']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        month = int(input("number: "))
        match month:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                print("31 days")
            case 4 | 6 | 9 | 11:
                print("30 days")
            case 2:
                print("28 days")
            case _:
                print("Invalid month")