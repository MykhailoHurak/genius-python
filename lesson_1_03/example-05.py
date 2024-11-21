user_1 = {
    # "name": "Michael",
    "age": 21,
    "balance": 10000,
    "status": False
}

# user_2 = {
#     "name": "Mykhailo",
#     "age": 33,
#     "balance": 33500,
#     "status": True
# }

# user_3 = {
#     "name": "Mike",
#     "age": 15,
#     "balance": 18000,
#     "status": True
# }

if user_1.get("name", None) and user_1["age"] >= 18 and user_1["status"]:
    if user_1["balance"] > 0:
        print(f"Hello, {user_1['name']}! Nice to meet you!")
    else:
        print(f"Sorry, {user_1['name']}! Unfortunally your balance is emrty!)")
else:
    print("ERROR!")