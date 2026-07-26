import json
class Course:
    id: int = 0
    name: str = ""
    units: int = 0
    scores: float = 0

    def __init__(self, id: int, name: str, units: int):
        self.id = id
        self.name = name
        self.units = units

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.units}"

    def __eq__(self, other):
        if isinstance(other, Course):
            return self.id == other.id
        return self.id == other


class Student:
    id: int = 0
    name: str = ""
    family: str = ""
    courses: list[Course]

    def __init__(self, id: int, name: str, family: str):
        self.id = id
        self.name = name
        self.family = family
        self.courses = []

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}"

    def __eq__(self, other):
        return (self.id == other.id)
    
    def info(self) -> None:
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"family: {self.family}")
        for c in self.courses:
            print(f"{c.id}\t{c.name}\t{c.scores}")

class Teacher:
    id: int = 0
    name: str = ""
    family: str = ""
    courses: list[Course]

    def __init__(self, id: int, name: str, family: str):
        self.id = id
        self.name = name
        self.family = family
        self.courses = []

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}"

    def __eq__(self, other):
        return (self.id == other.id)
    
    def info(self) -> None:
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"family: {self.family}")
        for c in self.courses:
            print(f"{c.id}\t{c.name}\t{c.scores}")

class Classroom:
    id: int = 0
    name: str = ""
    teacher: Teacher=None
    course: Course=None


    def __init__(self, id: int,name: str):
        self.id = id
        self.name = name
        self.students: list[Student] = []
        self.teacher = None
        self.course = None
        self.selected_classroom: Classroom = None

    def info(self) -> None:
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
        if isinstance(other, Classroom):
            return self.id == other.id
        return self.id == other
    def change_classroom_course(self, new_course: Course) -> None:
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
        if self.course not in new_teacher.courses:
            print("this teacher doesnt teach this course")
            return
        self.teacher=new_teacher
        print("teacher changed")
    def add_student_to_classroom(self, student:Student) -> None:
        if student in self.students:
            print("student already in classroom")
            return
        self.students.append(student)
        print("student added")
    def remove_student_from_classroom(self) -> None:
        
        if student in self.students:
            self.students.remove(student)
            print("student removed")
        else:
            print("student not found")



class School:
    name: str = ""
    courses: list[Course] = []
    students: list[Student] = []
    teachers: list[Teacher] = []
    classrooms: list[Classroom]=[]
    selected_students: Student= None
    

    def __init__(self, name: str):
        self.name = name
        self.courses = []
        self.students= []
        self.teachers=[]
        self.classrooms = []
        self.selected_students:Student=None
        self.selected_teachers:Teacher=None
        self.selected_courses:Course=None
        self.selected_classroom: Classroom = None
    
    
    def print_students(self) -> None:
        for s in self.students:
            print(f"ID: {s.id} | Name: {s.name} {s.family} | Courses: {s.courses}")

    def print_classrooms(self):
        for cl in self.classrooms:
            print(f"{cl.id}\t{cl.name}")
    def remove_classroom(self, id: int):

        search_classroom = Classroom(id, None, None)
        if search_classroom not in self.classrooms:
            print("classroom not found")
            return
        self.classrooms.remove(search_classroom)
        print("classroom deleted")


    def add_student(self, student: Student) -> None:
        for st in self.students:
            if st.id == student.id:
                print("this student id already exists.")
                return False
        self.students.append(student)
        return True

    def edit_student(self, student: Student) -> None:
        if student in self.students:
            i = self.students.index(student) 
            self.students[i] = student 
            print("student updated")
        else:
            print("student not found")

    def remove_student(self, id: int) -> None:
        search_student = Student(id, "", "")
        if search_student not in self.students:
            print("student not found")
            return
        for cl in self.classrooms:
            if search_student in cl.students:
                print("student is in a classroom, cannot delete")
                return

    def print_courses(self) -> None:
        for c in self.courses:
            print(c)

    def add_course(self, course: Course) -> None:
        for c in self.courses:
            if c.id == course.id:
                return False
        self.courses.append(course)
        return True

    def edit_course(self, course: Course) -> None:
        if course in self.courses:
            i = self.courses.index(course) 
            self.courses[i] = course 
            print("course updated")
        else:
            print("course not found")
    def remove_course(self, id: int) -> None:

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
        for t in self.teachers:
            print(t)

    def add_teacher(self, teacher: Teacher) -> None:
        for t in self.teachers:
            if t.id == teacher.id:
                print("this teacher id already exists.")
            return False
        self.teachers.append(teacher)
        return True
    def edit_teacher(self, teacher: Teacher) -> None:

        if teacher in self.teachers:
            i = self.teachers.index(teacher) 
            self.teachers[i] = teacher 
            print("teacher updated")
        else:
            print("teacher not found")

    def remove_teacher(self, id: int) -> None:
        
        search_teacher = Student(id, "", "")
        if search_teacher not in self.teachers:
            print("teacher not found")
            return 
        for cl in self.classrooms:
            if search_teacher == search_teacher:
                print("teacher is in a classroom, cannot delete")
                return
        self.teachers.remove(search_teacher)
    def load_data(self):
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
                    idx=self.courses.index(cid)
                    base=self.courses[idx] 
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
                    idx= self.teachers.index(search_t)
                    classroom.teacher=self.teachers[idx]
            else:
                classroom.teacher=None

            for sid in cl["students"]:
                search_s = Student(sid, "", "")
                if search_s in self.students:
                    idx = self.students.index(search_s)
                    classroom.students.append(self.students[idx])

            self.classrooms.append(classroom)
        
        
    def save_data(self):
        data={
            "students":[],
            "courses":[],
            "teachers":[],
            "classrooms":[]
        }

        for c in self.courses:
            data["courses"].append({
            "id":c.id,
                "name":c.name,
                "units":c.units
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

        file=open("01.json","w")
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
            pass
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
            pass
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
            pass
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