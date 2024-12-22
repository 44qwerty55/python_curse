# task 6
# input 45 80 98 47 81, 1 86 63 98 20
scores = map(int, input("numbers: ").split())
scores_list = list(scores)
max_score = max(scores_list)
print(max_score)
