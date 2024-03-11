import psycopg

# Function that gets all the students from the database
def getAllStudents(cursor):
    cursor.execute("SELECT * FROM students")
    studentRows = cursor.fetchall()

    print("(student_id, first_name, last_name, email, enrollment_date)")

    for studentRow in studentRows: 
        
        # Get each element to properly format it 
        student_id = studentRow[0]
        first_name = studentRow[1]
        last_name = studentRow[2]
        email = studentRow[3]
        enrollment_date = studentRow[4]

        # Format the row string to print it cleanly
        studentRow = f"({student_id}, {first_name}, {last_name}, {email}, {enrollment_date})"

        print(studentRow)

# Function that adds the student to the database
def addStudent(cursor, first_name, last_name, email, enrollment_date):
    addSQL = f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')"
    cursor.execute(addSQL)

# Function that updates a student email based on a provided student_id
def updateStudentEmail(cursor, student_id, new_email):
    updateSQL = f"UPDATE students set email = '{new_email}' WHERE student_id = '{student_id}'"
    cursor.execute(updateSQL)

# Function that attempts to delete a student based on a provided student_id.
def deleteStudent(cursor, student_id):
    deleteSQL = f"DELETE FROM students WHERE student_id = '{student_id}'" 
    cursor.execute(deleteSQL)

try:
    
    # Attempt to connect to the database
    # TODO (TA): this will need to be modified according to the TA's database name, username, password, and port number. The only thing probably different for the TA may be the password they are using and the dbname when setting up with the instructions.
    conn = psycopg.connect(dbname='StudentManagementSystem', user='postgres', password='postgres', host='localhost', port=5432)

    # The cursor is used to make queries to the database/execute commands.
    cursor = conn.cursor()

    userChoice = ""

    while userChoice != "exit":
        userChoice = input("Please select your choice (getAllStudents, addStudent, updateStudentEmail, deleteStudent, exit): ")

        if userChoice == "getAllStudents":
            getAllStudents(cursor)

        elif userChoice == "addStudent":
            userFirstName = input("Please write the first name: ")
            userLastName = input("Please write the last name: ")
            userEmail = input("Please write the email: ")
            userEnrollmentDate = input("Please write the enrollment date (YEAR-MONTH-DAY): ")
            addStudent(cursor, userFirstName, userLastName, userEmail, userEnrollmentDate)

        elif userChoice == "updateStudentEmail":
            userStudentID = input("Please enter student id you wish to update: ")
            userEmail = input("Please enter the email you wish to update: ")
            updateStudentEmail(cursor, userStudentID, userEmail)

        elif userChoice == "deleteStudent":
            userStudentID = input("Please provide the id of the student you wish to remove: ")
            deleteStudent(cursor, userStudentID)
        
        # Catch invalid selections 
        elif userChoice != "exit":
            print("Invalid choice selected. Please select from the listed choices.")

# Catch any errors psycopg throws
except psycopg.OperationalError as e:
    error_message = f"Error: {e}"
    print(error_message)
    exit(1)

# Close our database connections
finally:
    cursor.close()
    conn.commit() # what this does is save the database changes.
    conn.close()

