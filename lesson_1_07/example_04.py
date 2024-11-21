class Vehicle:
    """It's a base class for Vehicles"""
    def __init__(self, type, color, left_of_life=100) -> None:
        self.type = type
        self.color = color
        self.left_of_life = left_of_life

    def move(self):
        print("Your vehicle is moving")

    def fix(self):
        if self.left_of_life <= 50:
            print(f"{self.type} need to fix")
        else:
            print(f"Your {self.type} is good")

class Car(Vehicle):
    """Class Car"""

    def __init__(self, type, color, left_of_life, cost=0) -> None:
        super().__init__(type, color, left_of_life)
        self.cost = cost

    def move(self):
        print(f"{self.color} {self.type} is moving")
        print(f"Cost of this car is {self.cost}")

class Bicycle(Vehicle):
    """Class Bicycle"""

    def __init__(self, type, color, left_of_life, count_of_wheels) -> None:
        super().__init__(type, color, left_of_life)
        self.count_of_wheels = count_of_wheels

    def move(self):
        print("Run bicycle")

# ------------------------------------------

car_01 = Car("BMW", "black", 70, 11000)
car_01.move()
car_01.fix()

bicycle_01 = Bicycle("Leleka", "green", 30, 2000)
bicycle_01.move()
bicycle_01.fix()