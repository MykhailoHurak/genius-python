num_1 = 100
num_2 = 10
num_3 = num_1 + num_2
print(num_3)

num_1 = 100
num_2 = 10
num_3 = num_1 - num_2
print(num_3)

num_1 = 100
num_2 = 10
num_3 = num_1 * num_2
print(num_3)

num_1 = 100
num_2 = 10
num_3 = num_1 / num_2
print(num_3)

num_1 = 7
num_2 = 2
num_3 = num_1 / num_2 # ділення звичайне
num_4 = num_1 // num_2 # ділення цілочисельне
print(num_3, num_4)

num_1 = 5
num_2 = 3
num_3 = num_1 ** num_2 # зведення до степені
print(num_3)

num_1 = 7
num_2 = 3
num_3 = num_1 % num_2 # залишок від ділення
print(num_3)

num_1 = 100
num_2 = 10
num_3 = num_1 == num_2
print(num_3)

num_1 = 100
num_2 = 10
num_3 = num_1 != num_2
print(num_3)

num_1 = 100
num_2 = 10
num_3 = num_1 > num_2
print(num_3)

num_1 = 100
num_2 = 10
num_3 = num_1 < num_2
print(num_3)

num = 100
name = 'Mike'
result = num > 10 and name == 'Mike'
print(result)

num = 100
name = 'Mike'
result = num < 10 or name == 'Mike'
print(result)

num = 100
name = 'Mike'
message = 'Mike got some money'
print(name in message)

num = 100
name = 'Mike'
message = 'Mike got some money'
print(name not in message)

age = 33
name = 'Mike'
animal = 'dog'
hobby = 'gym'
print(age == 33 and 'M' in name and animal != 'dog' or hobby == 'gym')

num_1 = 5
print(type(num_1))