import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='localhost',
                             user='root',
                             password='123456789',
                             database='db')

cursor = conn.cursor()

#*Select example
cursor.execute(
    "SELECT nombre, apellido FROM clientes"
)
for nombre, apellido in cursor.fetchall():
    print("{0} {1}".format(nombre, apellido))
    

#* Insert Example
cursor.execute(
    "INSERT INTO clientes VALUES (%s, %s)",
    ("Recursos", "Python")
)
# Guardar cambios.
conn.commit()
conn.close()