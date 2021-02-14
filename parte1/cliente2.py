import secrets
import base64
import hashlib
import hmac
import os
payload = '{"carnet":"201114527","nombre":"cristian"}'
header = '{"alg":"HS256","typ":"JWT"}'
secret = "secreto201114527"

def menu():
    #os.system('cls')
    #print(header)
    #print("payload",payload)
    print("Seleccione una opción\n")
    print("\t1 - generar token jwt")
    print("\t2 - validar token jwt")
    print("\t9 - salir")


while(True):
    
    menu()
    opcion = input("inserte una opcion >>")

    if opcion == "1":
        # codificamos el header en ascii 
        header_bytes = header.encode('ascii')
        # codificamos en base64 
        base64_bytes = base64.b64encode(header_bytes)
        # imprimimos la codificado en bytes
        #print("base64 ", base64_bytes)
        # decodificamos el mensaje de ascii
        base64_message = base64_bytes.decode('ascii')
        # imprimimos el string codificado
        #print("enconde ",base64_message)
        #contatemamos al token el header codificado
        token_jwt = base64_message+"."
        # convertimos nuevamente para verificar el string
        b64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(b64_bytes)
        message = message_bytes.decode('ascii')
        #print("decode ",message)


        # codificamos el payload
        payload_bytes = payload.encode('ascii')
        # codificamos en base64 
        base64_bytes = base64.b64encode(payload_bytes)
        # imprimimos la codificado en bytes
        #print("base64 ", base64_bytes)
        # decodificamos el mensaje de ascii
        base64_message = base64_bytes.decode('ascii')
        # imprimimos el string codificado
        #print("enconde ",base64_message)
        #concatenamos al token el payload codificado
        token_jwt += base64_message
        # convertimos nuevamente para verificar el string
        b64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(b64_bytes)
        message = message_bytes.decode('ascii')
        #print("decode ",message)
        # creamos el secret en hexadecimal con 16 bits
        
        #print("secret",secret)
        digest = hmac.new(secret.encode('ascii'), token_jwt.encode('ascii'), hashlib.sha256)
        s_e = digest.hexdigest()
        ba = bytearray.fromhex(s_e)
        base64_val = base64.b64encode(ba).decode('ascii')

        #print(base64_val[:len(base64_val)-1])
        token_jwt += "."+base64_val[:len(base64_val)-1]
        print("token jwt: \n",token_jwt)
    elif opcion =="2":
        token = input("inserte token jwt: ")
        cad = token.split(".")
        
        pl_e = cad[1]
        pl = pl_e.encode('ascii')
        pl_b = base64.b64decode(pl)
        pl_d = pl_b.decode('ascii')
        print("payload ",pl_d)
        # codificamos el header en ascii 
        header_bytes = header.encode('ascii')
        # codificamos en base64 
        base64_bytes = base64.b64encode(header_bytes)
        # imprimimos la codificado en bytes
        #print("base64 ", base64_bytes)
        # decodificamos el mensaje de ascii
        base64_message = base64_bytes.decode('ascii')
        # imprimimos el string codificado
        #print("enconde ",base64_message)
        #contatemamos al token el header codificado
        token_jwt2 = base64_message+"."
        payload_bytes = pl_d.encode('ascii')
        # codificamos en base64 
        base64_bytes = base64.b64encode(payload_bytes)
        # imprimimos la codificado en bytes
        #print("base64 ", base64_bytes)
        # decodificamos el mensaje de ascii
        base64_message = base64_bytes.decode('ascii')
        # imprimimos el string codificado
        #print("enconde ",base64_message)
        #concatenamos al token el payload codificado
        token_jwt2 += base64_message
        # convertimos nuevamente para verificar el string
        b64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(b64_bytes)
        message = message_bytes.decode('ascii')
        #print("decode ",message)
        # creamos el secret en hexadecimal con 16 bits
        
        #print("secret",secret)
        digest = hmac.new(secret.encode('ascii'), token_jwt2.encode('ascii'), hashlib.sha256)
        s_e = digest.hexdigest()
        ba = bytearray.fromhex(s_e)
        base64_val = base64.b64encode(ba).decode('ascii')

        #print(base64_val[:len(base64_val)-1])
        token_jwt2 += "."+base64_val[:len(base64_val)-1]
        print("token jwt2: \n",token_jwt2)
        if(token_jwt == token_jwt2):
            print("token valido")
        else:
            print("token invalido")

    elif opcion=="9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")



