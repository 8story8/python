x = lambda a : a + 10
print(x(10))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(1, 2, 3))

def get_my_function(num):
    return lambda a : a * num

doubler = get_my_function(2)
tripler = get_my_function(3)

print(doubler(100))
print(tripler(100))