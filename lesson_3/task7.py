# task 6
# input 2 3 4 5, 3 3 4 4, 5 3 4 5
scores = map(int, input("numbers: ").split())
scores_list = list(scores)
average = sum(scores_list) / len(scores_list)
print(average)
