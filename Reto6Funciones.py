import mysql.connector
import json

# Datos de conexión
with open('datos_conexion.json','r') as file:
    config = json.load(file)

# Conectar a la base de datos
def conectar(config):
    conexion = mysql.connector.connect(
        user = config['database']['user'],
        password = config['database']['password'],
        host = config['database']['host'],
        port = config['database']['port'],
        database = config['database']['dbname']
    )
    if conexion.is_connected():
        print("Conexión exitosa")
        return conexion
    else:
        print("Error de conexión")
        return None
def consultaCoches():
    conexion = conectar(config)
# Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

# Consulta para obtener los registros de la tabla de coches
    query = "SELECT * FROM coches"

# Ejecutar la consulta
    cursor.execute(query)

# Obtener los registros
    registros = cursor.fetchall()
    cursor.close()
    conexion.close()
    return registros
    

    