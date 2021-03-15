# recibimos los parametros para escribir en el log y retornamos 1 porque son correctos
def escribirlog(path,fecha,idpedido,idcliente,estado):
    return 1

# se reciben los parametros del pedido y retorna 1 porque son correctos
def agregarpedido(idpedido,descripcion,idrestaurante,idrepartidor,idcliente,estado):
    return 1

# se reciben los parametros para consultar el pedido y retornamos 1 porque son correectos
def consultarpedido(idpedido,idcliente):
    return 1

# metodo de prueba assert si los datos son correctos regresa 1
def test_escribirlog():
    path = "C:\\Users\\Moino\\Documents\\1er2021\\sa\\lab\\practica4\\Cliente\\log.txt"
    fecha = "14/03/2021"
    idpedido = "1"
    idcliente = "4"
    estado = 0
    assert escribirlog(path,fecha,idpedido,idcliente,estado) == 1
# metodo de prueba assert si los datos son correctos regresa 1
def test_agregarpedido():
    idpedido = "1"
    descripcion = "tacos"
    idrestaurante = "10"
    idrepartidor = "10"
    idcliente = "11"
    estado = 0
    assert agregarpedido(idpedido,descripcion,idrestaurante,idrepartidor,idcliente,estado) == 1

# metodo de prueba assert si los datos son correctos regresa 1
def test_consultarpedido():
    idpedido = "1"
    idcliente = "11"
    assert consultarpedido(idpedido,idcliente) == 1


