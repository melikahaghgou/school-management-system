import json
class Course:
    """
    Represents a course in the school system.

    Attributes:
        id (int): unique id of the course.
        name (str): name of the course.
        units (int): number of units of the course.
        scores (float): score related to this course for a student.
    """
    id: int = 0
    name: str = ""
    units: int = 0
    scores: float = 0

    def __init__(self, id: int, name: str, units: int):
        """
        Initialize a Course object.

        :param id: course id
        :param name: course name
        :param units: number of units for the course
        """
        self.id = id
        self.name = name
        self.units = units

    def __str__(self):
        """
        Return a string representation of the course.

        :return: course id, name, and units as a formatted string
        """
        return f"{self.id}\t{self.name}\t{self.units}"

    def __eq__(self, other):
        """
        Compare two courses by id.

        :param other: another course or an id to compare with
        :return: True if ids are equal, otherwise False
        """
        if isinstance(other, Course):
            return self.id == other.id
        return self.id == other

    def edit_info(self, new_name: str, new_units: int) -> None:
        """
        Update the course information.

        :param new_name: new course name
        :param new_units: new number of units
        """
        self.name = new_name
        self.units = new_units


class Student:
    """
    Represents a student in the school system.

    Attributes:
        id (int): unique id of the student.
        name (str): first name of the student.
        family (str): last name of the student.
        courses (list[Course]): list of courses taken by the student.
    """
    id: int = 0
    name: str = ""
    family: str = ""
    courses: list[Course]

    def __init__(self, id: int, name: str, family: str):
        """
        Initialize a Student object.

        :param id: student id
        :param name: student first name
        :param family: student last name
        """
        self.id = id
        self.name = name
        self.family = family
        self.courses = []

    def __str__(self):
        """
        Return a string representation of the student.

        :return: student id, name, and family as a formatted string
        """
        return f"{self.id}\t{self.name}\t{self.family}"

    def __eq__(self, other):
        """
        Compare two students by id.

        :param other: another student object to compare with
        :return: True if student ids are equal, otherwise False
        """
        return (self.id == other.id)
    
    def info(self) -> None:
        """
        Print student details and their registered courses with scores.
        """
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"family: {self.family}")
        for c in self.courses:
            print(f"{c.id}\t{c.name}\t{c.scores}")
    
    def edit_info(self, new_name: str, new_family: str) -> None:
        """
        Update the student information.

        :param new_name: new first name of the student
        :param new_family: new last name of the student
        """
        self.name = new_name
        self.family = new_family

class Teacher:
    """
    Represents a teacher in the school system.

    Attributes:
        id (int): unique id of the teacher.
        name (str): first name of the teacher.
        family (str): last name of the teacher.
        courses (list[Course]): list of courses taught by the teacher.
    """
    id: int = 0
    name: str = ""
    family: str = ""
    courses: list[Course]

    def __init__(self, id: int, name: str, family: str):
        """
        Initialize a Teacher object.

        :param id: teacher id
        :param name: teacher first name
        :param family: teacher last name
        """
        self.id = id
        self.name = name
        self.family = family
        self.courses = []

    def __str__(self):
        """
        Return a string representation of the teacher.

        :return: teacher id, name, and family as a formatted string
        """
        return f"{self.id}\t{self.name}\t{self.family}"

    def __eq__(self, other):
        """
        Compare two teachers by id.

        :param other: another teacher object or an id to compare with
        :return: True if teacher ids are equal, otherwise False
        """
        return (self.id == other.id)
    
    def info(self) -> None:
        """
        Print teacher details and the courses they teach.
        """
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"family: {self.family}")
        for c in self.courses:
            print(f"{c.id}\t{c.name}\t{c.scores}")
    def edit_info(self, new_name: str, new_family: str) -> None:
        """
        Update the teacher information.

        :param new_name: new first name of the teacher
        :param new_family: new last name of the teacher
        """
        self.name = new_name
        self.family = new_family

class Classroom:
    """
    Represents a classroom in the school system.

    Attributes:
        id (int): unique id of the classroom.
        name (str): name or code of the classroom.
        teacher (Teacher | None): teacher assigned to this classroom.
        course (Course | None): course taught in this classroom.
        students (list[Student]): list of students registered in this classroom.
    """
    id: int = 0
    name: str = ""
    teacher: Teacher=None
    course: Course=None


    def __init__(self, id: int,name: str):
        """
        Initialize a Classroom object.

        :param id: classroom id
        :param name: classroom name or room number
        """
        self.id = id
        self.name = name
        self.students: list[Student] = []
        self.teacher = None
        self.course = None
        self.selected_classroom: Classroom = None

    def info(self) -> None:
        """
        Print detailed information of the classroom, including the teacher,
        the course, and the list of registered students.
        """
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
            print("empty.")
        else:
            for s in self.students:
                print(f"    {s.id}\t{s.name} {s.family}")
    def __eq__(self, other):
        """
        Compare two classrooms by ID.

        :param other: Another Classroom object or an integer ID
        :return: True if IDs match, False otherwise
        """
        if isinstance(other, Classroom):
            return self.id == other.id
        return self.id == other
    def change_classroom_course(self, new_course: Course) -> None:
        """
        Change the course taught in the classroom.
        If the current teacher doesn't teach this new course, the teacher is set to None.
        Only students who have registered for this new course will remain in the classroom.

        :param new_course: The new Course object to set
        """
        self.course = new_course
        if self.teacher and new_course not in self.teacher.courses:
            self.teacher = None
            print("None")
        new_student=[]
        for s in self.students:
            if new_course in s.courses:
                new_student.append(s)
        self.students=new_student
        print("course changed")

    def change_classroom_teacher(self, new_teacher:Teacher)->None:
        """
        Change the classroom teacher if they teach the classroom's course.

        :param new_teacher: The new Teacher object to assign
        """
        if self.course not in new_teacher.courses:
            print("this teacher doesnt teach this course")
            return
        self.teacher=new_teacher
        print("teacher changed")
    def add_student_to_classroom(self, student: Student) -> None:
        """
        Add a student to the classroom.

        :param student: The Student object to add
        """
        if student in self.students:
            print("student already in classroom")
            return
        self.students.append(student)
        print("student added")

    def remove_student_from_classroom(self, student: Student) -> None:
        """
        Remove a student from the classroom.

        :param student: The Student object to remove
        """
        if student in self.students:
            self.students.remove(student)
            print("student removed")
        else:
            print("student not found")



class School:
    """
    Represents the whole school system.

    Attributes:
        name (str): name of the school.
        courses (list[Course]): list of all courses in the school.
        students (list[Student]): list of all students in the school.
        teachers (list[Teacher]): list of all teachers in the school.
        classrooms (list[Classroom]): list of all classrooms in the school.
        selected_students (Student | None): currently selected student.
        selected_teachers (Teacher | None): currently selected teacher.
        selected_courses (Course | None): currently selected course.
        selected_classroom (Classroom | None): currently selected classroom.
    """
    name: str = ""
    courses: list[Course] = []
    students: list[Student] = []
    teachers: list[Teacher] = []
    classrooms: list[Classroom] = []
    selected_students: Student = None

    def __init__(self, name: str):
        """
        Initialize a School object.

        :param name: school name
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
        """
        Print all students in the school.
        """
        for s in self.students:
            print(f"ID: {s.id} | Name: {s.name} {s.family} | Courses: {s.courses}")

    def print_classrooms(self):
        """
        Print all classrooms in the school.
        """
        for cl in self.classrooms:
            print(f"{cl.id}\t{cl.name}")

    def remove_classroom(self, id: int):
        """
        Remove a classroom by its id.

        :param id: classroom id to remove
        """
        search_classroom = Classroom(id, None)
        if search_classroom not in self.classrooms:
            print("classroom not found")
            return
        self.classrooms.remove(search_classroom)
        print("classroom deleted")

    def add_student(self, student: Student) -> None:
        """
        Add a new student to the school if the id is unique.

        :param student: student object to add
        :return: True if added successfully, otherwise False
        """
        for st in self.students:
            if st.id == student.id:
                print("this student id already exists.")
                return False
        self.students.append(student)
        return True

    def edit_student(self, student: Student) -> None:
        """
        Replace an existing student with updated data.

        :param student: updated student object
        """
        if student in self.students:
            i = self.students.index(student)
            self.students[i] = student
            print("student updated")
        else:
            print("student not found")

    def remove_student(self, id: int) -> None:
        """
        Remove a student by id if the student is not assigned to any classroom.

        :param id: student id to remove
        """
        search_student = Student(id, "", "")
        if search_student not in self.students:
            print("student not found")
            return
        for cl in self.classrooms:
            if search_student in cl.students:
                print("student is in a classroom, cannot delete")
                return
        self.students.remove(search_student)

    def print_courses(self) -> None:
        """
        Print all courses in the school.
        """
        for c in self.courses:
            print(f"ID: {c.id} | Name: {c.name} | Units: {c.units}")

    def add_course(self, course: Course) -> None:
        """
        Add a new course to the school if the id is unique.

        :param course: course object to add
        :return: True if added successfully, otherwise False
        """
        for c in self.courses:
            if c.id == course.id:
                return False
        self.courses.append(course)
        return True

    def edit_course(self, course: Course) -> None:
        """
        Replace an existing course with updated data.

        :param course: updated course object
        """
        if course in self.courses:
            i = self.courses.index(course)
            self.courses[i] = course
            print("course updated")
        else:
            print("course not found")

    def remove_course(self, id: int) -> None:
        """
        Remove a course by id if it is not assigned to any classroom.

        :param id: course id to remove
        """
        search_course = Course(id, "", 0)
        if search_course not in self.courses:
            print("course not found")
            return
        for cl in self.classrooms:
            if cl.course == search_course:
                print("course is in classroom")
                return
        self.courses.remove(search_course)
        print("course deleted")

    def print_teachers(self) -> None:
        """
        Print all teachers in the school.
        """
        for t in self.teachers:
            print(f"ID: {t.id} | Name: {t.name} {t.family} | Courses: {t.courses}")

    def add_teacher(self, teacher: Teacher) -> None:
        """
        Add a new teacher to the school if the id is unique.

        :param teacher: teacher object to add
        :return: True if added successfully, otherwise False
        """
        for t in self.teachers:
            if t.id == teacher.id:
                print("this teacher id already exists.")
                return False
        self.teachers.append(teacher)
        return True

    def edit_teacher(self, teacher: Teacher) -> None:
        """
        Replace an existing teacher with updated data.

        :param teacher: updated teacher object
        """
        if teacher in self.teachers:
            i = self.teachers.index(teacher)
            self.teachers[i] = teacher
            print("teacher updated")
        else:
            print("teacher not found")

    def remove_teacher(self, id: int) -> None:
        """
        Remove a teacher by id if the teacher is not assigned to any classroom.

        :param id: teacher id to remove
        """
        search_teacher = Teacher(id, "", "")
        if search_teacher not in self.teachers:
            print("teacher not found")
            return
        for cl in self.classrooms:
            if search_teacher == search_teacher:
                print("teacher is in a classroom, cannot delete")
                return
        self.teachers.remove(search_teacher)

    def load_data(self):
        """
        Load school data from the JSON file and rebuild all objects.
        """
        file = open("01.json", "rt")
        f = file.read()
        data = json.loads(f)
        file.close()

        for c in data["courses"]:
            self.courses.append(Course(c["id"], c["name"], c["units"]))

        for t in data["teachers"]:
            tea = Teacher(t["id"], t["name"], t["family"])

            for cid in t["courses"]:
                if cid in self.courses:
                    idx = self.courses.index(cid)
                    base = self.courses[idx]

                    new_c = Course(base.id, base.name, base.units)
                    tea.courses.append(new_c)

            self.teachers.append(tea)

        for s in data["students"]:
            stu = Student(s["id"], s["name"], s["family"])

            for item in s["courses"]:
                cid = item[0]
                score = item[1]

                if cid in self.courses:
                    idx = self.courses.index(cid)
                    base = self.courses[idx]
                    new_c = Course(base.id, base.name, base.units)
                    new_c.scores = score
                    stu.courses.append(new_c)

            self.students.append(stu)

        for cl in data["classrooms"]:
            classroom = Classroom(cl["id"], cl["name"])
            cid = cl["course"]
            if cid in self.courses:
                idx = self.courses.index(cid)
                classroom.course = self.courses[idx]

            tid = cl["teacher"]

            if tid is not None:
                search_t = Teacher(tid, "", "")
                if search_t in self.teachers:
                    idx = self.teachers.index(search_t)
                    classroom.teacher = self.teachers[idx]
            else:
                classroom.teacher = None

            for sid in cl["students"]:
                search_s = Student(sid, "", "")
                if search_s in self.students:
                    idx = self.students.index(search_s)
                    classroom.students.append(self.students[idx])

            self.classrooms.append(classroom)

    def save_data(self):
        """
        Save all school data to the JSON file.
        """
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

        file = open("01.json", "w")
        json.dump(data, file)
        file.close()



level = "root"
sc1 = School("sama")
sc1.load_data()

while True:
    if level == "root":
        print("1- students")
        print("2- teachers")
        print("3- courses")
        print("4- classrooms")
        print("5- save")
        print("0- exit")
        cmd = int(input(">>: "))
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
        print("1- show students")
        print("2- add student")
        print("3- edit student")
        print("4- delete student")
        print("5- select student")
        print("0- back")
        cmd = int(input(">>: "))
        if cmd == 1:
            sc1.print_students()
        elif cmd == 2:
            while True:
                id = int(input("id: "))
                if Student(id, "", "") in sc1.students:
                    print("id exists")
                else:
                    break

            name = input("name: ")
            family = input("family: ")

            sc1.add_student(Student(id, name, family))
        elif cmd == 3:
            sid = int(input("enter student id to edit: "))
            search_s = Student(sid, "", "")
            if search_s in sc1.students:
                idx = sc1.students.index(search_s)
                target_student = sc1.students[idx]
            
                new_name = input("new name: ")
                new_family = input("new family: ")
                target_student.edit_info(new_name, new_family)
            else:
                print("student not found")
        elif cmd == 4:
            id = int(input("id: "))
            sc1.remove_student(id)

        elif cmd == 5:
            sc1.print_students()
            id = int(input("id: "))
            search_st = Student(id, "", "")
            if search_st in sc1.students:
                idx = sc1.students.index(search_st)
                sc1.selected_students = sc1.students[idx]
                level="students_select"
            else:
                print("students not found")
                
                
        elif cmd == 0:
            level = "root"
    elif level=="students_select":
        print("1- info")
        print("2- show courses")
        print("3- add course")
        print("4- delete course")
        print("5- set score")
        print("0- back")
        
        cmd = int(input(">>: "))
        if cmd==1:
            sc1.selected_students.info()
           
        elif cmd==2:
            pass
        elif cmd==3:
#            sc1.print_courses()
#            cid=int(input("course id: "))
#            search_course= Course(cid,"",0)
#            if search_course in sc1.courses:
#                target= sc1.courses[sc1.courses.index(search_course)]
#                sc1.selected_students.courses.append(target)
            for c in sc1.courses:
                if c not in sc1.selected_students.courses:
                    print(c)
            cid=int(input("course id: "))
            search_course= Course(cid,"",0)
            if search_course not in sc1.selected_students.courses:
                target= sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_students.courses.append(target)
                

        elif cmd==4:
            for c in sc1.selected_students.courses:
                print(c)
            cid=int(input("course id: "))
            search_course= Course(cid,"",0)
            if search_course in sc1.selected_students.courses:
                target= sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_students.courses.remove(target)
        elif cmd==5:
            for c in sc1.selected_students.courses:
                print(f"{c.id}\t{c.name}\t{c.scores}")

            cid = int(input("Course ID: "))
            search_course = Course(cid, "", 0)

            if search_course in sc1.selected_students.courses:
                idx = sc1.selected_students.courses.index(search_course)
                new_score = float(input("score: "))
                sc1.selected_students.courses[idx].scores = new_score

        elif cmd==0:
            level = "students"

        
    elif level == "teachers":
        print("1- show teachers")
        print("2- add teacher")
        print("3- edit teacher")
        print("4- delete teacher")
        print("5- select teacher")
        print("0- back")
        cmd = int(input(">>: "))


        if cmd == 1:
            sc1.print_teachers()
        elif cmd == 2:
            while True:
                id = int(input("id: "))
                if Teacher(id, "", "") in sc1.teachers:
                    print("id exists")
                else:
                    break

            name = input("name: ")
            family = input("family: ")

            sc1.add_teacher(Teacher(id, name, family))
        elif cmd == 3:
            tid = int(input("enter teacher id to edit: "))
            search_t = Teacher(tid, "", "")
            if search_t in sc1.teachers:
                idx = sc1.teachers.index(search_t)
                target_teacher = sc1.teachers[idx]
            
                new_name = input("new name: ")
                new_family = input("new family: ")
                target_teacher.edit_info(new_name, new_family)
            else:
                print("teacher not found")
        elif cmd == 4:
            id = int(input("id: "))
            sc1.remove_teacher(id)
        elif cmd == 5:
            sc1.print_teachers()
            id = int(input("id: "))
            search_tc = Teacher(id, "", "")
            if search_tc in sc1.teachers:
                idx = sc1.teachers.index(search_tc)
                sc1.selected_teachers = sc1.teachers[idx]
                level="teachers_select"
            else:
                print("teacher not found")
                
                
        elif cmd == 0:
            level = "root"
    elif level == "teachers_select":
        print("1- info")
        print("2- show courses")
        print("3- add course")
        print("4- delete course")
        print("5- set score")
        print("0- back")

        cmd = int(input(">>: "))

        if cmd == 1:
            sc1.selected_teachers.info()

        elif cmd == 2:
            pass

        elif cmd == 3:
            for c in sc1.courses:
                if c not in sc1.selected_teachers.courses:
                    print(c)

            cid = int(input("course id: "))
            search_course = Course(cid, "", 0)

            if search_course not in sc1.selected_teachers.courses:
                target = sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_teachers.courses.append(target)

        elif cmd == 4:
            for c in sc1.selected_teachers.courses:
                print(c)

            cid = int(input("course id: "))
            search_course = Course(cid, "", 0)

            if search_course in sc1.selected_teachers.courses:
                target = sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_teachers.courses.remove(target)

        elif cmd == 5:
            for c in sc1.selected_teachers.courses:
                print(f"{c.id}\t{c.name}\t{c.scores}")

            cid = int(input("Course ID: "))
            search_course = Course(cid, "", 0)

            if search_course in sc1.selected_teachers.courses:
                idx = sc1.selected_teachers.courses.index(search_course)
                new_score = float(input("score: "))
                sc1.selected_teachers.courses[idx].scores = new_score

        elif cmd == 0:
            level = "teachers"
    elif level == "courses":
        print("1- show courses")
        print("2- add course")
        print("3- edit course")
        print("4- delete course")
        print("5- select course")
        print("0- back")
        cmd = int(input(">>: "))
        if cmd == 1:
            sc1.print_courses()
        elif cmd == 2:
            while True:
                id = int(input("id: "))
                if Course(id, "", "") in sc1.courses:
                    print("id exists")
                else:
                    break

            name = input("name: ")
            family = input("family: ")

            sc1.add_course(Course(id, name, family))
        elif cmd == 3:
            cid = int(input("enter course id to edit: "))
            search_c = Course(cid, "", 0)
            if search_c in sc1.courses:
                idx = sc1.courses.index(search_c)
                target_course = sc1.courses[idx]
            
                new_name = input("enter new name: ")
                new_units = int(input("enter new units: "))           
                target_course.edit_info(new_name, new_units)
            else:
                print("course not found")
        elif cmd == 4:
            id = int(input("id: "))
            sc1.remove_course(id)
        elif cmd == 5:
            pass
        elif cmd == 0:
            level = "root"
    elif level == "classrooms":
        print("1- show classrooms")
        print("2- add classroom")
        print("3- edit classroom")
        print("4- delete classroom")
        print("5- select classroom")
        print("0- back")
        cmd = int(input(">>: "))
        if cmd == 1:
            sc1.print_classrooms()
        elif cmd == 2:
            id=int(input("classroom id: "))
            name=input("classroom name: ")
            classroom=Classroom(id,name)
            print("select course: ")
            sc1.print_courses()
            cid=int(input("course id: "))
            search_course=Course(cid,"",0)
            if search_course in sc1.courses:
                classroom.course=sc1.courses[sc1.courses.index(search_course)]

                print("available teachers: ")
                available_teachers=[]
                for t in sc1.teachers:
                    if search_course in t.courses:
                        print(t)
                        available_teachers.append(t)
                tid=int(input("teacher id: "))
                search_teacher= Teacher(tid , "","")
                if search_teacher in available_teachers:
                    classroom.teacher=available_teachers[available_teachers.index(search_teacher)]
            if classroom.teacher and classroom.course:
                sc1.classrooms.append(classroom)

            print("students with score under 10:")
            for s in sc1.students:
                for c in s.courses:
                    if c.id == classroom.course.id and c.scores < 10:
                        print(s)
            while True:
                sid=int(input("students id: "))
                if sid==0:
                    break
                search_s = Student(sid, "", "")
                if search_s in sc1.students:
                    idx = sc1.students.index(search_s)
                    student = sc1.students[idx]
                    if student not in classroom.students:
                        classroom.students.append(student)
            if classroom.teacher and classroom.course:
                sc1.classrooms.append(classroom)

        elif cmd == 3:
            id = int(input("id: "))
            for cl in sc1.classrooms:
                if cl.id== id:
                    new_name= input("new name: ")
                    cl.name=new_name
                    print(f"new name: {new_name}")
                    break
        elif cmd == 4:
            pass
        elif cmd == 5:
            sc1.print_classrooms()
            id = int(input("classroom id: "))
            search_cl = Classroom(id, "")
            if search_cl in sc1.classrooms:
                idx = sc1.classrooms.index(search_cl)
                sc1.selected_classroom = sc1.classrooms[idx]
                level = "classrooms_select"
            else:
                print("classroom not found")
        elif cmd == 0:
            level = "root"
    elif level=="classrooms_select":
        print("1- show info")
        print("2- change courses")
        print("3- change teacher")
        print("4- add student")
        print("5- remove student")
        print("0- back")
        cmd = int(input(">>: "))

        if cmd == 1:
            sc1.selected_classroom.info()
        elif cmd == 2:
            sc1.print_courses()
            
            cid = int(input("Enter new course id: "))
            search_course = Course(cid, "", 0)
            
            if search_course in sc1.courses:
                target_course = sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_classroom.change_classroom_course(target_course)

                #sc1.change_classroom_course(sc1.selected_classroom, target_course)
            else:
                print("Course not found.")
        elif cmd == 3:
            
            print("available teachers:")
            available_teachers = []
            for t in sc1.teachers:
                if sc1.selected_classroom.course in t.courses:
                    print(t)
                    available_teachers.append(t)

            if not available_teachers:
                print("no teacher available for this course")
            else:
                tid = int(input("teacher id: "))
                search_teacher = Teacher(tid, "", "")
                if search_teacher in available_teachers:
                    idx = available_teachers.index(search_teacher)
                    target_teacher = available_teachers[idx]
                    sc1.selected_classroom.change_classroom_teacher(target_teacher)
                else:
                    print("teacher not found")
        elif cmd == 4:
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
                print("no student available")
            else:
                sid = int(input("student id: "))
                search_student = Student(sid, "", "")

                if search_student in available_students:
                    student = available_students[available_students.index(search_student)]
                    sc1.selected_classroom.add_student_to_classroom(student)
                else:
                    print("student not found")

        elif cmd == 5:
            print("students in this classroom: ")
            for s in sc1.selected_classroom.students:
                print(s)
            sid = int(input("student id: "))
            search_student = Student(sid, "", "")
            if search_student in sc1.selected_classroom.students:
                student = sc1.selected_classroom.students[
                    sc1.selected_classroom.students.index(search_student)
                ]
                sc1.selected_classroom.remove_student_from_classroom(student)
            else:
                print("student not found")
        elif cmd == 0:
            level="classrooms"