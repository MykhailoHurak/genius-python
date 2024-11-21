# Абстракція

from abc import ABC, abstractclassmethod

class Car(ABC):

    def __init__(self, mark, cost) -> None:
        self.mark = mark
        self.cost = cost

    @abstractclassmethod
    def car_preview(self):
        pass

class Toyota(Car):

    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")

class BMW(Car):
        pass

toyota = Toyota("Corolla", 11000)
toyota.car_preview()

bmw = BMW("X7", 111000)
bmw.car_preview()
