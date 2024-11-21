class Car():
    def __init__(self, type) -> None:
        self.type = type
        self.properties = {}

    def set_properties(self, color, cost):
        self.properties = {"Color": {color}, "Cost": {cost}}

    def get_properties(self):
        return self.properties

class PetrolCar(Car):
    def __init__(self, type) -> None:
        self.type = type
        self.properties = {}

car_01 = PetrolCar("Toyota")
car_01.set_properties("Red", 12000)
print(car_01.__dict__)

car_02 = PetrolCar("BMW")
car_02.set_properties("Red", 21000)
print(car_02.__dict__)

car_03 = PetrolCar("Toyota")
car_03.set_properties("Black", 16000)
print(car_03.__dict__)

cars = [car_01, car_02, car_03]