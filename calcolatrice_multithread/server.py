# Server TCP multithread che accetta connessioni da più client e calcola risultati di operazioni aritmetiche
import socket                   # Per la comunicazione di rete
import json                     # Per la gestione dei dati in formato JSON
from threading import Thread    # Per gestire le connessioni in parallelo (multithreading)

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

# Funzione eseguita in un thread per ogni client connesso
def ricevi_comandi(sock_service, addr_client):
    with sock_service as sock_client:
        dati = sock_client.recv(DIM_BUFFER).decode() #converte da byte a stringa json
        dati = json.loads(dati) #loads() converte da stringa a dizionario
        
        risultato = ris(dati["primo_numero"], dati["operazione"], dati["secondo_numero"])

        sock_client.sendall(str(risultato).encode())#sendall() accetta solo parametri di tipo byte, e li manda al client

# Funzione che accetta una nuova connessione e lancia un thread per gestirla
def ricevi_connessioni(sock_listen):
    sock_service, address_client = sock_listen.accept()  # Accetta la connessione da un client
    try:
        # Avvia un nuovo thread per gestire i comandi del client
        Thread(target=ricevi_comandi, args=(sock_service, address_client)).start()
    except Exception as e:
        print(e)  # Stampa eventuali errori nella creazione del thread

# Funzione principale che avvia il server e resta in ascolto di nuove connessioni
def avvia_server(indirizzo, porta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
        # Imposta l'opzione per riutilizzare subito la porta dopo un riavvio del server
        sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Associa il server all'indirizzo e alla porta specificati
        sock_server.bind((indirizzo, porta))

        # Mette il server in ascolto con una coda massima di 5 connessioni pendenti
        sock_server.listen(5)

        # Ciclo infinito per accettare e gestire connessioni multiple
        while True:
            ricevi_connessioni(sock_server)
            print(f" ---- Server in ascolto su {indirizzo}:{porta} ----")

# --- MAIN ---
# Configurazione del server
IP = "127.0.0.1"          # Indirizzo locale
PORTA = 65432             # Porta di ascolto
DIM_BUFFER = 1024         # Dimensione del buffer per la ricezione dati

# Avvio del server
avvia_server(IP, PORTA)