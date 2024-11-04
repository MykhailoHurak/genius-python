def printNumbers(start, finish):
    for number in range(start, finish):
        print(f"Current number is: {number}")

list_of_ranges = [(1, 7), (3, 10), (5, 9)]

for start, finish in list_of_ranges:
    printNumbers(start, finish)
    print("-------")