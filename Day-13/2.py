import psycopg2

conn = psycopg2.connect(
    database="intern_db",
    user="postgres",
    password="sneha",
    host="localhost",
    port="5432"
)

print("Connected")