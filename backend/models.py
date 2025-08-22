import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",       # your MySQL username
        password="password",  # your MySQL password
        database="college_portal"
    )
    return conn
