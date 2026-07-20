import psycopg2

conn = psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

employees = [
    ("Rohan","HR",45000),
    ("Priya","IT",65000),
    ("Ankit","Sales",52000)
]

cur.executemany(
    "INSERT INTO employees(name,department,salary) VALUES(%s,%s,%s)",
    employees
)

conn.commit()

print("Employees Added")

cur.close()
conn.close()