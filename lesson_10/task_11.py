
"""
task 11

Define a function named only_one_poitive(). A function should return True in case of there is only
one positive number in the provided arguments. Otherwise, it will print False

"""


def only_one_positive(*arguments) -> bool:
    result_for_arguments = 0
    for elem in arguments:
        if elem > 0:
            result_for_arguments += 1
    return result_for_arguments == 1


data = [(1, 2), (-1, 0, -3, 5, -3), (4,), ()]

for input_value in data:
    result = only_one_positive(*input_value)
    print(f"input: {input_value}, result: {result}")