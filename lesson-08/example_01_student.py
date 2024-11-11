class Student:
    def __init__(self, name, age) -> None:
        self._name = name # Захищений атрибут
        self._age = age # Захищений атрибут

    # Публічний метод для отримання імені
    def get_name(self):
        return self._name

    # Публічний метод для зміни імені
    def set_name(self, name):
        self._name = name

# Створення об'єкта класу Student
student = Student("Mykhailo", 18)

# Отримання імені за допомогою публічного методу
print(student.get_name()) # Mykhailo

# Зміна імені за допомогою публічного методу
student.set_name("Michael")
print(student.get_name()) # Michael

# Прямий доступ до захищених атрибутів (не рекомендується)
student._name = "Mike"
print(student.get_name()) # Mike