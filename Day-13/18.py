import psycopg2

emp = int(input("Employee ID: "))

conn = psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("DELETE FROM employees WHERE employee_id=%s",(emp,))

conn.commit()

print("Deleted")

cur.close()
conn.close()