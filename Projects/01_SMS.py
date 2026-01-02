class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def basic_info(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.__marks = marks   

    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
            print("Marks updated successfully")
        else:
            print("Negative marks not allowed")

    def get_marks(self):
        return self.__marks

    def result_show(self):
        if self.__marks >= 33:
            print("Result : PASS")
        else:
            print("Result : FAIL")

    def student_info(self):
        self.basic_info()
        print(f"Roll No : {self.roll_no}")
        print(f"Marks   : {self.__marks}")
        self.result_show()
        print("-" * 30)


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.__salary = salary   

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print("Salary updated successfully")
        else:
            print("Invalid salary")

    def get_salary(self):
        return self.__salary

    def teacher_info(self):
        self.basic_info()
        print(f"Subject : {self.subject}")
        print(f"Salary  : {self.__salary}")
        print("-" * 30)


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_all_students(self):
        print("\n===== STUDENT DETAILS =====")
        for student in self.students:
            student.student_info()

    def show_all_teachers(self):
        print("\n===== TEACHER DETAILS =====")
        for teacher in self.teachers:
            teacher.teacher_info()


school = School("Parul University")

s1 = Student("Kanji", 23, 101, 88)
s2 = Student("Amit", 22, 102, 30)

t1 = Teacher("Yash", 35, "Maths", 20000)
t2 = Teacher("Rahul", 40, "Science", 25000)

school.add_student(s1)
school.add_student(s2)
school.add_teacher(t1)
school.add_teacher(t2)

school.show_all_students()
school.show_all_teachers()