import socket
from time import sleep
import binascii
import os

# Adresse IP et port de destination
server_address = ('1.1.1.1', 4626)

# Adresse IP de l'interface wlan0 de votre Raspberry Pi
source_address = '1.1.1.2'

numero_prgm = 20
dim = 50
speed = 10

response = os.system("ping -c 1 1.1.1.1")
print(response)

prgm = str(format(3+numero_prgm, "02X")+format(numero_prgm-1,"02x")).lower()
hex_message_prog = f'fbc5{str(prgm)}b23a0c00'

format_dim = str(format(int(dim * 0x1F / 100), "02X")).lower()
format_speed = str(format(int((speed) * 0x1F / 100 + 1), "02X")).lower()

hex_message_speed = f'fbc1ff{format_speed}{format_dim}0100a8003a0c00b23a0c00'
print(len(hex_message_speed))

message = binascii.unhexlify(hex_message_speed)
message_prgm = binascii.unhexlify(hex_message_prog)

# Convertir la chaîne hexadécimale en une séquence d'octets

# Créer un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Lier le socket à l'interface wlan0
    sock.bind((source_address, 0))

    # Envoyer le message au serveur
    sent = sock.sendto(message, server_address)
    sleep(0.2)
    sent = sock.sendto(message_prgm, server_address)
    print(f"Sent {sent} bytes to {server_address} from {source_address}")

finally:
    # Fermer le socket
    sock.close()


