from db import get_connection

conn = get_connection()
print("Connection:", conn)

if conn:
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    print("Tables:", cursor.fetchall())
    conn.close()