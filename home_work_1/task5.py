from unittest.mock import patch

"""
task 5
Once, visiting a stationery store, Jack bought X pencils, Y pens, and Z markers. It is known that the price of 
a pen is 2$ more than the price of a pencil and 7$ less than the price of a marker. It is also known that the 
cost of a pencil is 3$. The task is to determine the total cost of the purchase.
"""

inputs = ['1 1 1', '23 8 76', '75 5 72']

for input_value in inputs:
    with patch('builtins.input', return_value=input_value):
        numbers = map(int, input("numbers: ").split())
        numbers_list = list(numbers)
        pencils = int(numbers_list[0])*3
        pens = int(numbers_list[1]) * 5
        markers = int(numbers_list[2]) * 12
        actual_result = pencils + pens + markers

        print(f"Для входных данных '{numbers_list}': {actual_result}")
