import random

x = 1 # int
y = 7.7 # float
z = 1j # complex

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 900000000000000000000
z = -9000000

print(type(x))
print(type(y))
print(type(z))

x = 7.70
y = 7.0
z = -7.77

print(type(x))
print(type(y))
print(type(z))

x = 77e7
y = 7E7
z = -7.7e100

print(type(x))
print(type(y))
print(type(z))

x = 7+7j
y = 7j
z = -7j
print(type(x))
print(type(y))
print(type(z))

x = 1 # int
y = 2.3 # float
z = 4j # complex

# convert from int to float
a = float(x)

# convert from float to int
b = int(y)

# convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print(random.randrange(1,10))



