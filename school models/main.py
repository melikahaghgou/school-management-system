from colorama import Fore, Style

from model import (
    Course,
    Student,
    Teacher,
    Classroom,
    School
)



level = "root"
school = School("sama")
school.load_data()


while True:
    if level == "root":
        print(Fore.CYAN + Style.BRIGHT + "========== SCHOOL MANAGEMENT SYSTEM ==========")
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
            school.save_data()
        elif cmd == 0:
            break

    elif level == "students":
        print(Fore.GREEN + Style.BRIGHT + "========== STUDENTS MENU ==========")
        print(Fore.WHITE + "1- show students")
        print(Fore.WHITE + "2- add student")
        print(Fore.WHITE + "3- edit student")
        print(Fore.WHITE + "4- delete student")
        print(Fore.WHITE + "5- select student")
        print(Fore.BLUE + "0- back")

        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            for student in school.students:
                print(f"ID: {student.id} | Name: {student.name} {student.family}")

        elif cmd == 2:
            student_id = int(input(Fore.CYAN + "id: "))
            name = input(Fore.CYAN + "name: ")
            family = input(Fore.CYAN + "family: ")

            school.add_student(Student(student_id, name, family))

        elif cmd == 3:
            student_id = int(input(Fore.CYAN + "enter student id to edit: "))
            student = school.find_student(student_id)

            if student:
                new_name = input(Fore.CYAN + "new name: ")
                new_family = input(Fore.CYAN + "new family: ")
                student.edit_info(new_name, new_family)
            else:
                print(Fore.RED + "student not found")

        elif cmd == 4:
            student_id = int(input(Fore.CYAN + "id: "))
            school.remove_student(student_id)

        elif cmd == 5:
            for student in school.students:
                print(student)

            student_id = int(input(Fore.CYAN + "id: "))
            student = school.find_student(student_id)

            if student:
                school.selected_student = student
                level = "students_select"
            else:
                print(Fore.RED + "student not found")

        elif cmd == 0:
            level = "root"

    elif level == "students_select":
        student = school.selected_student

        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "========== STUDENT PANEL ==========")
        print(Fore.WHITE + "1- info")
        print(Fore.WHITE + "2- show courses")
        print(Fore.WHITE + "3- add course")
        print(Fore.WHITE + "4- delete course")
        print(Fore.WHITE + "5- set score")
        print(Fore.BLUE + "0- back")

        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            student.info()

        elif cmd == 2:
            for course in student.courses:
                print(f"{course.id}\t{course.name}\t{course.scores}")

        elif cmd == 3:
            for course in school.courses:
                if course not in student.courses:
                    print(course)

            course_id = int(input(Fore.CYAN + "course id: "))
            course = school.find_course(course_id)

            if course and course not in student.courses:
                student.courses.append(course)
            else:
                print(Fore.RED + "course not found or already added")

        elif cmd == 4:
            for course in student.courses:
                print(course)

            course_id = int(input(Fore.CYAN + "course id: "))
            course = school.find_course(course_id)

            if course and course in student.courses:
                student.courses.remove(course)
            else:
                print(Fore.RED + "course not found")

        elif cmd == 5:
            for course in student.courses:
                print(f"{course.id}\t{course.name}\t{course.scores}")

            course_id = int(input(Fore.CYAN + "course id: "))
            course = school.find_course(course_id)

            if course and course in student.courses:
                score = float(input(Fore.CYAN + "score: "))
                course.scores = score
            else:
                print(Fore.RED + "course not found")

        elif cmd == 0:
            level = "students"

    elif level == "teachers":
        print(Fore.YELLOW + Style.BRIGHT + "========== TEACHERS MENU ==========")
        print(Fore.WHITE + "1- show teachers")
        print(Fore.WHITE + "2- add teacher")
        print(Fore.WHITE + "3- edit teacher")
        print(Fore.WHITE + "4- delete teacher")
        print(Fore.WHITE + "5- select teacher")
        print(Fore.BLUE + "0- back")

        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            for teacher in school.teachers:
                print(f"ID: {teacher.id} | Name: {teacher.name} {teacher.family}")

        elif cmd == 2:
            teacher_id = int(input(Fore.CYAN + "id: "))
            name = input(Fore.CYAN + "name: ")
            family = input(Fore.CYAN + "family: ")

            school.add_teacher(Teacher(teacher_id, name, family))

        elif cmd == 3:
            teacher_id = int(input(Fore.CYAN + "enter teacher id to edit: "))
            teacher = school.find_teacher(teacher_id)

            if teacher:
                new_name = input(Fore.CYAN + "new name: ")
                new_family = input(Fore.CYAN + "new family: ")
                teacher.edit_info(new_name, new_family)
            else:
                print(Fore.RED + "teacher not found")

        elif cmd == 4:
            teacher_id = int(input(Fore.CYAN + "id: "))
            school.remove_teacher(teacher_id)

        elif cmd == 5:
            for teacher in school.teachers:
                print(teacher)

            teacher_id = int(input(Fore.CYAN + "id: "))
            teacher = school.find_teacher(teacher_id)

            if teacher:
                school.selected_teacher = teacher
                level = "teachers_select"
            else:
                print(Fore.RED + "teacher not found")

        elif cmd == 0:
            level = "root"

    elif level == "teachers_select":
        teacher = school.selected_teacher

        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "========== TEACHER PANEL ==========")
        print(Fore.WHITE + "1- info")
        print(Fore.WHITE + "2- show courses")
        print(Fore.WHITE + "3- add course")
        print(Fore.WHITE + "4- delete course")
        print(Fore.BLUE + "0- back")

        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            teacher.info()

        elif cmd == 2:
            for course in teacher.courses:
                print(course)

        elif cmd == 3:
            for course in school.courses:
                if course not in teacher.courses:
                    print(course)

            course_id = int(input(Fore.CYAN + "course id: "))
            course = school.find_course(course_id)

            if course and course not in teacher.courses:
                teacher.courses.append(course)
            else:
                print(Fore.RED + "course not found or already added")

        elif cmd == 4:
            for course in teacher.courses:
                print(course)

            course_id = int(input(Fore.CYAN + "course id: "))
            course = school.find_course(course_id)

            if course and course in teacher.courses:
                teacher.courses.remove(course)
            else:
                print(Fore.RED + "course not found")

        elif cmd == 0:
            level = "teachers"

    elif level == "courses":
        print(Fore.MAGENTA + Style.BRIGHT + "========== COURSES MENU ==========")
        print(Fore.WHITE + "1- show courses")
        print(Fore.WHITE + "2- add course")
        print(Fore.WHITE + "3- edit course")
        print(Fore.WHITE + "4- delete course")
        print(Fore.BLUE + "0- back")

        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            for course in school.courses:
                print(f"ID: {course.id} | Name: {course.name} | Units: {course.units}")

        elif cmd == 2:
            course_id = int(input(Fore.CYAN + "id: "))
            name = input(Fore.CYAN + "name: ")
            units = int(input(Fore.CYAN + "units: "))

            school.add_course(Course(course_id, name, units))

        elif cmd == 3:
            course_id = int(input(Fore.CYAN + "enter course id to edit: "))
            course = school.find_course(course_id)

            if course:
                new_name = input(Fore.CYAN + "new name: ")
                new_units = int(input(Fore.CYAN + "new units: "))
                course.edit_info(new_name, new_units)
            else:
                print(Fore.RED + "course not found")

        elif cmd == 4:
            course_id = int(input(Fore.CYAN + "id: "))
            school.remove_course(course_id)

        elif cmd == 0:
            level = "root"

    elif level == "classrooms":
        print(Fore.BLUE + Style.BRIGHT + "========== CLASSROOMS MENU ==========")
        print(Fore.WHITE + "1- show classrooms")
        print(Fore.WHITE + "2- add classroom")
        print(Fore.WHITE + "3- edit classroom")
        print(Fore.WHITE + "4- delete classroom")
        print(Fore.WHITE + "5- select classroom")
        print(Fore.BLUE + "0- back")

        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            for classroom in school.classrooms:
                print(classroom)

        elif cmd == 2:
            classroom_id = int(input(Fore.CYAN + "classroom id: "))
            classroom_name = input(Fore.CYAN + "classroom name: ")

            classroom = Classroom(classroom_id, classroom_name)

            print("select course:")
            for course in school.courses:
                print(course)

            course_id = int(input(Fore.CYAN + "course id: "))
            course = school.find_course(course_id)

            if not course:
                print(Fore.RED + "course not found")
                continue

            classroom.course = course

            print("available teachers:")
            available_teachers = []

            for teacher in school.teachers:
                if course in teacher.courses:
                    print(teacher)
                    available_teachers.append(teacher)

            teacher_id = int(input(Fore.CYAN + "teacher id: "))
            teacher = school.find_teacher(teacher_id)

            if teacher and teacher in available_teachers:
                classroom.teacher = teacher
            else:
                print(Fore.RED + "teacher not found")

            school.classrooms.append(classroom)
            print(Fore.GREEN + "classroom added")

        elif cmd == 3:
            classroom_id = int(input(Fore.CYAN + "id: "))
            classroom = school.find_classroom(classroom_id)

            if classroom:
                new_name = input(Fore.CYAN + "new name: ")
                classroom.name = new_name
                print(Fore.GREEN + "classroom updated")
            else:
                print(Fore.RED + "classroom not found")

        elif cmd == 4:
            classroom_id = int(input(Fore.CYAN + "id: "))
            school.remove_classroom(classroom_id)

        elif cmd == 5:
            for classroom in school.classrooms:
                print(classroom)

            classroom_id = int(input(Fore.CYAN + "classroom id: "))
            classroom = school.find_classroom(classroom_id)

            if classroom:
                school.selected_classroom = classroom
                level = "classrooms_select"
            else:
                print(Fore.RED + "classroom not found")

        elif cmd == 0:
            level = "root"

    elif level == "classrooms_select":
        classroom = school.selected_classroom

        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "========== CLASSROOM PANEL ==========")
        print(Fore.WHITE + "1- show info")
        print(Fore.WHITE + "2- change course")
        print(Fore.WHITE + "3- change teacher")
        print(Fore.WHITE + "4- add student")
        print(Fore.WHITE + "5- remove student")
        print(Fore.BLUE + "0- back")

        cmd = int(input(Fore.CYAN + ">>: "))

        if cmd == 1:
            classroom.info()

        elif cmd == 2:
            for course in school.courses:
                print(course)

            course_id = int(input(Fore.CYAN + "new course id: "))
            course = school.find_course(course_id)

            if course:
                classroom.change_classroom_course(course)
            else:
                print(Fore.RED + "course not found")

        elif cmd == 3:
            if not classroom.course:
                print(Fore.RED + "first select a course")
                continue

            print("available teachers:")
            available_teachers = []

            for teacher in school.teachers:
                if classroom.course in teacher.courses:
                    print(teacher)
                    available_teachers.append(teacher)

            if not available_teachers:
                print(Fore.RED + "no teacher available for this course")
                continue

            teacher_id = int(input(Fore.CYAN + "teacher id: "))
            teacher = school.find_teacher(teacher_id)

            if teacher and teacher in available_teachers:
                classroom.change_classroom_teacher(teacher)
            else:
                print(Fore.RED + "teacher not found")

        elif cmd == 4:
            if not classroom.course:
                print(Fore.RED + "first select a course")
                continue

            print("students with score under 10:")
            available_students = []

            for student in school.students:
                if student in classroom.students:
                    continue

                for course in student.courses:
                    if course.id == classroom.course.id and course.scores < 10:
                        print(student)
                        available_students.append(student)
                        break

            if not available_students:
                print(Fore.RED + "no student available")
                continue

            student_id = int(input(Fore.CYAN + "student id: "))
            student = school.find_student(student_id)

            if student and student in available_students:
                classroom.add_student_to_classroom(student)
            else:
                print(Fore.RED + "student not found")

        elif cmd == 5:
            for student in classroom.students:
                print(student)

            student_id = int(input(Fore.CYAN + "student id: "))
            student = school.find_student(student_id)

            if student:
                classroom.remove_student_from_classroom(student)
            else:
                print(Fore.RED + "student not found")

        elif cmd == 0:
            level = "classrooms"