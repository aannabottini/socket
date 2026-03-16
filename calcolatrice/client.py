import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

primo_numero = float(input("Inserisci primo numero: "))
operazione = input("Inserisci l'operazione (simbolo): ")
secondo_numero = float(input("Inserisci il secondo numero: "))

messaggio = {
    "primo_numero" : primo_numero,
    "operazione" : operazione,
    "secondo_numero" : secondo_numero
}

messaggio = json.dumps(messaggio) #json.dumps() trasforma un oggetto in una sringa formattata json

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: #viene creato il socket s
    s.sendto(messaggio.encode("UTF-8"), (SERVER_IP, SERVER_PORT)) #viene inviata la stringa codificata in byte all'indirizzo del server
    risultato = s.recv() #riceve la risposta
#chiusura blocco width
print(f"{primo_numero} {operazione} {secondo_numero} = {risultato}")
