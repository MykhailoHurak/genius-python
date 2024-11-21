class Vehicle:
    """It's a base class for Vehicles"""
    def __init__(self, type, color) -> None:
        self.type = type
        self.color = color

    def move(self):
        print("Your vehicle is moving")

class Car(Vehicle):
    """Class Car"""

    def __init__(self, type, color, cost=0) -> None:
        super().__init__(type, color)
        self.cost = cost

    def run_engine(self):
        super().move()
        print("Run engine")

class Bicycle(Vehicle):
    """Class Bicycle"""

    def __init__(self, type, color, count_of_wheels) -> None:
        super().__init__(type, color)
        self.count_of_wheels = count_of_wheels

    def run_bicycle(self):
        print("Run bicycle")

# ------------------------------------------

car_01 = Car("car", "black", 11000)
car_01.run_engine()