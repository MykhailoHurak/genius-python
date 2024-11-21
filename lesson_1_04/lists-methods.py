# Методи списків

# .append(item): Додає item в кінець списку.
# .insert(index, item): Вставляє item на певний index.
# .remove(item): Видаляє перше входження item зі списку.
# .pop(): Видаляє і повертає останній елемент списку (або з певного індексу, якщо передати індекс).
# .index(item): Повертає індекс першого входження item у списку.
# .count(item): Повертає кількість входжень item у списку.
# .sort(): Сортує список за зростанням.
# .reverse(): Розвертає список в зворотньому порядку

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 3, 3]
countries = ["Ukraine", "USA", "Spain", "Italy", "Argentina", "Romania", "Germany", "Portugal", "Brazil"]

numbers.append(11)
print(numbers)

numbers.insert(3, 777)
print(numbers)

numbers.remove(777)
print(numbers)

numbers.pop()
print(numbers)

print(countries.index("Italy"))

print(numbers.count(3))

numbers.sort(reverse=True) # сортування з кінця
print(numbers)

countries.sort() 
print(countries)

countries.reverse()
print(countries)