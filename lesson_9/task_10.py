
"""
task 10

Define a function named multiply(). A function should return a multiplication of all provided
arguments. In case of non-provided arguments – a function should return 1.

"""


def exponentiation(list_data: list):
    mul_elements = 1
    if len(list_data) == 0:
        print(1)
    else:
        for list_element in list_data:
          mul_elements = mul_elements * list_element
        print(mul_elements)

#    print("verification passed") if summary >= 50 else print("not enough")

data = [(1, 2, 3), (1, 2), (4,), ()]

for input_value in data:
    numbers_list = list(input_value)
    print(numbers_list)
    exponentiation(numbers_list)
