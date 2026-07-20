import psycopg2

conn=psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)

cur=conn.cursor()

cur.execute('SELECT * FROM students')

for record in cur.fetchall():
    print(record)

cur.close()
conn.close()