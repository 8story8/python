x = 3
y = 2.5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 7
print(x) # 7

x += 3
print(x) # 10

x -=  3
print(x) # 7

x *= 3
print(x) # 21

x /= 3
print(x) # 7

x %= 3
print(x) # 1

y = 256
y //= 4
print(y) # 64

y **= 2
print(y) # 4096

y &= 2
print(y) # 0

y |= 2
print(y) # 2

y ^= 2
print(y) # 0

y >>= 2 
print(y) # 0

y <<= 2
print(y) # 0

x = 10
y = 20

print(x == y) # False
print(x != y) # True
print(x > y) # False
print(x < y) # True
print(x >= y) # False
print(x <= y) # True

print(x < 10 and y < 20) # False
print(x < 10 or y >= 20) # True
print(not(x < 10 or y >= 20)) # False

x = ["teacher", "student"]
y = ["teacher", "student"]
z = x

print(x is z) # True
print(x is y) # False
print(x == y) # True
print(x is not y) # True
print("teacher" in x) # True
print("teacher" not in x) # False
