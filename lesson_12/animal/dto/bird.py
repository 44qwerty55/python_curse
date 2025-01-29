from lesson_12.animal.dto.animal import Animal


class Bird(Animal):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

class Parrot(Bird):
    def make_sound(self):
        print("Parrot sound")

class Eagle(Bird):
    def make_sound(self):
        print("Eagle sound")