fruit_tuple = ("apple", "banana", "cherry")
fruit_iter = iter(fruit_tuple)

print(next(fruit_iter))
print(next(fruit_iter))
print(next(fruit_iter))

string = "string"
string_iter = iter(string)

print(next(string_iter))
print(next(string_iter))
print(next(string_iter))
print(next(string_iter))
print(next(string_iter))
print(next(string_iter))

class Number:
    def __init__(self):
        self.__num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__num <= 7:
            next = self.__num
            self.__num += 1
            return next
        else:
            raise StopIteration

number = Number()
number_iter = iter(number)

# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))

# for x in number_iter:
#    print(x)
