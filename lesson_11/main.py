from lesson_11.calc_mods.calculator_module import calculate
from lesson_11.calc_mods.mul_mod import mul

x = 7
y = 0
print("task_1")
print(f"{x} * {y} = {mul(x, y)}")
print("task_2")
print(f"{x} + {y} = {calculate(x, y, '+')}")
print(f"{x} - {y} = {calculate(x, y, '-')}")
print(f"{x} * {y} = {calculate(x, y, '*')}")
print(f"{x} / {y} = {calculate(x, y, '/')}")


