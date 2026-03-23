# Server
import socket
import json

# Configurazione del server
IP = "127.0.0.1"
PORTA = 65432
DIM_BUFFER = 1024

def ris(primo_numero, operazione, secondo_numero):
    if(operazione=='+'):
        risultato = primo_numero+secondo_numero
    if(operazione=='-'):
        risultato = primo_numero-secondo_numero
    if(operazione=='*'):
        risultato = primo_numero*secondo_numero
    if(operazione=='/'):
        risultato = primo_numero/secondo_numero
    return risultato
    
# Creazione della socket del server con il costrutto with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

    # Binding della socket alla porta specificata
    sock_server.bind((IP, PORTA))

    # Metti la socket in ascolto per le connessioni in ingresso
    sock_server.listen()
    print(f"Server in ascolto su {IP}:{PORTA}...")

    # Loop principale del server
    while True:
        # accetta le connessioni
        sock_service, address_client = sock_server.accept()
        with sock_service as sock_client:

            # Leggi i dati inviati dal client
            dati = sock_client.recv(DIM_BUFFER).decode() #converte da byte a stringa json
            dati = json.loads(dati) #loads() converte da stringa a dizionario

            risultato = ris(dati["primo_numero"], dati["operazione"], dati["secondo_numero"])

            sock_client.sendall((str)(risultato).encode())#sendall() accetta solo parametri di tipo byte, e li manda al client



            