import psycopg2

roll=int(input("Roll:"))

conn = psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)
cur=conn.cursor()

cur.execute("DELETE FROM students WHERE roll=%s",(roll,))

conn.commit()
print("DELETED")
cur.close()
conn.close()