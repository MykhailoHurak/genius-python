a = 10
b = 20
c = "chat is active"
d = "count of users"

print("length c: ", len(c))
print("length d: ", len(d))

if a > len(c) and a < b:
    print("Condition 1 is True")
elif len(c) == len(d):
    print("Condition 2 is True")
else:
    print("ERROR! Wrong conditions")