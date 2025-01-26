"""
task 1

Write a function that takes a list and returns a new list that removes duplicates from the provided list.
Solve it in two ways.
"""
def dedupe_v1(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y


# this one uses sets
def dedupe_v2(x):
    return list(set(x))


a = [1, 2, 3, 4, 3, 2, 1]
print(a)
print(dedupe_v1(a))
print(dedupe_v2(a))