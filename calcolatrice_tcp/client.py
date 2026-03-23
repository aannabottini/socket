#Client con costrutto with
import socket
import json

HOST = '127.0.0.1' # Indirizzo del server
PORT = 65432       # Porta usata dal server

primo_numero = float(input("Inserisci primo numero: "))
operazione = input("Inserisci l'operazione (simbolo): ")
secondo_numero = float(input("Inserisci il secondo numero: "))

messaggio = {
    "primo_numero" : primo_numero,
    "operazione" : operazione,
    "secondo_numero" : secondo_numero
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))
    sock_service.sendall(json.dumps(messaggio).encode()) # invio direttamente in formato byte
    risultato = sock_service.recv(1024) # il parametro indica la dimensione massima dei dati che possono essere ricevuti in una sola volta

risultato = risultato.decode()
print(f"{primo_numero} {operazione} {secondo_numero} = {risultato}")
    
