a = 300
b = 500
c = 700

if b > a:
    print("b is greater than a!")
elif a == b:
    print("a and b are equal!")
else:
    print("a is greater than b!")

print("b is greater than a!") if b > a else print("a and b are equal!") if a == b else print("a is greater than b!")

if a < b and b < c:
    print("Both conditions are true!")

if a < b or b > c:
    print("At least one of the conditions is true!")