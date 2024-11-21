def sayHello(username, age):
    print(f"Hello, {username}! Welcome to the club!")
    print(f"Your name is {age}")
    print("-------")

user_data = {"Mike": 33, "Mykhailo": 15, "Michael": 22}

for name, age in user_data.items():
    print(sayHello(name, age))