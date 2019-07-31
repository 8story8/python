fruit_set = {"apple", "banana", "cherry", "123"}

print(len(fruit_set))

fruit_set.remove("123")
print(fruit_set)

fruit_set.discard("123")
print(fruit_set)

x = fruit_set.pop()

print(x)
print(fruit_set)

fruit_set.clear()
print(fruit_set)

# del fruit_set
# print(fruit_set)

fruit_set = set(("apple", "banana", "cherry"))
print(fruit_set)