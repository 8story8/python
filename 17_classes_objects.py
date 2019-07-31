class User:
    def __init__(self):
        print("Object initialized!")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_phone(self, phone):
        self.__phone = phone
    
    def get_phone(self):
        return self.__phone

    def __del__(self):
        print("Object destroyed!")

user = User()
user.set_name("Kiske")
user.set_phone("010-1111-1111")

print(user.get_name())
print(user.get_phone())

    