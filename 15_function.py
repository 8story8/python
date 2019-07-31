import random

def set_name(name):
    print("My name is", name)

set_name("Kiske")

def set_country(country = "Korea"):
    print("My country is", country)

set_country()
set_country("Sweden")

def set_fruit_list(fruit_list):
    for x in fruit_list:
        print(x)


fruit_list = ["apple", "banana", "cherry"]

set_fruit_list(fruit_list)

def get_my_random_num(x):
    return random.randrange(1, x)

print(get_my_random_num(7))

def get_factorial(num):
    if num == 2 or num == 1:
        return num
    else:
        return num * get_factorial(num-1)

print(get_factorial(4))
    
