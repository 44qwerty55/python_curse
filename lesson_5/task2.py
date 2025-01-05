from unittest.mock import patch
"""
task 2
"""
print("task 1:")
input_value = 'Many MuCh'
print(input_value.upper())

print("task 2:")
inputs = ['Hellow helLoW', 'Qwert qwe', 'U2 U3']

for input_value in inputs:
    with (patch('builtins.input', return_value=input_value)):
        numbers = map(str, input("input: ").split())
        numbers_list = list(numbers)
        string_1 = numbers_list[0]
        string_2 = numbers_list[1]
        actual_result = string_1.upper() == string_2.upper()
        print(f"Для входных данных '{input_value}': {actual_result}")

print("task 3:")
input_value = 'asdfrtyyqwe'
print(input_value[0:3].upper() + input_value[3:-3].lower() + input_value[-3:-1].upper() + input_value[-1].upper())

print("task 4:")
input_value = 'asdfrtYyqwe'
print(input_value.lower().count("y"))

