# task 6
# input 68 32 86
scores = map(float, input("numbers: ").split())
modified_scores = map(lambda x:( (x - 32)*5)/9, list(scores))
print(list(modified_scores))
