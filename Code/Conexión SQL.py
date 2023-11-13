import pymysql


connection = pymysql.connect(host="localhost", user="root", password="123456789", database="pokemon")

cursor = connection.cursor()
cursor.execute("SELECT TYPE1, COUNT(TYPE1) FROM STATS GROUP BY TYPE1")
result = cursor.fetchall()
for row in result:
    print(row)
cursor.close()
connection.close()