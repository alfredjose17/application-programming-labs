import mysql.connector
import info_pass


mydb = mysql.connector.connect(host="127.0.0.1", user='root', password=info_pass.PASSWORD)
cursor = mydb.cursor()
cursor.execute("USE ap")

# Define the SQL queries to create tables
create_student_table = """
CREATE TABLE student (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL UNIQUE
)
"""

create_course_table = """
CREATE TABLE course (
    course_id INT PRIMARY KEY,
    course_title VARCHAR(40) NOT NULL,
    course_credits INT
)
"""

create_registration_table = """
CREATE TABLE registration (
    registration_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_semester VARCHAR(20) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
)
"""

# Execute the table creation queries
cursor.execute(create_student_table)
cursor.execute(create_course_table)
cursor.execute(create_registration_table)

cursor.execute('DESCRIBE student')
print("\nStudent Table\n", cursor.fetchall())

cursor.execute('DESCRIBE course')
print("\nCourse Table\n", cursor.fetchall())

cursor.execute('DESCRIBE registration')
print("\nRegistration Table\n", cursor.fetchall())

# Commit the changes and close the cursor and connection
mydb.commit()
cursor.close()
mydb.close()