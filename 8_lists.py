fruit_list = ["apple", "banana", "cherry"]

print(fruit_list)
print(fruit_list[0])

fruit_list[0] = "berry"
print(fruit_list[0])

for x in fruit_list:
    print(x)

if "apple" in fruit_list:
    print("Yes, I am apple!")

print(len(fruit_list))

fruit_list.append("orange")
print(fruit_list)

fruit_list.insert(0, "tomato")
print(fruit_list)

fruit_list.remove("tomato")
print(fruit_list)

fruit_list.pop()
print(fruit_list)

del fruit_list[0]
print(fruit_list)

# fruit_list.clear()
# print(fruit_list)

# del fruit_list
# print(fruit_list)

my_fruit_list = fruit_list.copy()
print(my_fruit_list)

your_fruit_list = list(fruit_list)
print(your_fruit_list)

fruit_list = list(("apple", "banana", "cherry"))
print(fruit_list)

