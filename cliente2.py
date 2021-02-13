import secrets
import base64
import hashlib
import hmac

payload = '{"carnet":"201114527","nombre":"cristian"}'
header = '{"alg":"HS256","typ":"JWT"}'

# codificamos el header en ascii 
header_bytes = header.encode('ascii')
# codificamos en base64 
base64_bytes = base64.b64encode(header_bytes)
# imprimimos la codificado en bytes
print("base64 ", base64_bytes)
# decodificamos el mensaje de ascii
base64_message = base64_bytes.decode('ascii')
# imprimimos el string codificado
print("enconde ",base64_message)
#contatemamos al token el header codificado
token_jwt = base64_message+"."
# convertimos nuevamente para verificar el string
b64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(b64_bytes)
message = message_bytes.decode('ascii')
print("decode ",message)


# codificamos el payload
payload_bytes = payload.encode('ascii')
# codificamos en base64 
base64_bytes = base64.b64encode(payload_bytes)
# imprimimos la codificado en bytes
print("base64 ", base64_bytes)
# decodificamos el mensaje de ascii
base64_message = base64_bytes.decode('ascii')
# imprimimos el string codificado
print("enconde ",base64_message)
#concatenamos al token el payload codificado
token_jwt += base64_message
# convertimos nuevamente para verificar el string
b64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(b64_bytes)
message = message_bytes.decode('ascii')
print("decode ",message)
# creamos el secret en hexadecimal con 16 bits
secret = "secreto201114527"
print("secret",secret)
digest = hmac.new(secret.encode('ascii'), token_jwt.encode('ascii'), hashlib.sha256)
s_e = digest.hexdigest()
ba = bytearray.fromhex(s_e)
base64_val = base64.b64encode(ba).decode('ascii')

print(base64_val[:len(base64_val)-1])
token_jwt += "."+base64_val[:len(base64_val)-1]
print("token jwt: \n",token_jwt)