import psycopg2

conn=psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)

cur=conn.cursor()

students=[(102,"mehak",21,"mehak1@gmail.com",90), (103,"neha",19,"neha1@gmail.com",92),(104,"Rahul",22,"rahul1@gmail.com",76)]

cur.executemany(
    "INSERT INTO students VALUES(%s,%s,%s,%s,%s)",
    students
)

conn.commit()

print("students added")
cur.close()
conn.close()