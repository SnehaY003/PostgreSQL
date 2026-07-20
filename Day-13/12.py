import psycopg2

conn = psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)
cur=conn.cursor()

cur.execute("SELECT COUNT(*) FROM students")

conn.commit()
print("TOTAL STUDENTS:", cur.fetchone()[0])
cur.close()
conn.close()