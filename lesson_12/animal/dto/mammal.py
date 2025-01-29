from lesson_12.animal.dto.animal import Animal


class Mammal(Animal):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

class Lion(Mammal):
    def make_sound(self):
        print("Lion sound")


class Elephant(Mammal):
    def make_sound(self):
        print("Elephant sound")

