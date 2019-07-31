class User:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone
        print("User object initialized!")

    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def __del__(self):
        print("User object destroyed!")

class Student(User):
    def __init__(self, school, name, phone):
        User.__init__(self, name, phone)
        self.__school = school
        print("Student object initialized!")

    def get_school(self):
        return self.__school

    def get_student_infomation(self):
        return "School : " + self.get_school() + ", Name : " + self.get_name() + ", Phone : " + self.get_phone()
    
    def __del__(self):
        print("User del overrided!")
        print("Student object destroyed!")

student = Student("Cornell", "Kiske", "010-1111-1111")

print(student.get_school())
print(student.get_name())
print(student.get_phone())
print(student.get_student_infomation())

