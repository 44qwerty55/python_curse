from unittest.mock import patch
"""
task 1
1) Set the emails variable to be an empty dictionary
2) Add 'ashley', 'craig', and 'elizabeth' according to the format:
3) Remove 'craig' from the emails dictionary without reassigning the variable, just by using the 
corresponding method/statement
4) Add 'dalton' to the emails dictionary without reassigning the variable.
5) Return a list of keys from the emails dictionary , assign to `users` variable and print.
6) Return a list of values from the emails dictionary , assign to `email_list` variable and print.
# 7) Return a list of items, assign to `pairs` variable (representing the key/value pairs in `emails`) and print.


"""

emails = {}
print(emails.items())
emails['ashley'] = 'ashley@test.com'
emails['craig'] = 'craig@test.com'
emails['elizabeth'] = 'elizabeth@test.com'
print(emails.items())
emails.pop('craig')
#del emails['craig']
# 4) Добавляем 'dalton' в словарь emails
emails['dalton'] = 'dalton@test.com'

# 5) Возвращаем список ключей из словаря emails и присваиваем переменной users
users = list(emails.keys())
print(users)

# 6) Возвращаем список значений из словаря emails и присваиваем переменной email_list
email_list = list(emails.values())
print(email_list)

# 7) Возвращаем список элементов (пар ключ/значение) и присваиваем переменной pairs
pairs = list(emails.items())
print(pairs)











