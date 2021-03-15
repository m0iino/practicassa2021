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
Log = open("C:\\Users\\Moino\\Documents\\1er2021\\sa\\lab\\practica4\\Repartidor\\log.txt", "w")
Log.write(str(now)+" "+str(response.json())+" "+"\n")

# Log del estado del pedido solicitado
Log.write(str(now)+" id pedido: "+str(response.json().get("id"))+" id cliente: " +str(response.json().get("idCliente"))+" estado: "+str(response.json().get("estado"))+" "+"\n")


# entregar pedido
# hacemos un request solicitando el pedido del cliente 1
response = requests.get(urlsol+"1")
pedido = response.json()
pedido["estado"]= 1

# actualizamos el pedido del cliente 
headers = {
    'content-type' : 'application/json'
}
data = pedido
response = requests.request("POST", urlsol+"actualizar",data=json.dumps(data),headers = headers)


if response.status_code == 201:
    # Pedido creado correctamente y lo agregamos en el log
    Log.write(str(now)+"pedido actualizado"+"\n")
else:
    # error no se pudo crear el pedido y se guarda en el log
    Log.write(str(now)+" error al actualizar pedido\n")
# cerramos el log
Log.close()
