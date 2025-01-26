
"""
task 9

Define a function named check_sum. A function should print a message "verification passed" if a
sum of the provided arguments is equal or greater than 50. Otherwise, it should print "not enough"

"""
from unittest.mock import patch

def exponentiation(list_data: list):
    sum_elements = 0
    for list_element in list_data:
        sum_elements = sum_elements + list_element
    if sum_elements >= 50:
        print( "verification passed")
    else:
        print("not enough")
#    print("verification passed") if summary >= 50 else print("not enough")

inputs = ['8 11', '10 10 10 10 1', '20 20 10' ]

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        numbers = map(int, input("numbers: ").split())
        numbers_list = list(numbers)
        exponentiation(numbers_list)
