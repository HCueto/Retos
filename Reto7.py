import mysql.connector
import json
import Reto6Funciones
import tabulate

with open('datos_conexion.json','r') as file:
    config = json.load(file)


conexion = Reto6Funciones.conectar(config)
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

cabeceras = [columna[0] for columna in cursor.description]
print(tabulate.tabulate(registros, headers=cabeceras, tablefmt="grid"))
