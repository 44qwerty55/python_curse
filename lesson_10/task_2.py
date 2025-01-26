"""
task 1

There's the following names list : ["Yoav", "Ron", Aviva","Ronen', "Dan" ,"Galit"].
Using high order functions with lambda function:
• Print length of any name
• Print only names whose length are bigger than 4.

"""

names = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]

call_lambda_name =  lambda name: len(name)
lengths = list(map(call_lambda_name, names))
print(lengths)

call_lambda_name_over_fore =  lambda name: len(name)  > 4
names_over_fore = list(filter(call_lambda_name_over_fore, names))
print(names_over_fore)