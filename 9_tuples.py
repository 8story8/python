fruit_tuple = ("apple", "banana", "cherry")
print(fruit_tuple)
print(fruit_tuple[0])

for x in fruit_tuple:
    print(x)

if "apple" in fruit_tuple:
    print("Yes, I am apple!")

print(len(fruit_tuple))

# del fruit_tuple
# print(fruit_tuple)

fruit_tuple = tuple(("apple", "banana", "cherry"))
print(fruit_tuple)