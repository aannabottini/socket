# Client TCP multithread che invia NUM_WORKERS richieste contemporanee al server
# Ogni richiesta contiene un'operazione aritmetica da eseguire

import socket         # Per la comunicazione di rete
import json           # Per la codifica/decodifica JSON
import random         # Per generare numeri casuali
import time           # Per misurare i tempi di esecuzione
import threading      # Per gestire l'esecuzione parallela (multithreading)

# --- Configurazione ---
HOST = "127.0.0.1"           # IP del server
PORT = 65432                # Porta del server (assicurarsi che il server stia ascoltando su questa)
NUM_WORKERS = 15            # Numero di richieste (thread) da inviare in parallelo
OPERAZIONI = ["+", "-", "*", "/", "%"]  # Lista delle operazioni consentite

#1 Funzione genera_richieste che accetta indirizzo e porta
def genera_richieste(address, port):
    #2 Crea un socket tcp e stabilisce la connessione 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((address, port))  # Connessione al server

        #3 Genera dei numeri casuali per eseguire l'operazione
        primoNumero = random.randint(0, 100)
        operazione = OPERAZIONI[random.randint(0, 3)]  # Scegli operazione a caso (tra le prime 4)
        secondoNumero = random.randint(0, 100)

        #4 Mette i dati in un dizionario 
        messaggio = {
            "primoNumero": primoNumero,
            "operazione": operazione,
            "secondoNumero": secondoNumero
        }
        messaggio = json.dumps(messaggio) #prende il dizionario messaggio e lo trasforma in una stringa json

        ##5 converte la stringa json in byte siccome il passaggio di dati può avvenire solo in questo modo
        sock_service.sendall(messaggio.encode("UTF-8"))

        #6 Registra il tempo da quando inizia
        start_time_thread = time.time()

        #7 Attende la risposta del server
        data = sock_service.recv(1024)

    #8 Calcola il tempo finale 
    end_time_thread = time.time()
    print("Received: ", data.decode()) #decode() trasforma da byte a stringa
    print(f"{threading.current_thread().name} exec time = ", end_time_thread - start_time_thread) #current_thread() identifica il thread in esecuzione
                                                                                                    #stampa inoltre il tempo di esecuzione 

# --- Punto di ingresso del programma ---
if __name__ == "__main__":
    start_time = time.time()  # Tempo di inizio totale

    #9 crea una lista di thread
    threads = [
        threading.Thread(target=genera_richieste, args=(HOST, PORT))
        for _ in range(NUM_WORKERS)
    ]

    #10 Avvio dei thread
    [thread.start() for thread in threads]

    #11 Il programma si stoppa fino a che tutti i thread non hanno terminato
    [thread.join() for thread in threads]

    end_time = time.time()  # Tempo di fine totale

    # Stampa il tempo complessivo impiegato per eseguire tutte le richieste
    print("Tempo totale impiegato = ", end_time - start_time)