
"""
task 1
"""
input_value = 'Aleksandr'
print(input_value[0])

"""
task 2
"""
input_value = 'Free Nginx'
try:
    print(input_value[50])
except IndexError:
    print("IndexError: string index out of range")

"""
task 3
"""
input_value = 'Billie Elish'
print(input_value[-1])

"""
task 4
"""
input_value = 'abcdefg'
print(input_value[0:4])

"""
task 5
"""
input_value = 'Donald Trump'
print(input_value[1::2])

"""
task 6
"""
input_value = 'leetcode.com'
print(input_value[::-1])

"""
task 6
"""

input_value = 'leetcode.com'
new_value = input_value[-1] + input_value[:-1]
print(new_value)