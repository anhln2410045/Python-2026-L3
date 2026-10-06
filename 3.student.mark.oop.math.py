import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.gpa = 0.0

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def __str__(self):
        return f"{self.__id}-{self.__name}-{self.__dob}|GPA:{self.gpa:.1f}"

class Course:
    def __init__(self, course_id, name, credits):
        self.__id = course_id
        self.__name = name
        self.credits = credits
        self.__marks = {}

    def get_id(self):
        return self.__id

    def add_mark(self, student_id, mark):
        rounded_mark = math.floor(mark * 10) / 10
        self.__marks[student_id] = rounded_mark

    def get_mark(self, student_id):
        return self.__marks.get(student_id, 0.0)

    def show_marks(self, students):
        print(f"Marks for course {self.__id}")
        for s in students:
            print(f"{s.get_name()}: {self.__marks.get(s.get_id(), 'N/A')}")

class SchoolManager:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def add_student(self):
        n = int(input("How many students?"))
        for _ in range(n):
            sid = input("ID:")
            name = input("Name:")
            dob = input("DoB:")
            self.__students.append(Student(sid, name, dob))

    def add_course(self):
        n = int(input("How many courses?"))
        for _ in range(n):
            cid = input("Course ID:")
            name = input("Course Name:")
            credits = int(input("Credits:"))
            self.__courses.append(Course(cid, name, credits))

    def input_marks(self):
        cid = input("Enter Course ID to input marks:")
        course = next((c for c in self.__courses if c.get_id() == cid), None)
        if course:
            for s in self.__students:
                m = float(input(f"Mark for {s.get_name()}:"))
                course.add_mark(s.get_id(), m)
        else:
            print("Course not found")

    def list_students(self):
        for s in self.__students: print(s)

    def list_courses(self):
        for c in self.__courses: print(c)

    def show_marks(self):
        cid = input("Enter Course ID:")
        course = next((c for c in self.__courses if c.get_id() == cid), None)
        if course: course.show_marks(self.__students)
        else: print("Course not found")

    def calculate_gpa_and_sort(self):
        for s in self.__students:
            marks = [c.get_mark(s.get_id()) for c in self.__courses]
            credits = [c.credits for c in self.__courses]
            if sum(credits) > 0:
                s.gpa = np.average(marks, weights=credits)

        self.__students.sort(key=lambda x: x.gpa, reverse=True)
        print("Student List sorted by GPA")
        for s in self.__students:
            print(s)

manager = SchoolManager()
while True:
    print("MENU")
    print("1. Add Students\n2. Add Courses\n3. Input Marks\n4. List Students\n5. List Courses\n6. Show Marks\n7. GPA Calculation & Sort")
    choice = input("Selection:")
    if choice == '1': manager.add_student()
    elif choice == '2': manager.add_course()
    elif choice == '3': manager.input_marks()
    elif choice == '4': manager.list_students()
    elif choice == '5': manager.list_courses()
    elif choice == '6': manager.show_marks()
    elif choice == '7': manager.calculate_gpa_and_sort()
    else: break