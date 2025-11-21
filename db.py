import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootpassword11!&##22heherroot%RRww1",
        database="genevaauto"
    )
