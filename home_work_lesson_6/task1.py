
"""
task 1
1) Set the "users" variable to be an empty list.
2) Add "kevin", "bob", and "alice" to the users list in that order without reassigning the variable.
3) Remove "bob" from the `users` list without reassigning the variable.
4) Reverse the users list and assign the result to `rev_users`.
5) Add the user "melody" to users where "bob" used to be.
6) Add the users "andy", "wanda", and "jim" to the users list using a single command.
7) Slice the users lists to return the 3rd and 4th items and assign the result to `center_users`
"""

new_list = []
print(f"Set the 'users' variable to be an empty list: {new_list}")
new_list.append("kevin")
new_list.append("bob")
new_list.append("alice")
print(f"Add : {new_list}")
index_of_remove = new_list.index("bob")
new_list.pop(index_of_remove)
print(f"Remove 'bob' : {new_list}")
rev_users = new_list.copy() #.reverse()
rev_users.reverse()
print(f"Reverse : {rev_users}")
new_list.insert(index_of_remove, "melody")
print(f"Add the user 'melody' to users where 'bob' used to be : {new_list}")
new_list = new_list + ["andy", "wanda", "jim"]
print(f"Add the users : {new_list}")
center_users = new_list[2:4].copy()
print(f" Slice the users lists to return the 3rd and 4th items : {center_users}")