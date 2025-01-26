"""
task 1

- Create a function (named get_text_length()) that receives a string (with "Hello" as a default value)
and returns it's length
- Create a function (named get_text_length_in_list()) that receives a list of strings and returns it's
TOTAL length only by using calls to the first function ( get_text_length )

"""

def get_text_length(text: str ="Hello") -> int:
    return len(text)

def get_text_length_in_list(list_of_values: list) -> int:
    total_length = 0
    for string in list_of_values:
        total_length += get_text_length(string)
    return total_length


example_list = ["qwerty", "asdfg", "kkkki"]
result = get_text_length_in_list(example_list)
print(result)