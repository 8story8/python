book_dict = {
    "name": "L",
    "author": "me",
    "year": 1923
}

print(book_dict)

x = book_dict["name"]
print(x)

x = book_dict.get("name")
print(x)

book_dict["year"] = 2019
print(book_dict)

for x in book_dict.values():
    print(x)

for x, y in book_dict.items():
    print(x, ":", y)

if "name" in book_dict:
    print("Yes, I am name!")

print(len(book_dict))

book_dict["edition"] = "limited"
print(book_dict)

book_dict.pop("edition")
print(book_dict)

book_dict.popitem()
print(book_dict)

# del book_dict["author"]
# print(book_dict)

# del book_dict
# print(book_dict)

# book_dict.clear()
# print(book_dict)

my_book_dict = book_dict.copy()
print(my_book_dict is book_dict) # False
print(my_book_dict == book_dict) # True

your_book_dict = dict(book_dict)
print(your_book_dict is book_dict) # False
print(your_book_dict == book_dict) # True

my_book_dict = dict(name="L", author="me", year="2019")
print(my_book_dict)