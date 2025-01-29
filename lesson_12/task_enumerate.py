
"""
task 1
"""

words = ["qqwe", "eerr", "ddff"]
words_with_position = enumerate(words, start=1)
print(f"task 1: '{list(words_with_position)}'")

"""
task 2
"""
words_with_position = enumerate(words, start=1)
print("task 2")
for index, world in words_with_position:
    print(f"World with index: '{index}'  =  '{world}'")
