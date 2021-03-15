# importamos json
import json
# importamos requests
import requests
# importamos fecha y hora
from datetime import datetime
# solicitud de un pedido
# url de la solicitud
urlsol = "http://localhost:54736/api/bus/"

# hacemos un request y lo guardamos en un response
response = requests.get(urlsol+"1")
# Fecha y hora 
now = datetime.now()
# abrimos el archivo log y guardamos
Log = open("C:\\Users\\Moino\\Documents\\1er2021\\sa\\lab\\practica4\\Cliente\\log.txt", "w")
Log.write(str(now)+" "+str(response.json())+" "+"\n")

# Log del estado del pedido solicitado
Log.write(str(now)+" id pedido: "+str(response.json().get("id"))+" id cliente: " +
          str(response.json().get("idCliente"))+" estado: "+str(response.json().get("estado"))+" "+"\n")


# agregar pedido

# formato json para el header del request
headers = {
    'content-type': 'application/json'
}
# guardamos en una variable tipo json el pedido agregar
data = {
    "id": 10,
    "descripcion": "Tacos",
    "idrestaurante": 10,
    "idrepartidor": 10,
    "idcliente": 11,
    "estado": 0
}

# hacemos el request tipo post y lo guardamos en un response
response = requests.request("POST", urlsol+"agregar",
                            data=json.dumps(data), headers=headers)

#print("esto trae",response)
#if response.status_code == 201:
    # Pedido creado correctamente y lo agregamos en el log
Log.write(str(now)+'pedido agregado'+"\n"+str(data))
#else:
    # error no se pudo crear el pedido y se guarda en el log
#    Log.write(str(now)+" error al agregar pedido\n")
# cerramos el log
Log.close()
