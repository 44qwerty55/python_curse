from unittest.mock import patch
"""
task 2
You need to increase the Brad's salary to be 8500.
Then, print the updated dictionary

"""
workers = {
    'employer1': {'name': 'Jhon', 'salary': 7500},
    'employer2': {'name': 'Emma', 'salary': 8000},
    'employer3': {'name': 'Brad', 'salary': 500}
}

workers['employer3']['salary'] = 8500
print(workers)




