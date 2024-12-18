# Списки

# Створення списку:
# Список в Python - це змінна, яка може містити інші об'єкти. Список створюється за допомогою квадратних
# дужок [] або функції list(), і об'єкти в списку розділяються комами.
# my_list = [1, 2, 3, 4, 5] # Створення списку чисел
# fruits = ["apple", "banana", "cherry"] # Створення списку рядків
# mixed_list = [1, "apple", True, 3.14] # Створення списку з різними типами даних
# empty_list = [] # Порожній список

# Індексація списку:
# Елементи списку індексуються, починаючи з 0 для першого елемента, 1 для другого і так далі. Щоб отримати
# доступ до елемента за його індексом, використовуйте квадратні дужки і індекс:
# rst_element = my_list[0] # Отримання першого елемента
# second_element = my_list[1] # Отримання другого елемента

# Зрізи списків (slicing):
# Зрізи дозволяють отримувати підсписки списку. Синтаксис для зрізів виглядає так: my_list[start : stop : step],
# де start - індекс початку зрізу, stop - індекс кінця зрізу (не включаючи його), step - крок.
# sublist = my_list[1:4] # Отримання підсписку з другого до четвертого елемента
# every_other = my_list[::2] # Отримання кожного другого елемента

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = ["Dynamo K", "Shakhtar D", "Rukh", "Karpaty", "Kryvbas", "LNZ", "Oleksandriia"]

print(f"Елемент перший: {a[0]}")
print(f"Елемент третій: {a[2]}")
print(f"Елемент останній: {a[-1]}")
print(f"Елемент перший: {b[0]}")
print(f"Елемент третій: {b[2]}")
print(f"Елемент останній: {b[-1]}")

print(a[:])
print(b[1::2])
print(a[3:4])

print(f"Перевернутий список: {a[::-1]}")
print(f"Перевернутий список: {b[::-1]}")