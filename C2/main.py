class Student:
    count = 0
    def __init__(self, def_name, def_age) -> None:
        print("Student created")
        self.name = def_name
        self.age = def_age
        Student.count += 1


    def hello(self):
        print("Hello", self.name)

    def __str__(self):
        return self.name
    
    @classmethod
    def description(cls):
        print("This is a class for students", cls.count)


student_1 = Student("John", 25)
student_1_name = student_1.name
student_1.hello()
print(dir(student_1))
print(id(student_1))
print(type(student_1))
print(student_1)
student_2 = Student("Jane", 22)
print("Count:", Student.count)

