# Методи словника

# clear(): Видаляє всі пари ключ-значення з словника і робить його порожнім.
# my_dict = {'name': 'John', 'age': 30}
# my_dict.clear() # Зараз my_dict порожній словник {}

# copy(): Створює копію словника.
# original_dict = {'name': 'John', 'age': 30}
# new_dict = original_dict.copy() # Створить копію original_dict, яка буде присвоєна змінній new_dict

# get(key, default=None): Повертає значення, якщо ключ існує в словнику, 
# інакше повертає значення за замовчуванням (default, за замовчуванням None).
# age = my_dict.get('age') # Повертає 30
# country = my_dict.get('country', 'USA') # Повертає 'USA', оскільки ключ 'country' відсутній

# items(): Повертає усі пари ключ-значення словника у вигляді кортежів.
# my_dict = {'name': 'John', 'age': 30}
# items = my_dict.items() # Повертає [('name', 'John'), ('age', 30)]

# keys(): Повертає список усіх ключів у словнику.
# my_dict = {'name': 'John', 'age': 30}
# keys = my_dict.keys() # Повертає ['name', ‘age']

# values(): Повертає список усіх значень у словнику.
# my_dict = {'name': 'John', 'age': 30}
# values = my_dict.values() # Повертає ['John', 30]

# pop(key, default=None): Видаляє і повертає значення, що відповідає ключу. Якщо ключ не існує і вказано значення за замовчуванням, 
# то повертає значення за замовчуванням.
# age = my_dict.pop('age') # Видаляє ключ 'age' і повертає 30
# country = my_dict.pop('country', 'USA') # Не видаляє ключ 'country' і повертає ‘USA'

# update(iterable): Оновлює словник, додаючи пари ключ-значення із іншого ітерабельного об'єкту (зазвичай, іншого словника).
# my_dict = {'name': 'John', 'age': 30}
# my_dict.update({'city': 'New York', 'country': 'USA'}) # Оновлює словник з новими парами

user = {"name": "Mykhailo", "last name": "Hurak", "age": 33, "weight": 85, "high": 185}

print(user)
user.clear()
print(user)

user = {"name": "Mykhailo", "last name": "Hurak", "age": 33, "weight": 85, "high": 185}

copy_user = user.copy()
print(copy_user)

print(user.get("name"))
print(user.get("city", "None"))

user_items = user.items()
print(f"User items: {user_items}")

user_keys = user.keys()
print(f"User keys: {user_keys}")

user_values = user.values()
print(f"User values: {user_values}")

print(user.pop("name"))
print(user.pop("country", "None"))

print(user)
user.update({"country": "Ukraine"})
user.update({"city": "Kyiv", "hobby": "chess, fitness"})
print(user)
