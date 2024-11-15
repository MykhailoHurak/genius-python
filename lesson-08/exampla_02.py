class Card:
    """Class for users card"""

    def __init__(self, card_number, balance) -> None:
        if self.__check_attribute_type(card_number, str):
            self._card_number = card_number
        if self.__check_attribute_type(balance, float):
            self.__balance = balance

    def get_card_data(self):
        return self.__dict__
    
    def set_card_data(self, attr, value):
        if type(attr) == str:
            self. __dict__[attr] = value
            return {attr: self.__dict__[attr]}
        else:
            return "Attribute must be string type"
        
    def __check_attribute_type(self, attr, should_be):
        if type(attr) == should_be:
            return True
        else:
            raise TypeError(f"Attribute must be {should_be}")

user_card_01 = Card("4141 1234 5678 9012", 10010.0)

print(user_card_01.__dict__)
print(user_card_01._card_number)
# print(user_card_01.__balance) # буде помилка
# print(user_card_01._Card__balance) # не рекомендовано так звертатись

print(user_card_01.get_card_data())
print(user_card_01.set_card_data("card_number", "4141 0000 0000 0000"))
print(user_card_01.set_card_data(1111, "4141 1111 2222 3333"))

print(user_card_01.get_card_data())