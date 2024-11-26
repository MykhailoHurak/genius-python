class Car:
    def __init__(self, type) -> None:
        self.type = type
        self.properties = {}

    def set_properties(self, color, cost):
        self.properties = {"Color": color, "Cost": cost}

    def get_properties(self):
        print(self.properties)
        return self.properties

class PetrolCar(Car):
    def __init__(self, type) -> None:
        self.type = type
        self.properties = {}

car_01 = Car("Toyota")
car_01.set_properties("Red", 12000)
car_01.get_properties()

car_02 = PetrolCar("BMW")
car_02.set_properties("Red", 21000)

car_03 = PetrolCar("Toyota")
car_03.set_properties("Black", 16000)

cars = [car_01, car_02, car_03]

# print(f"Car 01 - {car_01.type}")
# print(f"Car 02 - {car_02.type}")
# print(f"Car 03 - {car_03.type}, color: {car_03.color}")

def get_concret_type_car(type):
    count = 0
    for car in cars:
        if car.type == type:
            count += 1

    print(f"Count of {type} cars: {count}")

def get_concret_color_car(color):
    count = 0
    for car in cars:
        if car.properties["Color"] == color:
            count += 1

    print(f"Count of {color} cars: {count}")

get_concret_type_car("Toyota")
get_concret_color_car("Black")