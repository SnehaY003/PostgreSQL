import psycopg2

def connect():
    return psycopg2.connect(
        database="intern_db",
        user="postgres",
        password="sneha",
        host="localhost",
        port="5432"
    )

conn = connect()
print("connected")