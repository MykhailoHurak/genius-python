# Абстракція

from abc import ABC, abstractclassmethod

class Animal(ABC):

    def move(self):
        pass

    def eat(self):
        pass

class Dog(Animal):

    def __init__(self, name, food) -> None:
        self.name = name
        self.food = food

    def move(self):
        print(f"Dog's name is {self.name}")

    def eat(self):
        print(f"Dog {self.name} eats {self.food}")

class AnimalType(ABC):
    pass

class Bird(AnimalType):

    def __init__(self, name) -> None:
        self.name = name
        
    def move(self):
        print(f"Bird's name is {self.name}")

    def eat(self):
        print(f"Bird {self.name} like to eat and fly")
        
dog = Dog("Rocky", "meat")
dog.move()
dog.eat()

bird = Bird("Leleka")
bird.move()
bird.eat()

animal_type = AnimalType()
animal_type.move()
animal_type.eat()