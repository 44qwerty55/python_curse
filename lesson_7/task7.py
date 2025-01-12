
"""
task 6
"""
my_tuple = (11, [22, 33], 44, 55)
list_from_tuple = list(my_tuple)
list_from_tuple[1][0] = 222
my_tuple = tuple(list_from_tuple)
print(f"modify_tuple: {my_tuple}")
