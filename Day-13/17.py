import psycopg2

emp = int(input("Employee ID: "))
salary = float(input("New Salary: "))

conn = psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute(
    "UPDATE employees SET salary=%s WHERE employee_id=%s",
    (salary,emp)
)

conn.commit()

print("Updated")

cur.close()
conn.close()