fruit_list = ["apple", "banana", "cherry", "mango"]
book_list = ["L", "K", "P", "T"]

for x in fruit_list:
    if x == "apple":
        continue
    elif x == "cherry":
        break
    else:
        print(x)

for x in range(7):
    print(x)

for x in range(1,7):
    print(x)

for x in range(1, 30, 3):
    print(x)

for x in fruit_list:
    for y in book_list:
        print(x, ":", y)