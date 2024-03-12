COMP 3005 Winter 2024 Assignment 3 Question 1
Student Name: Adam Luczaj
Student #: 101196424

Video URL: https://youtu.be/1pBLvLGJ1AQ

Design decision:
- I used psycopg3 because that is what were going to be using for the Final Project 1. Also, we are allowed to use any programming language for this assignment.
- Database validation was not provided as in the brightspace discussion forum it was stated that we can assume all data will be of valid types and that this check doesn't have to be done.

Functions:
- getAllStudents: Function that gets all the students from the database
- addStudents: Function that adds the student to the database
- updateStudentEmail: Function that updates a student email based on a provided student_id
- deleteStudent: Function that attempts to delete a student based on a provided student_id.

Instructions to setup database for program runtime (using pgAdmin4 as discussed on brightspace discussion forum):
1. Open pgAdmin4
2. Open Servers Dropdown
3. Open PostgreSQL 16 Dropdown
4. Right click database and click Create->Database...
5. Write a Database name (I used StudentManagementSystem) and press save.
6. Right click your database name and press Query Tool.
7. In this menu copy and paste:

CREATE TABLE students ( 
student_id SERIAL PRIMARY KEY, 
first_name TEXT NOT NULL, 
last_name TEXT NOT NULL, 
email TEXT UNIQUE NOT NULL, 
enrollment_date DATE 
); 

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES 
('John', 'Doe', 'john.doe@example.com', '2023-09-01'), 
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'), 
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

8. Highlight all this text you pasted then press the execute button.
9. In the comp3005a3q1AdamLuczaj.py file in the connect statement, fill out all the required system specific information detailed below the TODO (TA) comment.

Instructions to run program:
1. Install psycopg3 (do pip install psycopg then pip install "psycopg[binary]") (If that doesn't work please see this site for more information: https://www.psycopg.org/psycopg3/docs/basic/install.html)
2. Run the program (In VSCode you can press the play button)
