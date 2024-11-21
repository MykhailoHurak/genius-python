num_1 = 5
print(type(num_1))

num_2 = 3.14
print(type(num_2))

string_test = 'Hello'
print(type(string_test))

check_test = True
print(type(check_test))

list_test_1 = [3, 6, 1, 12, 5]
list_test_2 = ['hello', 'my', 'name', 'is', 'Michael']
print(type(list_test_1))
print(type(list_test_2))

tuple_test = (1, 2, 3, 4, 5)
print(type(tuple_test))

dict_test = {'name': 'Mike', 'age': 33, 'high': 185}
print(type(dict_test))

set_test = {1, 2, 3, 4, 5}
print(type(set_test))

print(type(None))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dct = {'name': 'Mike', 'age': 10, 'high': 185}
tpl = ('m', 'g', 'i', 'a')
name_1 = 'Mike'
name_2 = 'Michael'
result = dct['age'] in lst and dct['name'] in tpl
print(result)
print(dct['name'] == name_1 and dct['age'] in lst)