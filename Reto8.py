import pymongo 
import prettytable
client = pymongo.MongoClient('mongodb://root:1234@172.17.0.2:27017/')
db = client['CochesDB']
collection = db['coches']
#y=collection.get()
x = collection.find()
#print(f"ID   MARCA        MODELO     COLOR      KM      PRECIO")
#print("--------------------------------------------------------")
#for f in x:
    #print(f"{f[0]:<5}{f[1]:<12} {f[2]:<10} {f[3]:<10} {f[4]:<7} {f[5]:<6}")
#print("--------------------------------------------------------")
#print(x[0])
#print(y)
tabla=prettytable.PrettyTable(["_ID","ID","Marca","Modelo","Kilometraje","Precio"])
idcont=0
for f in x:
    idcont=idcont+1
    tabla.add_row([
        f.get("_id", ""),
        f.get("id", idcont),
        f.get("marca", ""),
        f.get("modelo", ""),
        f.get("km", ""),
        f.get("precio", "")
    ])

print(tabla)