# Методи кортежу

# Кортежі не мають багатьох методів порівняно із списками, оскільки вони
# незмінні. Однак вони підтримують тільки два методи: .count() і .index():

# .count(item): Повертає кількість входжень item у кортеж.
# .index(item): Повертає індекс першого входження item у кортеж.

# count = my_tuple.count(3) # Підрахунок кількості трійок у кортежі
# index = my_tuple.index(4) # Знаходження індексу першої четвірки

fruits = ("orange", "banana", "apple", "banana", "banana", "apple")

print(f"Apple: {fruits.count("apple")}")
print(f"Banana: {fruits.count("banana")}")
print(f"Orange: {fruits.count("orange")}")

print(f"Index of Banana: {fruits.index("banana")}")
print(f"Index of Orange: {fruits.index("orange")}")