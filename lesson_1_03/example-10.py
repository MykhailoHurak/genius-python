user_1 = {
    "name": "Michael",
    "role": "admin",
    "age": 33,
    "connection": True
}

user_2 = {
    "name": "Mykhailo",
    "role": "user",
    "age": 22,
    "connection": False
}

user_3 = {
    "name": "Mike",
    "role": "user",
    "age": 11,
    "connection": True
}

users_list = [user_1, user_2, user_3]

for user in users_list:
    if user["connection"]:
        print(f"Hello, {user["name"]}! You connected successful!")
        if user["age"] >= 18:
            print("Your access is Full")
        else:
            print("Your access is Limited")
    else:
        print(f"Sorry, {user["name"]}, You could not connect!")
        print("Please, try again!")