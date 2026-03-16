import socket
import json

def ris(primo_numero, operazione, secondo_numero):
    if(operazione=='+'):
        return primo_numero+secondo_numero
    if(operazione=='-'):
        return primo_numero-secondo_numero
    if(operazione=='*'):
        return primo_numero*secondo_numero
    if(operazione=='/'):
        return primo_numero/secondo_numero
    
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

while True:
    data, mittente = sock.recvfrom()
    if not data:
        break
    data = data.decode()
    data = json.loads(data)
    primo_numero = data["primo_numero"]
    operazione = data["operazione"]
    secondo_numero = data["secondo_numero"]

    sock.sendto(ris(primo_numero, operazione, secondo_numero).encode(), mittente)


