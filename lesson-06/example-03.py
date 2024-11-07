class Person:
    """Class for creation persons"""
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def printAttrs(self):
        print(self.name, self.age)
        print(self)

person01 = Person("Mike", 33)
person01.printAttrs()
print(person01)

person02 = Person("Mykhailo", 18)
person02.printAttrs()
print(person02)