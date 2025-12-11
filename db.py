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

'''def fetch_all(table_name):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {table_name}")
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error fetching {table_name}: {err}")
        finally:
            conn.close()
    return []'''

def fetch_one(table_name, column, value):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {table_name} WHERE {column}=%s", (value,))
            return cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error fetching {table_name}: {err}")
        finally:
            conn.close()
    return None

def insert_row(table_name, columns, values):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cols = ", ".join(columns)
            placeholders = ", ".join(["%s"] * len(values))
            cursor.execute(f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})", values)
            conn.commit()
        except mysql.connector.Error as err:
            print(f"Error inserting into {table_name}: {err}")
        finally:
            conn.close()

def update_row(table_name, set_column, set_value, condition_column, condition_value):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE {table_name} SET {set_column}=%s WHERE {condition_column}=%s",
                           (set_value, condition_value))
            conn.commit()
        except mysql.connector.Error as err:
            print(f"Error updating {table_name}: {err}")
        finally:
            conn.close()

def delete_row(table_name, condition_column, condition_value):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {table_name} WHERE {condition_column}=%s", (condition_value,))
            conn.commit()
        except mysql.connector.Error as err:
            print(f"Error deleting from {table_name}: {err}")
        finally:
            conn.close()

def fetch_all_dict(table_name):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {table_name}")
        results = cursor.fetchall()
        conn.close()
        return results
    return None

def execute_query(query, values=None):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            conn.commit()
        except mysql.connector.Error as err:
            print(f"DB error: {err}")
            raise err
        finally:
            conn.close()
