from lesson_12.animal.dto.bird import Parrot, Eagle
from lesson_12.animal.dto.mammal import Lion, Elephant


def zoo_announcement(animals):
    for animal in animals:
        print(f"Animal: {animal.get_name()}, Age: {animal.get_age()}, Sound: ", end="")
        animal.make_sound()


if __name__ == "__main__":
    zoo_animals = [
        Lion("Leo", 5),
        Elephant("Ella", 10),
        Parrot("Polly", 2),
        Eagle("Eddie", 3),
    ]

    zoo_announcement(zoo_animals)