


import os
import mysql.connector

db = mysql.connector.connect(
    host=os.environ.get("dpg-d6e18h75r7bs73bbfskg-a"),
    user=os.environ.get("feminova_user"),
    password=os.environ.get("InNmYo9axkBI2uFZ8qS1vrcRLQ7XpofF"),
    database=os.environ.get("feminova"),
)

def get_cursor():
    return db.cursor(dictionary=True, buffered=True)