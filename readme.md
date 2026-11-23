# School Management System

This project is a school management system that you can use on your computer and it is made using Python. It lets people manage the students, the teachers, the courses and the classrooms.

There is a menu to use that instructs them on what to do. The program is also made in a way that's easy to understand and it stores all the information in a special file called a JSON file.

The School Management System uses a way of making programs called object-oriented programming. This means the School Management System contains parts that operate together to support the entire system. This project stores its data in the JSON file so it can remember things later.

The code is split into two files: `model.py` contains all the models (classes), and `main.py` contains the menus and user interaction.

## Project Structure

```text
school-management-system/
├── main.py       # menus and user interaction
├── model.py      # models: Course, Student, Teacher, Classroom, School
└── data.json     # saved data
```

## Models

All the models are separated from the menu code and live in `model.py`:

- `Course`: id, name, units and score. It can edit its own info.
- `Student`: id, name, family and a list of courses. It can show and edit its info.
- `Teacher`: id, name, family and a list of courses that they teach. It can show and edit its info.
- `Classroom`: id, name, one course, one teacher and a list of students. It can change its course and teacher, and add or remove students.
- `School`: the main model that keeps all the lists (students, teachers, courses, classrooms), finds, adds and removes records, and saves and loads the data from the JSON file.

`main.py` only imports these models and uses them, so the logic of the system stays in the models and the menu stays simple.

## Installation

1. Clone the repository:
=======
This project is a school management system that you can use on your computer and it is made using Python.It lets people manage the students, the teachers, the courses and the classrooms.

There is a menu to use that instructs them on what to do. The program is also made in a way that's easy to understand and it stores all the information, in a special file called a JSON file.

The School Management System uses a way of making programs called object-oriented programming, This means the School Management System contains parts that operate together to support the entire system.This project stores its data in the JSON file so it can remember things later.

## Installation

1. Clone the repository :
>>>>>>> 979233c9d70d8f67f6c578bf73fdbe17e07aeaa8
   https://github.com/melikahaghgou/school-management-system

2. Navigate to the project directory:
   ```bash
<<<<<<< HEAD
   cd school-management-system
   ```

Ensure you have Python installed on your system. You can verify this by running `python --version` in your terminal.

3. Install the required library:
   ```bash
   pip install colorama
   ```

4. Now you should open VS Code. Then open the folder that has these files.

5. After that you need to open the terminal in VS Code by pressing Ctrl and the backtick key at the same time.

6. Once you are in the project directory, run the main file by typing the following command and pressing Enter:

```bash
python main.py
```

The program is going to start. You will see the menu for the program.

Note: the file `data.json` must exist in the project folder with this content:

```json
{
    "students": [],
    "courses": [],
    "teachers": [],
    "classrooms": []
}
```
=======
      cd school-management-system
   ```
Ensure you have Python installed on your system. You can verify this by running python --version in your terminal.


1. Now you should open VS Code. Then open the folder that has these files.

2. After that you need to open the terminal in VS Code by pressing Ctrl and the backtick key at the time.

5.Once you are in the project directory, run your Python file by typing the following command and pressing Enter:

python your_filename.py

The program is going to start. You will see the menu, for the program.

>>>>>>> 979233c9d70d8f67f6c578bf73fdbe17e07aeaa8

# Usage

When you run the program the main menu appears on the screen.

```text
1- students
2- teachers
3- courses
4- classrooms
5- save
0- exit
```
<<<<<<< HEAD

=======
>>>>>>> 979233c9d70d8f67f6c578bf73fdbe17e07aeaa8
Each of the sections students and teachers and courses and classrooms takes you to a sub-menu where you can manage things. Here is what you can do in each part of the system:

1- Students, Teachers, Courses, & Classrooms

<<<<<<< HEAD
The sub-menu for students and teachers and courses and classrooms is almost the same. When you pick one of these you will see:

```text
1- show students
2- add student
3- edit student
4- delete student
5- select student
=======
The sub-menu for students and teachers and courses and classrooms is all the same. When you pick one of these you will see:

```text
1- show students
2- add students
3- edit students
4- delete students
5- students
>>>>>>> 979233c9d70d8f67f6c578bf73fdbe17e07aeaa8
0- back
```
Or
```text
1- show teachers
<<<<<<< HEAD
2- add teacher
3- edit teacher
4- delete teacher
5- select teacher
0- back
```

It is the same for courses and classrooms (courses do not have the select option).

Options Explained:
=======
2- add teachers
3- edit teachers
4- teachers
5- select teachers
0- back
```

It is the same for courses and classrooms.

Options Explained:  
>>>>>>> 979233c9d70d8f67f6c578bf73fdbe17e07aeaa8

Show: displays all records for the selected section.  
Add: creates a new record.  
Edit: updates an existing record.  
Delete: removes a record from the system.  
Select: chooses a specific record for further operations.  
<<<<<<< HEAD
Back: returns to the main menu.

Save and Exit:  
5- save: saves all current changes to data.json.  
0- exit: closes the application.  
Make sure to save your changes before exiting, otherwise they will not be stored.

This is very important. It saves your current session data into the data.json file.

Note: Always remember to select 5- save before you exit the program or any changes you made during that session will not be saved.
=======
Back: returns to the main menu.    
Save and Exit :  
5- save: saves all current changes to 01.json.  
0- exit: closes the application.  
Make sure to save your changes before exiting, otherwise they will not be stored.

This is very important. It saves your current session data into the 01.json file.

Note: Always remember to select 5- save before you exit the program or any changes you made, during that session will not be saved.




>>>>>>> 979233c9d70d8f67f6c578bf73fdbe17e07aeaa8
