__author__ = 'luyangsheng'
import mysql.connector

cnt = mysql.connector.connect(user="root", password="root", database="mysql")

cursor = cnt.cursor()
cursor.execute("select * from user")
res = cursor.fetchone()
print(res)
