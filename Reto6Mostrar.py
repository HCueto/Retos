import mysql.connector
import json
import Reto6Funciones

coches = Reto6Funciones.consultaCoches()
print(f"ID   MARCA        MODELO     COLOR      KM      PRECIO")
print("--------------------------------------------------------")
for coche in coches:
    print(f"{coche[0]:<5}{coche[1]:<12} {coche[2]:<10} {coche[3]:<10} {coche[4]:<7} {coche[5]:<6}")
print("--------------------------------------------------------")