class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def test(self):
        print(f"my name iz {self.name} my agis is {self.age}")


class Terrir(Dog):
    def __init__(self, name, age, breed, sound="arffff"):
        super().__init__(name, age)
        self.breed = breed
        self.sound = sound

    def test(self):
        print('Terrir')
