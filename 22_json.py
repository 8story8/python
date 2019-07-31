import json

x = '{ "name":"Kiske", "age":27, "country":"Korea"}'

y = json.loads(x)

print(y["name"])

x = {
    "name": "Kiske",
    "age": 27,
    "country": "Korea"
}

y = json.dumps(x)

print(y)

print(json.dumps({"name": "Kiske", "age": 27}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("Hello"))
print(json.dumps(77))
print(json.dumps(77.77))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
    "name": "Kiske",
    "age": 27,
    "country": "Korea",
    "car": [
        {"model": "Porsche", "price": 30},
        {"model": "BMW", "price": 20}
    ]
}

print(json.dumps(x))
print(json.dumps(x, indent=2, separators=(". ", " = "), sort_keys=True))
