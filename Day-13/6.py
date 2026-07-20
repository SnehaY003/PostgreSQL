import psycopg2

conn=psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)

cur=conn.cursor()

cur.execute(
    "INSERT INTO students VALUES(%s,%s,%s,%s,%s)",
    (101,"Sneha",20,"sneha3@gmail.com",95)
)
conn.commit()

print("student added")
cur.close()
conn.close()