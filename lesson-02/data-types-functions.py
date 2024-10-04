num_1 = '33'
print(num_1)
print(type(num_1))
num_1 = int(num_1) #перетворення в ціле число
print(num_1)
print(type(num_1))
num_1 = float(num_1) #перетворення в число з крапкою
print(num_1)
print(type(num_1))

message = 'my name is Michael!'
print(len(message)) #кількість символів, довжина рядка
message = message.upper() # верхній регістр
print(message)
message = message.lower() # нижній регістр
print(message)
message = message.capitalize() # перше слово з великої літери
print(message)
message = message.replace('!', '.') # заміна символа
print(message)
message = message.split() # розбиття рядка
print(message)
message = ' '.join(message) # з'єднання рядка
print(message)
message = message.count('m') # підрахунок к-сті заданих символів
print(message)
message = 33
message = str(message) # перетворення в тип рядка
print(type(message))

list_test = [1, 2, 3]
print(len(list_test))
list_test.append(4) # додавання в кінець
print(list_test)
list_test.extend([5, 6, 7, 8]) # розширення в кінець
print(list_test)
print(list_test.index(7)) # визначення номеру індекса

dict_test = {'name': 'Mykhailo', 'age': 33, 'high': 185}
print(dict_test.keys()) # всі ключі 
print(dict_test.values()) # всі значення
print(dict_test.items()) # всі пари ключ-значення
print(dict_test['name'], dict_test['age'])
print(dict_test.get('hobby', 'No'))