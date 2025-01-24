import mysql.connector

# Datos de conexión
username = 'root'
password = '1234'
host = '172.17.0.2'
database = 'CochesDB'

# Conectar a la base de datos
conexion = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    port=3306,
    database=database
    )

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Consulta para obtener los registros de la tabla de coches
query = "SELECT * FROM coches"

# Ejecutar la consulta
cursor.execute(query)

# Obtener los registros
registros = cursor.fetchall()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()

# Imprimir los registros de forma estética
print(f"ID   MARCA        MODELO     COLOR      KM      PRECIO")
print("--------------------------------------------------------")
for registro in registros:
    print(f"{registro[0]:<5}{registro[1]:<12} {registro[2]:<10} {registro[3]:<10} {registro[4]:<7} {registro[5]:<6}")
print("--------------------------------------------------------")