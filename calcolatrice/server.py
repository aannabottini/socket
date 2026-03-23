import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #viene creato il socket udp
sock.bind((SERVER_IP, SERVER_PORT)) #il server si mette in ascolto su un IP e una porta specifici

def ris(primo_numero, operazione, secondo_numero):
    if(operazione=='+'):
        return primo_numero+secondo_numero
    if(operazione=='-'):
        return primo_numero-secondo_numero
    if(operazione=='*'):
        return primo_numero*secondo_numero
    if(operazione=='/'):
        return primo_numero/secondo_numero
    
while True:
    data, mittente = sock.recvfrom(1024) #riceve data e mittente dal socket
    if not data:
        break
    data = data.decode() #data da byte a stringa
    data = json.loads(data) #metodo da stringa JSON a dizionario Python

    #estrazione dei dati
    primo_numero = data["primo_numero"] 
    operazione = data["operazione"]
    secondo_numero = data["secondo_numero"]

    sock.sendto(str(ris(primo_numero, operazione, secondo_numero)).encode(), mittente) 
    #metodo ris(): è la funzione a riga 4
    #metodo encode() trasforma da stringa a byte FUNZIONA SOLO SU STRINGHE
    #metodo sendto() manda la risposta al client

