class Person:
    """Class for creation persons"""
    name = "Mike"
    age = 33
    high = 185

person01 = Person()

# отримуємо дані атрибуту
print(f"Name of person01: {getattr(person01, "name")}")
print(f"Hobby of person01: {getattr(person01, "hobby", "Not hobby")}")

# додаємо або змінюємо атрибути
setattr(person01, "age", 50)
setattr(person01, "hobby", "chess")
print(f"Age of person01: {getattr(person01, "age", "None")}")
print(f"Hobby of person01: {getattr(person01, "hobby", "Not hobby")}")

# перевіряємо, чи є такий атрибут
hasattr(person01, "last name")
print(f"Has person01 attr 'last name'? - {hasattr(person01, "last name")}")

# видалення атрибутів
del Person.age
print(Person.__dict__)
print(hasattr(Person, "age"))

delattr(Person, "high")
print(Person.__dict__)
print(hasattr(Person, "high"))

print(f"Doc: {Person.__doc__}")