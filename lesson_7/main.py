

new_list = ["andy", "wanda", "jim"]
list_to_add = ["andy1", "wanda2", "jim3"]
new_list.append(list_to_add)
print(new_list)
print(f"id new_list:  {id(new_list)}")

print(new_list[3])
print(f"id list_to_add in new_list:  {id(new_list[3])}")

new_list_copy = new_list.copy()

print(new_list_copy)
print(f"id new_list_copy:  {id(new_list_copy)}")

print(new_list_copy[3])
print(f"id list_to_add in new_list_copy:  {id(new_list_copy[3])}")