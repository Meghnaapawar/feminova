
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Carlos@55",
    database="feminova_db",
)

def get_cursor():
    return db.cursor(dictionary=True, buffered=True)

