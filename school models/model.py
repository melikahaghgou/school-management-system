import json

from colorama import Fore


class Course:
    def __init__(self, id: int, name: str, units: int):
        self.id = id
        self.name = name
        self.units = units
        self.scores = 0.0

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.units}"

    def __eq__(self, other):
        if isinstance(other, Course):
            return self.id == other.id
        return self.id == other

    def edit_info(self, new_name: str, new_units: int):
        self.name = new_name
        self.units = new_units


class Student:
    def __init__(self, id: int, name: str, family: str):
        self.id = id
        self.name = name
        self.family = family
        self.courses: list[Course] = []

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.id == other.id
        return self.id == other

    def info(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"family: {self.family}")

        for course in self.courses:
            print(f"{course.id}\t{course.name}\t{course.scores}")

    def edit_info(self, new_name: str, new_family: str):
        self.name = new_name
        self.family = new_family


class Teacher:
    def __init__(self, id: int, name: str, family: str):
        self.id = id
        self.name = name
        self.family = family
        self.courses: list[Course] = []

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}"

    def __eq__(self, other):
        if isinstance(other, Teacher):
            return self.id == other.id
        return self.id == other

    def info(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"family: {self.family}")

        for course in self.courses:
            print(f"{course.id}\t{course.name}")

    def edit_info(self, new_name: str, new_family: str):
        self.name = new_name
        self.family = new_family


class Classroom:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.students: list[Student] = []
        self.teacher: Teacher | None = None
        self.course: Course | None = None

    def __str__(self):
        return f"{self.id}\t{self.name}"

    def __eq__(self, other):
        if isinstance(other, Classroom):
            return self.id == other.id
        return self.id == other

    def info(self):
        print(f"classroom id: {self.id}")
        print(f"classroom name: {self.name}")

        if self.teacher:
            print(f"teacher: {self.teacher.id}\t{self.teacher.name} {self.teacher.family}")
        else:
            print("teacher: None")

        if self.course:
            print(f"course: {self.course.id}\t{self.course.name} ({self.course.units} Units)")
        else:
            print("course: None")

        print("students:")
        if not self.students:
            print(Fore.RED + "empty.")
        else:
            for student in self.students:
                print(f"    {student.id}\t{student.name} {student.family}")

    def change_classroom_course(self, new_course: Course):
        self.course = new_course

        if self.teacher and new_course not in self.teacher.courses:
            self.teacher = None
            print(Fore.RED + "teacher removed because they do not teach this course")

        self.students = [
            student for student in self.students
            if new_course in student.courses
        ]

        print(Fore.GREEN + "course changed")

    def change_classroom_teacher(self, new_teacher: Teacher):
        if self.course not in new_teacher.courses:
            print(Fore.YELLOW + "this teacher does not teach this course")
            return

        self.teacher = new_teacher
        print(Fore.GREEN + "teacher changed")

    def add_student_to_classroom(self, student: Student):
        if student in self.students:
            print(Fore.YELLOW + "student already in classroom")
            return

        self.students.append(student)
        print(Fore.GREEN + "student added")

    def remove_student_from_classroom(self, student: Student):
        if student in self.students:
            self.students.remove(student)
            print(Fore.RED + "student removed")
        else:
            print(Fore.RED + "student not found")


class School:
    def __init__(self, name: str):
        self.name = name
        self.courses: list[Course] = []
        self.students: list[Student] = []
        self.teachers: list[Teacher] = []
        self.classrooms: list[Classroom] = []

        self.selected_student: Student | None = None
        self.selected_teacher: Teacher | None = None
        self.selected_course: Course | None = None
        self.selected_classroom: Classroom | None = None

    def find_course(self, course_id: int) -> Course | None:
        for course in self.courses:
            if course.id == course_id:
                return course
        return None

    def find_student(self, student_id: int) -> Student | None:
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def find_teacher(self, teacher_id: int) -> Teacher | None:
        for teacher in self.teachers:
            if teacher.id == teacher_id:
                return teacher
        return None

    def find_classroom(self, classroom_id: int) -> Classroom | None:
        for classroom in self.classrooms:
            if classroom.id == classroom_id:
                return classroom
        return None

    def add_student(self, student: Student) -> bool:
        if self.find_student(student.id):
            print(Fore.YELLOW + "this student id already exists.")
            return False

        self.students.append(student)
        return True

    def remove_student(self, student_id: int):
        student = self.find_student(student_id)

        if not student:
            print(Fore.RED + "student not found")
            return

        for classroom in self.classrooms:
            if student in classroom.students:
                print(Fore.YELLOW + "student is in a classroom, cannot delete")
                return

        self.students.remove(student)
        print(Fore.RED + "student deleted")

    def add_course(self, course: Course) -> bool:
        if self.find_course(course.id):
            print(Fore.YELLOW + "this course id already exists.")
            return False

        self.courses.append(course)
        return True

    def remove_course(self, course_id: int):
        course = self.find_course(course_id)

        if not course:
            print(Fore.RED + "course not found")
            return

        for classroom in self.classrooms:
            if classroom.course == course:
                print(Fore.YELLOW + "course is in classroom")
                return

        self.courses.remove(course)
        print(Fore.RED + "course deleted")

    def add_teacher(self, teacher: Teacher) -> bool:
        if self.find_teacher(teacher.id):
            print(Fore.YELLOW + "this teacher id already exists.")
            return False

        self.teachers.append(teacher)
        return True

    def remove_teacher(self, teacher_id: int):
        teacher = self.find_teacher(teacher_id)

        if not teacher:
            print(Fore.RED + "teacher not found")
            return

        for classroom in self.classrooms:
            if classroom.teacher == teacher:
                print(Fore.YELLOW + "teacher is in a classroom, cannot delete")
                return

        self.teachers.remove(teacher)
        print(Fore.RED + "teacher deleted")

    def remove_classroom(self, classroom_id: int):
        classroom = self.find_classroom(classroom_id)

        if not classroom:
            print(Fore.RED + "classroom not found")
            return

        self.classrooms.remove(classroom)
        print(Fore.RED + "classroom deleted")

    def save_data(self):
        data = {
            "students": [],
            "courses": [],
            "teachers": [],
            "classrooms": []
        }

        for course in self.courses:
            data["courses"].append({
                "id": course.id,
                "name": course.name,
                "units": course.units
            })

        for student in self.students:
            data["students"].append({
                "id": student.id,
                "name": student.name,
                "family": student.family,
                "courses": [
                    [course.id, course.scores]
                    for course in student.courses
                ]
            })

        for teacher in self.teachers:
            data["teachers"].append({
                "id": teacher.id,
                "name": teacher.name,
                "family": teacher.family,
                "courses": [
                    course.id for course in teacher.courses
                ]
            })

        for classroom in self.classrooms:
            data["classrooms"].append({
                "id": classroom.id,
                "name": classroom.name,
                "course": classroom.course.id if classroom.course else None,
                "teacher": classroom.teacher.id if classroom.teacher else None,
                "students": [
                    student.id for student in classroom.students
                ]
            })

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data["courses"]:
            self.courses.append(Course(
                item["id"],
                item["name"],
                item["units"]
            ))

        for item in data["teachers"]:
            teacher = Teacher(
                item["id"],
                item["name"],
                item["family"]
            )

            for course_id in item["courses"]:
                course = self.find_course(course_id)

                if course:
                    teacher.courses.append(course)

            self.teachers.append(teacher)

        for item in data["students"]:
            student = Student(
                item["id"],
                item["name"],
                item["family"]
            )

            for course_id, score in item["courses"]:
                course = self.find_course(course_id)

                if course:
                    student_course = Course(
                        course.id,
                        course.name,
                        course.units
                    )
                    student_course.scores = score
                    student.courses.append(student_course)

            self.students.append(student)

        for item in data["classrooms"]:
            classroom = Classroom(
                item["id"],
                item["name"]
            )

            if item["course"] is not None:
                classroom.course = self.find_course(item["course"])

            if item["teacher"] is not None:
                classroom.teacher = self.find_teacher(item["teacher"])

            for student_id in item["students"]:
                student = self.find_student(student_id)

                if student:
                    classroom.students.append(student)

            self.classrooms.append(classroom)