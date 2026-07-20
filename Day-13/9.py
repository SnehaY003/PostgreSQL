import psycopg2

conn = psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

roll = int(input("Enter roll number: "))

cur.execute("SELECT * FROM students WHERE roll=%s", (roll,))

student = cur.fetchone()

print(student)

cur.close()
conn.close()