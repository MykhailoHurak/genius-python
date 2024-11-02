a = 0
add_list = []

while len(add_list) < 20:
    print("Length of the list: ", len(add_list))
    add_list.append(a)
    a += 1
    if len(add_list) == 10:
        print("You are in middle of the list")