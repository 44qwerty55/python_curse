from lesson_11.calc_mods.add_mod import add


def mul(num_1, num_2):
    result = 0
    for _ in range(num_2):
        result = add(result, num_1)
    return result