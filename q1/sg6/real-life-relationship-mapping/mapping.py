class Course:
    def __init__(self, name: str):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Student:
    def __init__(self, name, student_id: int):
        self.name = name
        self.student_id = student_id

studentCourse = Course("ComSci")

student1 = Student("Martin", 6675)
student2 = Student("Juliska", 4349)

studentCourse.add_student(student1)
studentCourse.add_student(student2)

print(studentCourse.name)

for student in studentCourse.students:
    print(student.name, student.student_id)
