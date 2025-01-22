"""
task 5

Write a program to create a function show_employee() using the following conditions.
• It should accept the employee’s name and salary and display both.
• If the salary is missing in the function call then assign default value 9000 to salary.

"""

def show_employee(name: str, salary: int = 9000):
    print(f"employee’s name: {name}, salary: {salary}")


show_employee("Ben", 1200)
show_employee("Jessa", )