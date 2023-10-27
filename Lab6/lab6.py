"""
Application Name: Lab6.py
Developer: Alfred Varghese Jose
Date: 10/23/2023

An application program for an Institution where new students can added, students can be registered on courses available, display the existing students, courses and registrations and search for the students. 
"""

import mysql.connector
import info_pass


mydb = mysql.connector.connect(host="127.0.0.1", user='root', password=info_pass.PASSWORD)
my_cursor = mydb.cursor()
my_cursor.execute("USE ap")


# add new student
def student_add():

    student_id = int(input("Enter student ID:\t"))

    my_cursor.execute(f"select * from student where student_id={student_id}")
    result = my_cursor.fetchall()

    if not result:
        first_name = input("Enter first name of the student to register:\t")
        last_name = input("Enter last name of the student to register:\t")
        email_id = input("Enter email ID of the student to register:\t")

        my_cursor.execute(f"insert into student values ({student_id}, '{first_name}', '{last_name}', '{email_id}')")
        mydb.commit()

        print("Student was added and registered .. .. ..")
    else:
        print(f"Student with student ID {student_id} already exists .. .. ..")


# register student in course
def student_register():

    student_id = int(input("Enter student ID:\t"))
    my_cursor.execute(f"select * from student where student_id={student_id}")
    result1 = my_cursor.fetchall()

    if result1:

        course_id = int(input("Enter course ID:\t"))
        my_cursor.execute(f"select * from course where course_id={course_id}")
        result2 = my_cursor.fetchall()

        if result2:

            enrollment_semester = input("Enter semester of enrollment:\t")
            my_cursor.execute(f"select s.last_name, s.first_name, s.student_id, c.course_id, c.course_title, r.enrollment_semester from registration r join student s on r.student_id = s.student_id join course c on r.course_id = c.course_id where s.student_id={student_id} and c.course_id={course_id} and r.enrollment_semester='{enrollment_semester}'")
            result3 = my_cursor.fetchall()

            if not result3:

                my_cursor.execute(f"insert into registration(student_id, course_id, enrollment_semester) values ({student_id}, {course_id}, '{enrollment_semester}')")
                mydb.commit()

                print(f"Student {student_id} is registered for course {course_id} .. .. ..")
            
            else:
                print(f"Student {student_id} already registered in course {course_id} for {enrollment_semester}  .. .. ..")
        
        else:
            print(f"Course with course code {course_id} does not exist - cannot register .. .. ..")

    else:
        print(f"Student with student ID {student_id} does not exist - cannot register .. .. ..")


# display all students
def display_student():
    
    my_cursor.execute("select * from student")
    result = my_cursor.fetchall()

    if result:
        author_display()
        print("\n%60s\n%s" % ("Students", "#*"*60))
        print("\n%30s%30s%30s%30s" % ("Student ID", "First Name", "Last Name", "Email Address"))
        for student in result:
            print("\n%30s%30s%30s%30s" % (student[0], student[1], student[2], student[3]))
        print("#*"*60)
    else:
        print("There are no students registered with this institution .. .. ..")


# display all courses
def display_course():

    my_cursor.execute("select * from course")
    result = my_cursor.fetchall()

    if result:
        author_display()
        print("\n%60s\n%s" % ("Courses", "#*"*60))
        print("\n%40s%40s%40s" % ("Course Code", "Course Title", "Course Credits"))
        for course in result:
            print("\n%40s%40s%40s" % (course[0], course[1], course[2]))
        print("#*"*60)
    else:
        print("Courses are not currently offered at this institution .. .. ..")


# display all registrations
def display_registration():
    
    my_cursor.execute("select s.last_name, s.first_name, s.student_id, c.course_id, c.course_title, r.enrollment_semester from registration r join student s on r.student_id = s.student_id join course c on r.course_id = c.course_id")
    result = my_cursor.fetchall()

    if result:
        author_display()
        print("\n%60s\n%s" % ("Registration", "#*"*60))
        print("\n%20s%20s%20s%20s%20s%20s" % ("Last Name", "First Name", "Student ID", "Course Code", "Course Title", "Semester Enrolled"))
        for item in result:
            print("\n%20s%20s%20s%20s%20s%20s" % (item[0], item[1], item[2], item[3], item[4], item[5]))
        print("#*"*60)
    else:
        print("There are no student registered in any course at the institution .. .. ..")


# display author info
def author_display():

    print("\n%s\n%120s\n%120s\n%s" % ("#*"*60, "Alfred Varghese Jose", "N01619463","#*"*60))


# search for student
def student_search():

    student_id = int(input("Enter student ID to search:\t"))

    my_cursor.execute(f"select * from student where student_id={student_id}")
    student = my_cursor.fetchone()

    if student:
        author_display()
        print("\n%60s\n%s" % ("Student Search", "#*"*60))
        print("\n%30s%30s%30s%30s" % ("Student ID", "First Name", "Last Name", "Email Address"))
        print("\n%30s%30s%30s%30s" % (student[0], student[1], student[2], student[3]))
        print("#*"*60)
    else:
        print(f"Student having student ID {student_id} is not enrolled in the institution .. .. ..")


if __name__ == '__main__':

    print(__doc__)
    
    choice = ""

    # display menu and accept choice
    while True:

        print("\n\t1) Display all students \n\t2) Display all courses \n\t3) Display all registrations - students and courses \n\t4) Register student in course \n\t5) Search Student \n\t6) Add Student \n\t7) End Application \n")
        choice = input("Enter your choice ... ...")
        
        if choice == '1':
            display_student()

        elif choice == '2':
            display_course()

        elif choice == '3':
            display_registration()

        elif choice == '4':
            student_register()

        elif choice == '5':
            student_search()

        elif choice == '6':
            student_add()

        elif choice == '7':
            print("\nApplication ending now .. .. .. ..")
            my_cursor.close()
            mydb.close()
            break

        else:
            print("\nPlease enter a valid choice from the menu .. .. ..")
