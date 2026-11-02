import json
import os
from colorama import Fore, Back, Style, init

# Initialize colorama with automatic style reset
init(autoreset=True)


class Course:
    """Represents a school course with an id, name, and unit count."""

    id: int = 0
    name: str = ""
    units: int = 0
    scores: float = 0

    def __init__(self, id: int, name: str, units: int):
        """Create a new course instance.

        :param id: Unique course identifier.
        :param name: Course name.
        :param units: Number of units for the course.
        """
        self.id = id
        self.name = name
        self.units = units
        self.scores: float = 0.0

    def __str__(self):
        """Return a readable string representation for printing."""
        return f"{self.id}\t{self.name}\t{self.units}"

    def __eq__(self, other):
        """Compare courses by id.

        :param other: Another Course object or an id value.
        """
        if isinstance(other, Course):
            return self.id == other.id
        elif isinstance(other, int):
            return self.id == other
        return False

    def edit_info(self, new_name: str, new_units: int) -> None:
        """Update the course name and units.

        :param new_name: New course name.
        :param new_units: New number of units.
        """
        self.name = new_name
        self.units = new_units


class Student:
    """Represents a student and the courses they are enrolled in."""

    id: int = 0
    name: str = ""
    family: str = ""
    courses: list[Course]

    def __init__(self, id: int, name: str, family: str):
        """Create a new student instance.

        :param id: Unique student identifier.
        :param name: Student first name.
        :param family: Student last name.
        """
        self.id = id
        self.name = name
        self.family = family
        self.courses = []

    def __str__(self):
        """Return a readable string representation for printing."""
        return f"{self.id}\t{self.name}\t{self.family}"

    def __eq__(self, other):
        """Compare students by id.

        :param other: Another Student object or an integer id.
        """
        if isinstance(other, Student):
            return self.id == other.id
        elif isinstance(other, int):
            return self.id == other
        return False

    def info(self) -> None:
        """Print detailed student information, including enrolled courses."""
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"family: {self.family}")
        if not self.courses:
            print(Fore.YELLOW + "courses: None")
        for c in self.courses:
            print(f"{c.id}\t{c.name}\t{c.scores}")

    def edit_info(self, new_name: str, new_family: str) -> None:
        """Update the student's name and family name.

        :param new_name: New first name.
        :param new_family: New last name.
        """
        self.name = new_name
        self.family = new_family


class Teacher:
    """Represents a teacher and the courses they can teach."""

    id: int = 0
    name: str = ""
    family: str = ""
    courses: list[Course]

    def __init__(self, id: int, name: str, family: str):
        """Create a new teacher instance.

        :param id: Unique teacher identifier.
        :param name: Teacher first name.
        :param family: Teacher last name.
        """
        self.id = id
        self.name = name
        self.family = family
        self.courses = []

    def __str__(self):
        """Return a readable string representation for printing."""
        return f"{self.id}\t{self.name}\t{self.family}"

    def __eq__(self, other):
        """Compare teachers by id.

        :param other: Another Teacher object or an integer id.
        """
        if isinstance(other, Teacher):
            return self.id == other.id
        elif isinstance(other, int):
            return self.id == other
        return False

    def info(self) -> None:
        """Print detailed teacher information, including assigned courses."""
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"family: {self.family}")
        if not self.courses:
            print(Fore.YELLOW + "courses: None")
        for c in self.courses:
            print(f"{c.id}\t{c.name}\t{c.units} Units")

    def edit_info(self, new_name: str, new_family: str) -> None:
        """Update the teacher's name and family name.

        :param new_name: New first name.
        :param new_family: New last name.
        """
        self.name = new_name
        self.family = new_family


class Classroom:
    """Represents a classroom, its assigned course, teacher, and students."""

    id: int = 0
    name: str = ""
    teacher: Teacher = None
    course: Course = None

    def __init__(self, id: int, name: str):
        """Create a new classroom instance.

        :param id: Unique classroom identifier.
        :param name: Classroom name.
        """
        self.id = id
        self.name = name
        self.students: list[Student] = []
        self.teacher = None
        self.course = None
        self.selected_classroom: Classroom = None

    def info(self) -> None:
        """Print complete classroom information."""
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
            for s in self.students:
                print(f"    {s.id}\t{s.name} {s.family}")

    def __eq__(self, other):
        """Compare classrooms by id.

        :param other: Another Classroom object or an integer id.
        """
        if isinstance(other, Classroom):
            return self.id == other.id
        elif isinstance(other, int):
            return self.id == other
        return False

    def change_classroom_course(self, new_course: Course) -> None:
        """Change the classroom course and keep only matching students.

        :param new_course: The new course to assign to the classroom.
        """
        self.course = new_course
        if self.teacher and new_course not in self.teacher.courses:
            self.teacher = None
            print(Fore.YELLOW + "None")
        new_student = []
        for s in self.students:
            if new_course in s.courses:
                new_student.append(s)
        self.students = new_student
        print(Fore.GREEN + "course changed")

    def change_classroom_teacher(self, new_teacher: Teacher) -> None:
        """Assign a new teacher to the classroom if the teacher can teach the course.

        :param new_teacher: Teacher to assign.
        """
        if not self.course:
            print(Fore.RED + "classroom has no course assigned yet")
            return
        if self.course not in new_teacher.courses:
            print(Fore.YELLOW + "this teacher doesnt teach this course")
            return
        self.teacher = new_teacher
        print(Fore.GREEN + "teacher changed")

    def add_student_to_classroom(self, student: Student) -> None:
        """Add a student to the classroom if they are not already present.

        :param student: Student to add.
        """
        if student in self.students:
            print(Fore.YELLOW + "student already in classroom")
            return
        self.students.append(student)
        print(Fore.GREEN + "student added")

    def remove_student_from_classroom(self, student: Student) -> None:
        """Remove a student from the classroom.

        :param student: Student object to remove.
        """
        if student in self.students:
            self.students.remove(student)
            print(Fore.GREEN + "student removed")
        else:
            print(Fore.RED + "student not found")


class School:
    """Main container class that stores courses, students, teachers, and classrooms."""

    name: str = ""
    courses: list[Course] = []
    students: list[Student] = []
    teachers: list[Teacher] = []
    classrooms: list[Classroom] = []
    selected_students: Student = None

    def __init__(self, name: str):
        """Create a school object with empty collections.

        :param name: School name.
        """
        self.name = name
        self.courses = []
        self.students = []
        self.teachers = []
        self.classrooms = []
        self.selected_students: Student = None
        self.selected_teachers: Teacher = None
        self.selected_courses: Course = None
        self.selected_classroom: Classroom = None

    def print_students(self) -> None:
        """Print a short list of all students."""
        if not self.students:
            print(Fore.YELLOW + "No students found.")
            return
        for s in self.students:
            print(f"ID: {s.id} | Name: {s.name} {s.family} | Courses: {s.courses}")

    def print_classrooms(self):
        """Print a short list of all classrooms."""
        if not self.classrooms:
            print(Fore.YELLOW + "No classrooms found.")
            return
        for cl in self.classrooms:
            print(f"{cl.id}\t{cl.name}")

    def remove_classroom(self, id: int):
        """Remove a classroom by id.

        :param id: Classroom id to remove.
        """
        search_classroom = Classroom(id, "")
        if search_classroom not in self.classrooms:
            print(Fore.RED + "classroom not found")
            return
        self.classrooms.remove(search_classroom)
        print(Fore.GREEN + "classroom deleted")

    def add_student(self, student: Student) -> bool:
        """Add a student if the id is not already used.

        :param student: Student object to add.
        :return: True if added, False if duplicate id exists.
        """
        for st in self.students:
            if st.id == student.id:
                print(Fore.YELLOW + "this student id already exists.")
                return False
        self.students.append(student)
        print(Fore.GREEN + "student added")
        return True

    def edit_student(self, student: Student) -> None:
        """Replace an existing student object with an updated one.

        :param student: Updated student object.
        """
        if student in self.students:
            i = self.students.index(student)
            self.students[i] = student
            print(Fore.GREEN + "student updated")
        else:
            print(Fore.RED + "student not found")

    def remove_student(self, id: int) -> None:
        """Remove a student by id if the student is not assigned to a classroom.

        :param id: Student id to remove.
        """
        search_student = Student(id, "", "")
        if search_student not in self.students:
            print(Fore.RED + "student not found")
            return
        for cl in self.classrooms:
            if search_student in cl.students:
                print(Fore.YELLOW + "student is in a classroom, cannot delete")
                return
        self.students.remove(search_student)
        print(Fore.GREEN + "student deleted")

    def print_courses(self) -> None:
        """Print a short list of all courses."""
        if not self.courses:
            print(Fore.YELLOW + "No courses found.")
            return
        for c in self.courses:
            print(f"ID: {c.id} | Name: {c.name} | Units: {c.units}")

    def add_course(self, course: Course) -> bool:
        """Add a course if the id is not already used.

        :param course: Course object to add.
        :return: True if added, False if duplicate id exists.
        """
        for c in self.courses:
            if c.id == course.id:
                print(Fore.YELLOW + "course id already exists")
                return False
        self.courses.append(course)
        print(Fore.GREEN + "course added")
        return True

    def edit_course(self, course: Course) -> None:
        """Replace an existing course object with an updated one.

        :param course: Updated course object.
        """
        if course in self.courses:
            i = self.courses.index(course)
            self.courses[i] = course
            print(Fore.GREEN + "course updated")
        else:
            print(Fore.RED + "course not found")

    def remove_course(self, id: int) -> None:
        """Remove a course by id if it is not assigned to any classroom.

        :param id: Course id to remove.
        """
        search_course = Course(id, "", 0)
        if search_course not in self.courses:
            print(Fore.RED + "course not found")
            return
        for cl in self.classrooms:
            if cl.course == search_course:
                print(Fore.YELLOW + "course is in classroom")
                return
        self.courses.remove(search_course)
        print(Fore.GREEN + "course deleted")

    def print_teachers(self) -> None:
        """Print a short list of all teachers."""
        if not self.teachers:
            print(Fore.YELLOW + "No teachers found.")
            return
        for t in self.teachers:
            print(f"ID: {t.id} | Name: {t.name} {t.family} | Courses: {t.courses}")

    def add_teacher(self, teacher: Teacher) -> bool:
        """Add a teacher if the id is not already used.

        :param teacher: Teacher object to add.
        :return: True if added, False if duplicate id exists.
        """
        for t in self.teachers:
            if t.id == teacher.id:
                print(Fore.YELLOW + "this teacher id already exists.")
                return False
        self.teachers.append(teacher)
        print(Fore.GREEN + "teacher added")
        return True

    def edit_teacher(self, teacher: Teacher) -> None:
        """Replace an existing teacher object with an updated one.

        :param teacher: Updated teacher object.
        """
        if teacher in self.teachers:
            i = self.teachers.index(teacher)
            self.teachers[i] = teacher
            print(Fore.GREEN + "teacher updated")
        else:
            print(Fore.RED + "teacher not found")

    def remove_teacher(self, id: int) -> None:
        """Remove a teacher by id if possible.

        :param id: Teacher id to remove.
        """
        search_teacher = Teacher(id, "", "")
        if search_teacher not in self.teachers:
            print(Fore.RED + "teacher not found")
            return
        for cl in self.classrooms:
            if cl.teacher and cl.teacher.id == id:
                print(Fore.YELLOW + "teacher is in a classroom, cannot delete")
                return
        self.teachers.remove(search_teacher)
        print(Fore.GREEN + "teacher deleted")

    def load_data(self):
        """Load school data from the JSON file into memory."""
        if not os.path.exists("01.json"):
            return
        try:
            with open("01.json", "rt", encoding="utf-8") as file:
                data = json.load(file)

            for c in data.get("courses", []):
                self.courses.append(Course(c["id"], c["name"], c["units"]))

            for t in data.get("teachers", []):
                tea = Teacher(t["id"], t["name"], t["family"])
                for cid in t.get("courses", []):
                    search_c = Course(cid, "", 0)
                    if search_c in self.courses:
                        idx = self.courses.index(search_c)
                        base = self.courses[idx]
                        new_c = Course(base.id, base.name, base.units)
                        tea.courses.append(new_c)
                self.teachers.append(tea)

            for s in data.get("students", []):
                stu = Student(s["id"], s["name"], s["family"])
                for item in s.get("courses", []):
                    cid = item[0]
                    score = item[1]
                    search_c = Course(cid, "", 0)
                    if search_c in self.courses:
                        idx = self.courses.index(search_c)
                        base = self.courses[idx]
                        new_c = Course(base.id, base.name, base.units)
                        new_c.scores = score
                        stu.courses.append(new_c)
                self.students.append(stu)

            for cl in data.get("classrooms", []):
                classroom = Classroom(cl["id"], cl["name"])
                cid = cl.get("course")
                if cid is not None:
                    search_c = Course(cid, "", 0)
                    if search_c in self.courses:
                        classroom.course = self.courses[self.courses.index(search_c)]

                tid = cl.get("teacher")
                if tid is not None:
                    search_t = Teacher(tid, "", "")
                    if search_t in self.teachers:
                        classroom.teacher = self.teachers[self.teachers.index(search_t)]

                for sid in cl.get("students", []):
                    search_s = Student(sid, "", "")
                    if search_s in self.students:
                        classroom.students.append(self.students[self.students.index(search_s)])

                self.classrooms.append(classroom)
        except Exception as e:
            print(Fore.RED + f"Error loading data: {e}")

    def save_data(self):
        """Save all current school data into the JSON file."""
        data = {
            "students": [],
            "courses": [],
            "teachers": [],
            "classrooms": []
        }

        for c in self.courses:
            data["courses"].append({
                "id": c.id,
                "name": c.name,
                "units": c.units
            })

        for s in self.students:
            student_courses = []
            for c in s.courses:
                student_courses.append([c.id, c.scores])
            data["students"].append({
                "id": s.id,
                "name": s.name,
                "family": s.family,
                "courses": student_courses
            })

        for t in self.teachers:
            teacher_courses = []
            for c in t.courses:
                teacher_courses.append(c.id)
            data["teachers"].append({
                "id": t.id,
                "name": t.name,
                "family": t.family,
                "courses": teacher_courses
            })

        for cl in self.classrooms:
            classroom_students = []
            for s in cl.students:
                classroom_students.append(s.id)
            data["classrooms"].append({
                "id": cl.id,
                "name": cl.name,
                "course": cl.course.id if cl.course else None,
                "teacher": cl.teacher.id if cl.teacher else None,
                "students": classroom_students
            })

        with open("01.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(Fore.GREEN + "Data saved successfully to 01.json")


# ----------------------------
# Main application loop
# ----------------------------

level = "root"
sc1 = School("sama")
sc1.load_data()

while True:
    if level == "root":
        print(Fore.CYAN + Style.BRIGHT + "\n========== SCHOOL MANAGEMENT SYSTEM ==========")
        print(Fore.WHITE + "1- students")
        print(Fore.WHITE + "2- teachers")
        print(Fore.WHITE + "3- courses")
        print(Fore.WHITE + "4- classrooms")
        print(Fore.GREEN + "5- save")
        print(Fore.RED + "0- exit")
        cmd = int(input(Fore.CYAN + ">>: "))
        if cmd == 1:
            level = "students"
        elif cmd == 2:
            level = "teachers"
        elif cmd == 3:
            level = "courses"
        elif cmd == 4:
            level = "classrooms"
        elif cmd == 5:
            sc1.save_data()
        elif cmd == 0:
            break

    elif level == "students":
        print(Fore.GREEN + Style.BRIGHT + "\n========== STUDENTS MENU ==========")
        print(Fore.WHITE + "1- show students")
        print(Fore.WHITE + "2- add student")
        print(Fore.WHITE + "3- edit student")
        print(Fore.WHITE + "4- delete student")
        print(Fore.WHITE + "5- select student")
        print(Fore.RED + "0- back")
        cmd = int(input(Fore.CYAN + ">>: "))
        if cmd == 1:
            sc1.print_students()
        elif cmd == 2:
            while True:
                id = int(input(Fore.CYAN + "id: "))
                if Student(id, "", "") in sc1.students:
                    print(Fore.RED + "id exists")
                else:
                    break

            name = input(Fore.CYAN + "name: ")
            family = input(Fore.CYAN + "family: ")
            sc1.add_student(Student(id, name, family))
        elif cmd == 3:
            sid = int(input(Fore.CYAN + "enter student id to edit: "))
            search_s = Student(sid, "", "")
            if search_s in sc1.students:
                idx = sc1.students.index(search_s)
                target_student = sc1.students[idx]

                new_name = input(Fore.CYAN + "new name: ")
                new_family = input(Fore.CYAN + "new family: ")
                target_student.edit_info(new_name, new_family)
            else:
                print(Fore.RED + "student not found")
        elif cmd == 4:
            id = int(input(Fore.CYAN + "id: "))
            sc1.remove_student(id)

        elif cmd == 5:
            sc1.print_students()
            id = int(input(Fore.CYAN + "id: "))
            search_st = Student(id, "", "")
            if search_st in sc1.students:
                idx = sc1.students.index(search_st)
                sc1.selected_students = sc1.students[idx]
                level = "students_select"
            else:
                print(Fore.RED + "students not found")

        elif cmd == 0:
            level = "root"

    elif level == "students_select":
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "========== STUDENT PANEL ==========")
        print(Fore.WHITE + "1- info")
        print(Fore.WHITE + "2- show courses")
        print(Fore.WHITE + "3- add course")
        print(Fore.WHITE + "4- delete course")
        print(Fore.WHITE + "5- set score")
        print(Fore.BLUE + "0- back")

        cmd = int(input(Fore.CYAN + ">>: "))
        if cmd == 1:
            sc1.selected_students.info()

        elif cmd == 2:
            if not sc1.selected_students.courses:
                print(Fore.YELLOW + "No courses assigned.")
            for c in sc1.selected_students.courses:
                print(f"{c.id}\t{c.name}\t{c.scores}")

        elif cmd == 3:
            for c in sc1.courses:
                if c not in sc1.selected_students.courses:
                    print(c)
            cid = int(input(Fore.CYAN + "course id: "))
            search_course = Course(cid, "", 0)
            if search_course not in sc1.selected_students.courses:
                target = sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_students.courses.append(target)
                print(Fore.GREEN + "course added")

        elif cmd == 4:
            for c in sc1.selected_students.courses:
                print(c)
            cid = int(input(Fore.CYAN + "course id: "))
            search_course = Course(cid, "", 0)
            if search_course in sc1.selected_students.courses:
                target = sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_students.courses.remove(target)
                print(Fore.GREEN + "course removed")

        elif cmd == 5:
            for c in sc1.selected_students.courses:
                print(f"{c.id}\t{c.name}\t{c.scores}")

            cid = int(input(Fore.CYAN + "Course ID: "))
            search_course = Course(cid, "", 0)

            if search_course in sc1.selected_students.courses:
                idx = sc1.selected_students.courses.index(search_course)
                new_score = float(input(Fore.CYAN + "score: "))
                sc1.selected_students.courses[idx].scores = new_score
                print(Fore.GREEN + "score updated")

        elif cmd == 0:
            level = "students"

    elif level == "teachers":
        print(Fore.YELLOW + Style.BRIGHT + "\n========== TEACHERS MENU ==========")
        print(Fore.WHITE + "1- show teachers")
        print(Fore.WHITE + "2- add teacher")
        print(Fore.WHITE + "3- edit teacher")
        print(Fore.WHITE + "4- delete teacher")
        print(Fore.WHITE + "5- select teacher")
        print(Fore.BLUE + "0- back")
        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            sc1.print_teachers()
        elif cmd == 2:
            while True:
                id = int(input(Fore.CYAN + "id: "))
                if Teacher(id, "", "") in sc1.teachers:
                    print(Fore.RED + "id exists")
                else:
                    break

            name = input(Fore.CYAN + "name: ")
            family = input(Fore.CYAN + "family: ")
            sc1.add_teacher(Teacher(id, name, family))

        elif cmd == 3:
            tid = int(input(Fore.CYAN + "enter teacher id to edit: "))
            search_t = Teacher(tid, "", "")
            if search_t in sc1.teachers:
                idx = sc1.teachers.index(search_t)
                target_teacher = sc1.teachers[idx]

                new_name = input(Fore.CYAN + "new name: ")
                new_family = input(Fore.CYAN + "new family: ")
                target_teacher.edit_info(new_name, new_family)
            else:
                print(Fore.RED + "teacher not found")

        elif cmd == 4:
            id = int(input(Fore.CYAN + "id: "))
            sc1.remove_teacher(id)

        elif cmd == 5:
            sc1.print_teachers()
            id = int(input(Fore.CYAN + "id: "))
            search_tc = Teacher(id, "", "")
            if search_tc in sc1.teachers:
                idx = sc1.teachers.index(search_tc)
                sc1.selected_teachers = sc1.teachers[idx]
                level = "teachers_select"
            else:
                print(Fore.RED + "teacher not found")

        elif cmd == 0:
            level = "root"

    elif level == "teachers_select":
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "========== TEACHER PANEL ==========")
        print(Fore.WHITE + "1- info")
        print(Fore.WHITE + "2- show courses")
        print(Fore.WHITE + "3- add course")
        print(Fore.WHITE + "4- delete course")
        print(Fore.WHITE + "5- set score")
        print(Fore.BLUE + "0- back")

        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            sc1.selected_teachers.info()

        elif cmd == 2:
            if not sc1.selected_teachers.courses:
                print(Fore.YELLOW + "No courses assigned.")
            for c in sc1.selected_teachers.courses:
                print(c)

        elif cmd == 3:
            for c in sc1.courses:
                if c not in sc1.selected_teachers.courses:
                    print(c)

            cid = int(input(Fore.CYAN + "course id: "))
            search_course = Course(cid, "", 0)

            if search_course not in sc1.selected_teachers.courses:
                target = sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_teachers.courses.append(target)
                print(Fore.GREEN + "course added")

        elif cmd == 4:
            for c in sc1.selected_teachers.courses:
                print(c)

            cid = int(input(Fore.CYAN + "course id: "))
            search_course = Course(cid, "", 0)

            if search_course in sc1.selected_teachers.courses:
                target = sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_teachers.courses.remove(target)
                print(Fore.GREEN + "course removed")

        elif cmd == 5:
            for c in sc1.selected_teachers.courses:
                print(f"{c.id}\t{c.name}\t{c.scores}")

            cid = int(input(Fore.CYAN + "Course ID: "))
            search_course = Course(cid, "", 0)

            if search_course in sc1.selected_teachers.courses:
                idx = sc1.selected_teachers.courses.index(search_course)
                new_score = float(input(Fore.CYAN + "score: "))
                sc1.selected_teachers.courses[idx].scores = new_score
                print(Fore.GREEN + "score updated")

        elif cmd == 0:
            level = "teachers"

    elif level == "courses":
        print(Fore.MAGENTA + Style.BRIGHT + "\n========== COURSES MENU ==========")
        print(Fore.WHITE + "1- show courses")
        print(Fore.WHITE + "2- add course")
        print(Fore.WHITE + "3- edit course")
        print(Fore.WHITE + "4- delete course")
        print(Fore.WHITE + "5- select course")
        print(Fore.BLUE + "0- back")
        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            sc1.print_courses()
        elif cmd == 2:
            while True:
                id = int(input(Fore.CYAN + "id: "))
                if Course(id, "", 0) in sc1.courses:
                    print(Fore.RED + "id exists")
                else:
                    break

            name = input(Fore.CYAN + "name: ")
            units = int(input(Fore.CYAN + "units: "))
            sc1.add_course(Course(id, name, units))

        elif cmd == 3:
            cid = int(input(Fore.CYAN + "enter course id to edit: "))
            search_c = Course(cid, "", 0)
            if search_c in sc1.courses:
                idx = sc1.courses.index(search_c)
                target_course = sc1.courses[idx]

                new_name = input(Fore.CYAN + "enter new name: ")
                new_units = int(input(Fore.CYAN + "enter new units: "))
                target_course.edit_info(new_name, new_units)
                print(Fore.GREEN + "course updated")
            else:
                print(Fore.RED + "course not found")

        elif cmd == 4:
            id = int(input(Fore.CYAN + "id: "))
            sc1.remove_course(id)

        elif cmd == 5:
            pass

        elif cmd == 0:
            level = "root"

    elif level == "classrooms":
        print(Fore.BLUE + Style.BRIGHT + "\n========== CLASSROOMS MENU ==========")
        print(Fore.WHITE + "1- show classrooms")
        print(Fore.WHITE + "2- add classroom")
        print(Fore.WHITE + "3- edit classroom")
        print(Fore.WHITE + "4- delete classroom")
        print(Fore.WHITE + "5- select classroom")
        print(Fore.BLUE + "0- back")
        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            sc1.print_classrooms()

        elif cmd == 2:
            id = int(input(Fore.CYAN + "classroom id: "))
            name = input(Fore.CYAN + "classroom name: ")
            classroom = Classroom(id, name)

            print("select course: ")
            sc1.print_courses()
            cid = int(input(Fore.CYAN + "course id: "))
            search_course = Course(cid, "", 0)

            if search_course in sc1.courses:
                classroom.course = sc1.courses[sc1.courses.index(search_course)]

                print("available teachers: ")
                available_teachers = []
                for t in sc1.teachers:
                    if search_course in t.courses:
                        print(t)
                        available_teachers.append(t)

                if available_teachers:
                    tid = int(input(Fore.CYAN + "teacher id: "))
                    search_teacher = Teacher(tid, "", "")
                    if search_teacher in available_teachers:
                        classroom.teacher = available_teachers[available_teachers.index(search_teacher)]
                    else:
                        print(Fore.RED + "teacher not found in available list")
                else:
                    print(Fore.YELLOW + "no teacher available for this course")

            print("students with score under 10:")
            if classroom.course:
                for s in sc1.students:
                    for c in s.courses:
                        if c.id == classroom.course.id and c.scores < 10:
                            print(s)

            while True:
                sid = int(input(Fore.CYAN + "students id (0 to finish): "))
                if sid == 0:
                    break
                search_s = Student(sid, "", "")
                if search_s in sc1.students:
                    idx = sc1.students.index(search_s)
                    student = sc1.students[idx]
                    if student not in classroom.students:
                        classroom.students.append(student)
                else:
                    print(Fore.RED + "student not found")

            sc1.classrooms.append(classroom)
            print(Fore.GREEN + "classroom added")

        elif cmd == 3:
            id = int(input(Fore.CYAN + "id: "))
            found = False
            for cl in sc1.classrooms:
                if cl.id == id:
                    new_name = input(Fore.CYAN + "new name: ")
                    cl.name = new_name
                    print(Fore.GREEN + f"new name: {new_name}")
                    found = True
                    break
            if not found:
                print(Fore.RED + "classroom not found")

        elif cmd == 4:
            id = int(input(Fore.CYAN + "id: "))
            sc1.remove_classroom(id)

        elif cmd == 5:
            sc1.print_classrooms()
            id = int(input(Fore.CYAN + "classroom id: "))
            search_cl = Classroom(id, "")
            if search_cl in sc1.classrooms:
                idx = sc1.classrooms.index(search_cl)
                sc1.selected_classroom = sc1.classrooms[idx]
                level = "classrooms_select"
            else:
                print(Fore.RED + "classroom not found")

        elif cmd == 0:
            level = "root"

    elif level == "classrooms_select":
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "========== CLASSROOM PANEL ==========")
        print(Fore.WHITE + "1- show info")
        print("2- change courses")
        print("3- change teacher")
        print("4- add student")
        print("5- remove student")
        print(Fore.BLUE + "0- back")
        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            sc1.selected_classroom.info()

        elif cmd == 2:
            sc1.print_courses()
            cid = int(input(Fore.CYAN + "Enter new course id: "))
            search_course = Course(cid, "", 0)
            if search_course in sc1.courses:
                target_course = sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_classroom.change_classroom_course(target_course)
            else:
                print(Fore.RED + "Course not found.")

        elif cmd == 3:
            if not sc1.selected_classroom.course:
                print(Fore.RED + "classroom has no course set")
            else:
                print("available teachers:")
                available_teachers = []
                for t in sc1.teachers:
                    if sc1.selected_classroom.course in t.courses:
                        print(t)
                        available_teachers.append(t)

                if not available_teachers:
                    print(Fore.RED + "no teacher available for this course")
                else:
                    tid = int(input(Fore.CYAN + "teacher id: "))
                    search_teacher = Teacher(tid, "", "")
                    if search_teacher in available_teachers:
                        idx = available_teachers.index(search_teacher)
                        target_teacher = available_teachers[idx]
                        sc1.selected_classroom.change_classroom_teacher(target_teacher)
                    else:
                        print(Fore.RED + "teacher not found")

        elif cmd == 4:
            if not sc1.selected_classroom.course:
                print(Fore.RED + "classroom has no course set")
            else:
                print("students with score under 10:")
                available_students = []
                for s in sc1.students:
                    if s not in sc1.selected_classroom.students:
                        for c in s.courses:
                            if c.id == sc1.selected_classroom.course.id and c.scores < 10:
                                print(s)
                                available_students.append(s)
                                break

                if not available_students:
                    print(Fore.RED + "no student available")
                else:
                    sid = int(input(Fore.CYAN + "student id: "))
                    search_student = Student(sid, "", "")
                    if search_student in available_students:
                        student = available_students[available_students.index(search_student)]
                        sc1.selected_classroom.add_student_to_classroom(student)
                    else:
                        print(Fore.RED + "student not found")

        elif cmd == 5:
            print("students in this classroom: ")
            for s in sc1.selected_classroom.students:
                print(s)
            sid = int(input(Fore.CYAN + "student id: "))
            search_student = Student(sid, "", "")
            if search_student in sc1.selected_classroom.students:
                student = sc1.selected_classroom.students[
                    sc1.selected_classroom.students.index(search_student)
                ]
                sc1.selected_classroom.remove_student_from_classroom(student)
            else:
                print(Fore.RED + "student not found")

        elif cmd == 0:
            level = "classrooms"
