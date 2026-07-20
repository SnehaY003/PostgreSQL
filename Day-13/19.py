import psycopg2

dept = input("Department: ")

conn = psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute(
    "SELECT * FROM employees WHERE department=%s",
    (dept,)
)

for row in cur.fetchall():
    print(row)

cur.close()
conn.close()