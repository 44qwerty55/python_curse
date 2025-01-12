
"""
# Given these inputs
numbers = (2, 4, 6, 8, 10)
word = "hello"

# Challenge:
# Create a single line that makes a tuple containing:
# 1. The word where each letter is repeated twice ('h' -> 'hh')
# 2. The sum of the first three numbers in the tuple
# 3. The word in uppercase, but only first and last letters
"""
numbers =  (2, 4, 6, 8, 10)
word = "hello"
result_tuple = (''.join([char * 2 for char in word]), sum(numbers[:3]), word[0].upper() + word[-1].upper())
print(result_tuple)
