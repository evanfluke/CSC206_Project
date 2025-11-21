import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rootpassword11!&##22heherroot%RRww1',
            database='genevaauto'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
