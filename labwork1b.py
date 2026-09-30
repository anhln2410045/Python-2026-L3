class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

students = []
courses = []
marks = {}

def add_student():
    print("Adding Students")
    n = int(input("How many students?"))
    for i in range(n):
        print(f"Student {i+1}:")
        student_id = input("ID:")
        name = input("Name:")
        dob = input("Date of Birth:")
        students.append(Student(student_id, name, dob))

def add_course():
    print("Adding Courses")
    n = int(input("How many courses?"))
    for i in range(n):
        course_id = input("Course ID:")
        course_name = input("Course Name:")
        courses.append(Course(course_id, course_name))
        marks[course_id] = {}

def input_marks():
    course_id = input("Enter Course ID to input marks:")
    if course_id not in marks:
        print("Course ID not found")
        return
    print(f"Input marks for course:{course_id}")
    for s in students:
        m = float(input(f"Mark for {s.name}({s.id}):"))
        marks[course_id][s.id] = m

def list_students():
    print("List of students:")
    for s in students:
        print(f"{s.id}-{s.name}-{s.dob}")

def list_courses():
    print("List of courses:")
    for c in courses:
        print(f"{c.id}-{c.name}")

def show_marks():
    course_id = input("Which course marks you want to see?")
    if course_id in marks:
        print(f"Marks for {course_id}:")
        for s in students:
            mark = marks[course_id].get(s.id,"None")
            print(f"{s.name}:{mark}")
    else:
        print("Course not found")

while True:
    print("1. Add Students\n2. Add Courses\n3. Input Marks\n4. List Students\n5. List Courses\n6. Show Marks")
    i = input("Your selection:")
    if i == '1': add_student()
    elif i == '2': add_course()
    elif i == '3': input_marks()
    elif i == '4': list_students()
    elif i == '5': list_courses()
    elif i == '6': show_marks()
    else: print("Try again")