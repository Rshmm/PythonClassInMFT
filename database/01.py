import mysql.connector as sql_con
from mysql.connector import cursor

db = sql_con.connect(host="localhost", database="stuff",user="rootasdf", password="root123")

print("connect")

db.close()

print("disconnect")