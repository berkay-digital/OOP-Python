class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, grades) -> None:
        super().__init__(name, age)
        self.grades = grades

class Professor(Person):
    def __init__(self, name, age, students) -> None:
        super().__init__(name, age)
        self.students = students

new_student = Student("John", 20, [90, 80, 70])
new_student2 = Student("Example", 20, [90, 80, 70])
new_professor = Professor("Jane", 30, [new_student, new_student2])
print(new_student.name, new_student.age, new_student.grades)
print(new_professor.name, new_professor.age, new_professor.students[0].name, new_professor.students[0].age, new_professor.students[0].grades)


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
class Parent(Person):
    def __init__(self, name, age, children) -> None:
        super().__init__(name, age)
        self.children = children

class Father(Parent):
    def __init__(self, name, age, children, job) -> None:
        super().__init__(name, age, children)
        self.job = job
    
father = Father("John", 40, ["John Jr", "Jane"], "Engineer")
print(father.name, father.age, father.children, father.job)

