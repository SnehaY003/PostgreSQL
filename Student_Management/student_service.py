from database import connect
import psycopg2


def add_student():
    try:
        roll = int(input("Roll Number: "))
        name = input("Name: ")
        age = int(input("Age: "))
        email = input("Email: ")
        marks = int(input("Marks: "))

        if age <= 0:
            print("Age must be positive")
            return

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100")
            return

        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM students WHERE email=%s", (email,))
        if cur.fetchone():
            print("Email already exists")
            cur.close()
            conn.close()
            return

        cur.execute(
            "INSERT INTO students VALUES (%s,%s,%s,%s,%s)",
            (roll, name, age, email, marks)
        )

        conn.commit()
        print("Student Added")

        cur.close()
        conn.close()

    except ValueError:
        print("Invalid Input")

    except psycopg2.Error as e:
        print("Database Error:", e)


def view_students():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    students = cur.fetchall()

    for student in students:
        print(student)

    cur.close()
    conn.close()


def search_student():
    roll = int(input("Enter Roll Number: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE roll=%s", (roll,))
    student = cur.fetchone()

    if student:
        print(student)
    else:
        print("Student Not Found")

    cur.close()
    conn.close()


def update_student():
    roll = int(input("Roll Number: "))
    marks = int(input("New Marks: "))

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100")
        return

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE students SET marks=%s WHERE roll=%s",
        (marks, roll)
    )

    conn.commit()
    print("Student Updated")

    cur.close()
    conn.close()


def delete_student():
    roll = int(input("Roll Number: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE roll=%s", (roll,))

    conn.commit()
    print("Student Deleted")

    cur.close()
    conn.close()