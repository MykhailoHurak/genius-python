# Кортежі

# Створення кортежу:
# Кортеж в Python - це колекція об'єктів, які мають фіксовану послідовність і не можуть бути змінені після створення. 
# Кортежі створюються, як і списки, за допомогою круглих дужок () або tuple(), і об'єкти в кортежі розділяються комами.
# my_tuple = (1, 2, 3, 4, 5) # Створення кортежу чисел
# fruits_tuple = ("apple", "banana", "cherry") # Створення кортежу рядків
# mixed_tuple = (1, "apple", True, 3.14) # Створення кортежу з різними типами даних
# single_item_tuple = (42,) # Створення кортежу з одним елементом

# Індексація кортежу:
# Елементи кортежу індексуються так само, як і елементи списку, починаючи з 0. Щоб отримати доступ до елемента за його індексом,
# використовуйте квадратні дужки і індекс:
# rst_element = my_tuple[0] # Отримання першого елемента кортежу
# second_element = my_tuple[1] # Отримання другого елемента кортежу

# Зрізи кортежів (slicing):
# Зрізи кортежів працюють аналогічно до списків. Ви можете отримати підписок кортежу, використовуючи синтаксис my_tuple[start:stop:step].
# subtuple = my_tuple[1:4] # Отримання підсписку з другого до четвертого елемента
# every_other = my_tuple[::2] # Отримання кожного другого елемента

# Кортежі є незмінними:
# Одна з основних різниць між кортежами і списками полягає в тому, що кортежі незмінні. 
# Це означає, що після створення кортежу ви не можете змінити його елементи. Наприклад, такий код призведе до помилки:
# my_tuple[0] = 10 # Помилка! Кортеж незмінний

names = ("Mykhailo", "Denys", "Volodymyr", "Ihor", "Andrii", "Petro", "Oleksii", "Maksym")

print(names[0])
print(names[3])
print(names[-1])

print(names[1:5:2])