# Словники

# Створення словника:
# Словник в Python - це колекція пар ключ-значення, де ключі унікальні та незмінні, а значення можуть бути будь-якого типу даних. Словники
# створюються за допомогою фігурних дужок {} або dict(), а пари ключ-значення розділяються двокрапкою.
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'} # Створення словника
# empty_dict = {} # Порожній словник

# Доступ до значень за ключем:
# Ви можете отримати доступ до значень в словнику, вказавши ключ у квадратних дужках або за допомогою методу .get().
# name = my_dct['name'] # Отримання значення за ключем 'name'
# age = my_dict.get('age') # Отримання значення за ключем 'age' за допомогою методу .get()

# Зміна значень за ключем:
# Значення в словнику можна змінювати, вказавши нове значення за існуючим ключем:
# my_dict['age'] = 31 # Зміна значення 'age' на 31

# Додавання нових пар ключ-значення:
# Для додавання нової пари ключ-значення просто вказуйте новий ключ та відповідне значення:
# my_dict['country'] = 'USA' # Додавання нового ключа 'country' зі значенням ‘USA'

# Видалення пар ключ-значення:
# Ви можете видалити пару ключ-значення за ключем за допомогою оператора del або методу .pop():
# del my_dict['city'] # Видалення ключа 'city' із словника
# country = my_dict.pop('country') # Видалення та отримання значення за ключем 'country'

user = {"name": "Mykhailo", "last name": "Hurak", "age": 33, "weight": 85, "high": 185}

# show values
print(user["name"])
print(user.get("name", "None name"))
print(user.get("city", "None city"))

# change values
print(f"Old weight: {user["weight"]}")
user["weight"] = 90
print(f"New weight: {user["weight"]}")

# add keys-values
user["city"] = "Kyiv"
user["country"] = "Ukraine"
print(user)

# delete keys-values
del user["age"]
print(user)
user.pop("last name")
print(user)