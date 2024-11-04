def checkConnection(username, count_tries, priority):
    if priority >= 10:
        finish = 5
        for attempt in range(1, count_tries + 1):
            if attempt == finish:
                print("Connect was successful")
                break
            print(f"Attempt: {attempt} connect to {username}")

    elif priority > 5 and priority < 10:
        finish = 3
        for attempt in range(1, 6):
            if attempt == finish:
                print("Connect was successful")
                break
            print(f"Attempt: {attempt} connect to {username}")

    else:
        print(f"Your {username} has so low priority")

checkConnection(username = "Mike", count_tries = 10, priority = 111)