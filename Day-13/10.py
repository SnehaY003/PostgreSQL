import psycopg2

roll = int(input("Roll: "))
marks = int(input("Marks: "))

conn = psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute(
    "UPDATE students SET marks=%s WHERE roll=%s",
    (marks,roll)
)

conn.commit()

print("Updated")

cur.close()
conn.close()