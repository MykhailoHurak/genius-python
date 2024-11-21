from abc import ABC, abstractclassmethod

class DiscountCalculator(ABC):
    @abstractclassmethod
    def get_discounted_product():
        pass

class DiscountCalculatorShirt(DiscountCalculator):
    def __init__(self, cost) -> None:
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.1)
    
class DiscountCalculatorPant(DiscountCalculator):
    def __init__(self, cost) -> None:
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.2)
    
class DiscountCalculatorHat(DiscountCalculator):
    def __init__(self, cost) -> None:
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.25)
    
shirt = DiscountCalculatorShirt(1000)
print(shirt.get_discounted_product())

shirt = DiscountCalculatorPant(15000)
print(shirt.get_discounted_product())

shirt = DiscountCalculatorHat(800)
print(shirt.get_discounted_product())